# -*- coding: utf-8 -*-
"""清洗 catalog 里的英文名字段。

问题：`nameEn` 是 "CP24 · Ganyu x Ayaka" 这种带编号前缀的形式，
检索时 `ganyu` 会在它里面命中（子串），拿到与英文角色名同档的分数，
于是"甘雨"的英文查询会挑错套件（cp14 而非 cp15）。
`charEn` 才是纯角色英文名，检索应该只认它。

顺带让 `nameEn` 读起来统一：`CP24 · Ganyu x Ayaka`。
"""
import io
import json
import os
import re
import sys

CAT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "genshen_cp_skin", "catalog.json")
PREFIX = re.compile(r"^\s*(Genshin\s+)?CP\d+\s*[.·]\s*", re.I)


def main():
    cat = json.load(io.open(CAT, encoding="utf-8"))
    fixed = 0
    for p in cat["packs"]:
        ne = (p.get("nameEn") or "").strip()
        core = PREFIX.sub("", ne).strip()
        if not core:
            core = (p.get("charEn") or "").strip()
        want = "CP%d · %s" % (p["cp"], core)
        if ne != want:
            p["nameEn"] = want
            fixed += 1
        # charEn 必须是纯角色英文名（不能带编号前缀），否则检索会串
        ce = (p.get("charEn") or "").strip()
        ce2 = PREFIX.sub("", ce).strip()
        if ce2 != ce:
            p["charEn"] = ce2
            fixed += 1
    io.open(CAT, "w", encoding="utf-8", newline="\n").write(
        json.dumps(cat, ensure_ascii=False, indent=1) + "\n")
    print("修正 %d 处" % fixed)
    print()
    for p in cat["packs"][:6] + cat["packs"][-2:]:
        print("  %-5s nameEn=%-26r charEn=%r" % (p["id"], p["nameEn"], p["charEn"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
