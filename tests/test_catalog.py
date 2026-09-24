# -*- coding: utf-8 -*-
"""catalog 与包内素材的自洽性测试（零依赖、不联网）。

重点检查「声称的东西是否真的在包里」——这是本包立身之本：
如果 catalog 说有 24 套、每套带 N 个文件，那 wheel 里就必须真的有这些文件。

    py -3 -m unittest discover -s tests -v
"""
import io
import json
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from genshen_cp_skin import catalog as cat_mod       # noqa: E402
from genshen_cp_skin import repo                     # noqa: E402

EXPECTED_PACKS = 24
REQUIRED_PACK_FIELDS = ("id", "no", "cp", "name", "char", "accent", "sources",
                        "modes", "mode_list", "pack_dir", "engine", "caps",
                        "repo", "url", "bundled")


class CatalogTest(unittest.TestCase):
    def setUp(self):
        self.cat = cat_mod.load_catalog(refresh=True)
        self.packs = self.cat["packs"]

    def test_count(self):
        self.assertEqual(self.cat["count"], EXPECTED_PACKS)
        self.assertEqual(len(self.packs), EXPECTED_PACKS)

    def test_required_fields(self):
        for p in self.packs:
            for k in REQUIRED_PACK_FIELDS:
                self.assertIn(k, p, "%s 缺少字段 %s" % (p.get("id"), k))

    def test_ids_and_numbers(self):
        ids = [p["id"] for p in self.packs]
        self.assertEqual(len(set(ids)), EXPECTED_PACKS, "id 有重复")
        self.assertEqual([p["no"] for p in self.packs], list(range(1, EXPECTED_PACKS + 1)))
        self.assertEqual([p["cp"] for p in self.packs], list(range(1, EXPECTED_PACKS + 1)))

    def test_accents_are_hex(self):
        for p in self.packs:
            self.assertRegex(p["accent"], r"^#[0-9a-fA-F]{6}$",
                             "%s 主题色不合法: %r" % (p["id"], p["accent"]))

    def test_modes_match_mode_list(self):
        for p in self.packs:
            self.assertEqual(p["modes"], len(p["mode_list"]),
                             "%s: modes=%s 但 mode_list 有 %d 项"
                             % (p["id"], p["modes"], len(p["mode_list"])))
            self.assertGreaterEqual(p["modes"], 1, "%s 一个摆法都没有" % p["id"])

    def test_mode_ids_are_wallpaper_families(self):
        """mode_list 里只能是摆法，不能混进 list/random/pet 这类功能子命令。"""
        for p in self.packs:
            for m in p["mode_list"]:
                self.assertRegex(m["id"], r"^(single|cover|showall)\d*$",
                                 "%s 的 %r 不像摆法" % (p["id"], m["id"]))

    def test_sources_are_images(self):
        for p in self.packs:
            self.assertTrue(p["sources"], "%s 一张源图都没有" % p["id"])
            for s in p["sources"]:
                self.assertRegex(s.lower(), r"\.(jpg|jpeg|png)$", "%s: %r" % (p["id"], s))


class BundledTest(unittest.TestCase):
    """包内素材：声称自带的文件必须真的在包里。"""

    def setUp(self):
        self.packs = cat_mod.load_catalog()["packs"]

    def test_every_pack_declares_bundled_files(self):
        for p in self.packs:
            files = p["bundled"].get("file_list") or []
            self.assertTrue(files, "%s 没声明任何包内文件" % p["id"])
            self.assertEqual(p["bundled"].get("files"), len(files),
                             "%s bundled.files 与 file_list 长度不一致" % p["id"])

    def test_declared_files_exist_in_package(self):
        missing = []
        for p in self.packs:
            for rel in p["bundled"]["file_list"]:
                if repo.bundled_path(p, rel) is None:
                    missing.append("%s/%s" % (p["id"], rel))
        self.assertEqual(missing, [], "包内缺少 %d 个已声明的文件，例如 %s"
                         % (len(missing), missing[:3]))

    def test_sources_are_bundled(self):
        """每张源图都必须在包里 —— 不在就没法离线合成壁纸。"""
        missing = []
        for p in self.packs:
            for s in p["sources"]:
                if repo.bundled_path(p, s) is None:
                    missing.append("%s/%s" % (p["id"], s))
        self.assertEqual(missing, [], "这些源图没随包：%s" % missing[:5])

    def test_engine_code_is_bundled(self):
        """引擎入口也必须在包里 —— 只有图没有引擎，等于不能换壁纸。"""
        missing = []
        for p in self.packs:
            cli = p["engine"]["cli"]
            if repo.bundled_path(p, cli) is None:
                missing.append("%s/%s" % (p["id"], cli))
        self.assertEqual(missing, [], "这些引擎没随包：%s" % missing[:5])

    def test_no_vsix_bundled(self):
        """VSIX 明确不随包（44 MB），不该出现在 packs/ 里。"""
        found = []
        for p in self.packs:
            for rel in p["bundled"]["file_list"]:
                if rel.lower().endswith(".vsix"):
                    found.append("%s/%s" % (p["id"], rel))
        self.assertEqual(found, [], "VSIX 不该随包：%s" % found[:3])

    def test_no_pycache_bundled(self):
        bad = []
        for p in self.packs:
            for rel in p["bundled"]["file_list"]:
                if "__pycache__" in rel or rel.endswith((".pyc", ".pyo")):
                    bad.append("%s/%s" % (p["id"], rel))
        self.assertEqual(bad, [], "缓存文件不该随包：%s" % bad[:5])

    def test_pack_dirs_are_unique(self):
        dirs = [p["pack_dir"] for p in self.packs]
        self.assertEqual(len(set(dirs)), len(dirs), "pack_dir 有重复")


class FindTest(unittest.TestCase):
    def setUp(self):
        self.cat = cat_mod.load_catalog()

    def _find(self, key):
        p = cat_mod.find_pack(self.cat, key)
        return p["id"] if p else None

    def test_by_id(self):
        self.assertEqual(self._find("cp24"), "cp24")
        self.assertEqual(self._find("cp1"), "cp1")

    def test_by_number(self):
        """纯数字当序号解：gc show 5 是第 5 套。"""
        for p in self.cat["packs"]:
            self.assertEqual(self._find(str(p["no"])), p["id"],
                             "序号 %d 应指向 %s" % (p["no"], p["id"]))

    def test_by_chinese(self):
        self.assertEqual(self._find("温迪"), "cp16")
        self.assertEqual(self._find("甘雨"), self._find("cp15") or self._find("cp14"))
        self.assertIsNotNone(self._find("刻晴"))

    def test_by_pinyin(self):
        self.assertEqual(self._find("venti"), "cp16")
        self.assertIsNotNone(self._find("ganyu"))

    def test_case_insensitive(self):
        self.assertEqual(self._find("CP24"), "cp24")
        self.assertEqual(self._find("Venti"), "cp16")

    def test_unknown_returns_none(self):
        self.assertIsNone(cat_mod.find_pack(self.cat, "不存在的角色xyz"))

    def test_empty_returns_default(self):
        self.assertIsNone(cat_mod.find_pack(self.cat, ""))
        self.assertEqual(cat_mod.find_pack(self.cat, "", default="x"), "x")

    def test_every_pack_findable_by_own_id(self):
        for p in self.cat["packs"]:
            self.assertEqual(self._find(p["id"]), p["id"])


class ModesTest(unittest.TestCase):
    def setUp(self):
        self.packs = cat_mod.load_catalog()["packs"]

    def test_modes_of_matches_catalog(self):
        for p in self.packs:
            self.assertEqual(len(cat_mod.modes_of(p)), p["modes"], p["id"])

    def test_cp1_has_no_showall(self):
        """CP1 是最老的一套，只有 single/cover 两族 —— 这条钉住"实测而非推算"。"""
        cp1 = [p for p in self.packs if p["id"] == "cp1"][0]
        fams = {m["id"].rstrip("0123456789") for m in cp1["mode_list"]}
        self.assertEqual(fams, {"single", "cover"},
                         "cp1 的摆法族变了？请重新核对引擎：%s" % sorted(fams))
        self.assertEqual(cp1["modes"], 6)

    def test_three_source_packs_have_nine_modes(self):
        for p in self.packs:
            if len(p["sources"]) == 3 and p["id"] != "cp1":
                self.assertEqual(p["modes"], 9, "%s 三张源图应有 9 种摆法" % p["id"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
