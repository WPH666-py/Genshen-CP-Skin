# -*- coding: utf-8 -*-
"""把 24 套 CP 的「源图 + 完整引擎代码」打进 genshen_cp_skin/packs/cpNN/。

为什么连引擎代码一起带：CP 的壁纸是各套自带引擎现算的（按用户屏幕分辨率），
所以只带 jpg 没用 —— 必须让引擎能跑起来。引擎全是相对导入，
因此保持每套内部布局不变即可，外层放哪个目录都不影响导入。

不带的东西（体积考虑，且都能按需联网取）：
  vscode/media/    缩略图，约 24 MB
  assets/background/  吉祥物，DeepKing 用，缺了只是少一张水印图
  dist/            各套自己的 wheel（CP1 有，1.2 MB）
  tools/           各套的维护脚本，运行不需要
  *.vsix           共 44 MB
"""
import io
import json
import os
import shutil
import sys

K = r"D:\projects-py\Genshen-skins"
REPO = os.path.join(K, "Genshen-CP-Skin")
PACKS = os.path.join(REPO, "genshen_cp_skin", "packs")
CAT = os.path.join(REPO, "genshen_cp_skin", "catalog.json")

SKIP_DIRS = {".git", "build", "dist", "__pycache__", ".pytest_cache", "node_modules",
             ".mypy_cache", ".ruff_cache", ".tox", "obj", "bin", ".eggs", "tools",
             "vscode-test", ".vscode-test", "media"}
SKIP_DIR_NAMES_EXACT = {"background"}          # assets/background
KEEP_EXT = {".py", ".json", ".md", ".txt", ".bat", ".sh", ".ps1", ".cfg", ".toml",
            ".css", ".js", ".html", ".yml", ".yaml", ".in", ".jpg", ".jpeg", ".png"}


def keep(rel):
    low = rel.replace("\\", "/").lower()
    parts = low.split("/")
    if any(p in SKIP_DIRS for p in parts[:-1]):
        return False
    if "vscode/media" in low or "/media/" in low:
        return False
    if "assets/background" in low:
        return False
    ext = os.path.splitext(low)[1]
    return ext in KEEP_EXT


def main():
    cat = json.load(io.open(CAT, encoding="utf-8"))
    if os.path.isdir(PACKS):
        shutil.rmtree(PACKS)
    os.makedirs(PACKS, exist_ok=True)

    total = 0
    nfiles = 0
    for e in cat["packs"]:
        src_root = os.path.join(K, e["repo"])
        dst_root = os.path.join(PACKS, e["pack_dir"])
        n = 0
        b = 0
        for dp, dn, fn in os.walk(src_root):
            dn[:] = [d for d in dn if d not in SKIP_DIRS and not d.startswith("_")]
            for f in fn:
                p = os.path.join(dp, f)
                rel = os.path.relpath(p, src_root).replace("\\", "/")
                if not keep(rel):
                    continue
                dst = os.path.join(dst_root, rel.replace("/", os.sep))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(p, dst)
                sz = os.path.getsize(p)
                n += 1
                b += sz
        total += b
        nfiles += n
        e["bundled"]["files"] = n
        print("  %-5s %-8s %3d 个文件  %6.2f MB"
              % (e["id"], e["pack_dir"], n, b / 1048576))

    # 记录每套包内带了哪些文件，便于安装时铺开与校验
    for e in cat["packs"]:
        d = os.path.join(PACKS, e["pack_dir"])
        files = []
        for dp, dn, fn in os.walk(d):
            for f in fn:
                files.append(os.path.relpath(os.path.join(dp, f), d).replace("\\", "/"))
        e["bundled"]["file_list"] = sorted(files)

    io.open(CAT, "w", encoding="utf-8", newline="\n").write(
        json.dumps(cat, ensure_ascii=False, indent=1) + "\n")

    print()
    print("套件数   : %d" % len(cat["packs"]))
    print("文件数   : %d" % nfiles)
    print("总体积   : %.2f MB" % (total / 1048576))
    print("输出     : %s" % PACKS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
