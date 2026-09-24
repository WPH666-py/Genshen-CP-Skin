# -*- coding: utf-8 -*-
"""向各套引擎**直接询问**它支持哪些摆法（而不是解析源码或猜测）。

各套引擎用 `skin_core.all_modes()` / `skin_core.MODES` 暴露自己的模式清单，
所以导入它、问它，比任何静态解析都可靠。

导入方式与运行时一致：铺开仓库树 -> 把 <仓库>/src 加进 sys.path -> import。
"""
import importlib
import io
import json
import os
import sys

K = r"D:\projects-py\Genshen-skins"
REPO = os.path.join(K, "Genshen-CP-Skin")
sys.path.insert(0, REPO)

from genshen_cp_skin import catalog as cat_mod      # noqa: E402
from genshen_cp_skin import repo as repo_mod        # noqa: E402

CAT = cat_mod.catalog_path()


def modes_from(pack):
    """铺开该套并问它的引擎要模式清单。返回 [(id, label), ...]。"""
    root = repo_mod.materialize(pack, quiet=True) or repo_mod.skin_dir(pack["repo"])
    src = os.path.join(root, "src")
    pkg = pack["engine"]["package"]
    sub = "engine." if pack["engine"].get("engine_subdir") else ""
    added = src not in sys.path
    if added:
        sys.path.insert(0, src)
    try:
        mod = importlib.import_module("%s.%sskin_core" % (pkg, sub))
        # 第一优先：显式的模式清单
        raw = None
        if hasattr(mod, "all_modes"):
            raw = list(mod.all_modes())
        elif hasattr(mod, "MODES"):
            raw = list(mod.MODES)
        out = []
        for item in raw or []:
            if isinstance(item, (tuple, list)) and len(item) >= 2:
                out.append((str(item[0]), str(item[1])))
            else:
                out.append((str(item), ""))
        return out
    finally:
        if added:
            try:
                sys.path.remove(src)
            except ValueError:
                pass
        for name in list(sys.modules):
            if name.split(".")[0] == pkg:
                sys.modules.pop(name, None)


FAMILY = ("single", "cover", "showall")


def family_of(mid):
    for f in FAMILY:
        if mid.startswith(f):
            return f
    return ""


def main():
    cat = json.load(io.open(CAT, encoding="utf-8"))
    bad = []
    rows = []
    for p in cat["packs"]:
        try:
            modes = modes_from(p)
        except Exception as e:
            bad.append((p["id"], "%s: %s" % (type(e).__name__, e)))
            continue
        if not modes:
            bad.append((p["id"], "引擎没有暴露模式清单"))
            continue
        # 只保留摆法家族，滤掉 list/random 之类
        modes = [(m, d) for m, d in modes if family_of(m)]
        order = {f: i for i, f in enumerate(FAMILY)}
        modes.sort(key=lambda t: (order.get(family_of(t[0]), 9),
                                  int("".join(c for c in t[0] if c.isdigit()) or 1)))
        p["modes"] = len(modes)
        p["mode_list"] = [{"id": m, "desc": d} for m, d in modes]
        fams = []
        for m, _d in modes:
            f = family_of(m)
            if f not in fams:
                fams.append(f)
        rows.append((p["id"], len(p["sources"]), len(modes), "+".join(fams),
                     ", ".join(m for m, _ in modes)))

    io.open(CAT, "w", encoding="utf-8", newline="\n").write(
        json.dumps(cat, ensure_ascii=False, indent=1) + "\n")

    print("向引擎实测的摆法：")
    for pid, nsrc, nmodes, fams, ids in rows:
        print("  %-5s %d 张源图 -> %2d 种  %-22s %s" % (pid, nsrc, nmodes, fams, ids))
    print()
    print("套件 %d，总摆法 %d" % (len(rows), sum(r[2] for r in rows)))
    if bad:
        print()
        print("有问题 %d 套：" % len(bad))
        for pid, why in bad:
            print("  %s: %s" % (pid, why))
    print()
    print("VERDICT:", "PASS" if not bad else "FAIL")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
