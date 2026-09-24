# -*- coding: utf-8 -*-
"""生成 genshen_cp_skin/catalog.json —— 只含 CP 套件，编号重排为 1..24。

来源是 Desktop-Skin 那份已验证过的 catalog（它的 CP 条目是从各仓库实测出来的），
这里只做筛选 + 重新编号 + 补上「包内自带」相关字段，避免再写一遍提取逻辑。

新增字段：
  pack_dir   —— 该套在包内的目录名（packs/<pack_dir>/）
  engine     —— 引擎入口信息（cli 相对路径、模块名、是否有 pet/deepking）
  bundled    —— 该套的源图与引擎代码是否随包自带
"""
import io
import json
import os
import re
import sys

K = r"D:\projects-py\Genshen-skins"
SRC = os.path.join(K, "_desktop-skin", "repo", "catalog.json")
DST_REPO = os.path.join(K, "Genshen-CP-Skin")
DST = os.path.join(DST_REPO, "genshen_cp_skin", "catalog.json")


def engine_module(root, cp):
    """定位引擎，返回 (相对仓库根的 cli 路径, 包名, 是否带 engine 子目录)。"""
    pkg_flat = "genshin_skin_cp%d" % cp       # CP1 的拼写
    pkg = "genshen_skin_cp%d" % cp
    for pkgname, sub in ((pkg_flat, None), (pkg, "engine")):
        base = os.path.join(root, "src", pkgname)
        if os.path.isfile(os.path.join(base, "cli.py")):
            return "src/%s/cli.py" % pkgname, pkgname, False
        if sub and os.path.isfile(os.path.join(base, sub, "cli.py")):
            return "src/%s/%s/cli.py" % (pkgname, sub), pkgname, True
    return None, None, None


def main():
    cat = json.load(io.open(SRC, encoding="utf-8"))
    cps = [s for s in cat["skins"] if s.get("kind") == "cp"]
    cps.sort(key=lambda s: s["cp"])
    print("来源 catalog 里的 CP: %d 套" % len(cps))

    out = []
    for i, s in enumerate(cps, start=1):
        repo = os.path.join(K, s["repo"])
        cli_rel, pkg, has_engine = engine_module(repo, s["cp"])
        if not cli_rel:
            print("  跳过 %s：找不到引擎 cli.py" % s["id"])
            continue
        # 核对源图都在
        srcs = [p for p in (s.get("sources") or [])
                if os.path.isfile(os.path.join(repo, p.replace("/", os.sep)))]
        if len(srcs) != len(s.get("sources") or []):
            print("  警告 %s：源图缺 %d 个" % (s["id"], len(s.get("sources") or []) - len(srcs)))
        e = {
            "id": "cp%d" % s["cp"],
            "no": i,
            "cp": s["cp"],
            "name": s["name"],
            "nameEn": s.get("nameEn") or "",
            "char": s["char"],
            "charEn": s.get("charEn") or "",
            "accent": s["accent"],
            "tagline": s.get("tagline") or "",
            "aliases": sorted(set((s.get("aliases") or []) + ["cp%d" % s["cp"]])),
            # 源仓库仍保留（素材版权页、单套 README 都在那儿）
            "repo": s["repo"],
            "url": s["url"],
            "raw": s["raw"],
            "clone": s["clone"],
            "sources": srcs,
            "modes": len(srcs) * 3,
            "pack_dir": "cp%02d" % s["cp"],
            "engine": {
                "cli": cli_rel,
                "package": pkg,
                "engine_subdir": bool(has_engine),
                "module": ("%s.engine.cli" % pkg) if has_engine else ("%s.cli" % pkg),
                "pet": bool(s["paths"].get("engine_pet")),
                "deepking": bool(s["paths"].get("engine_deepking")),
            },
            "caps": {
                "wallpaper": True,
                "desktop": bool(s["caps"].get("desktop")),
                "vscode": bool(s["caps"].get("vscode")),
                "deepking": bool(s["caps"].get("deepking")),
            },
            "vsix": s["paths"].get("vsix"),
            "deepking_css": s["paths"].get("deepking_css"),
            "ext": s.get("ext") or {},
            "bundled": {
                "sources": True,
                "engine": True,
                "vsix": False,        # VSIX 44 MB，按需联网取
            },
        }
        out.append(e)

    doc = {
        "schema": 2,
        "family": "原神 CP 壁纸套件",
        "owner": "WPH666-py",
        "repo": "Genshen-CP-Skin",
        "pypi": "genshen-cp-skin",
        "cli": "gc",
        "homepage": "https://github.com/WPH666-py/Genshen-CP-Skin",
        "generated_at": cat.get("generated_at"),
        "count": len(out),
        "note": "素材（源图）与各套自带引擎均在包内，装完即可离线使用；"
                "VSIX 与吉祥物等可选件按需联网取。",
        "packs": out,
    }
    io.open(DST, "w", encoding="utf-8", newline="\n").write(
        json.dumps(doc, ensure_ascii=False, indent=1) + "\n")
    print()
    print("已写出 %s" % DST)
    print("CP 套件: %d 套" % len(out))
    print("源图总数: %d" % sum(len(e["sources"]) for e in out))
    print("摆法总数: %d" % sum(e["modes"] for e in out))
    print()
    for e in out:
        print("  %-5s no=%-3d %-30s %-9s %d源图/%d摆法  %s"
              % (e["id"], e["no"], e["name"], e["accent"], len(e["sources"]),
                 e["modes"], e["engine"]["module"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
