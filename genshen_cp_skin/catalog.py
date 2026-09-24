# -*- coding: utf-8 -*-
"""genshen_cp_skin.catalog —— 读取 catalog.json，按关键词找到用户想要的那套 CP。

检索口径：
    纯数字  -> 序号（gc show 5 = 第 5 套）
    cpN     -> 直接命中（gc show cp24）
    中文/拼音/别名 -> 模糊匹配，配对里"整段相等"优先于"只是出现过"

最后那条很重要：用户搜「甘雨」时想要的是标题为「甘雨×刻晴」的 cp15，
而不是「神里绫华×优菈×甘雨」里顺带提到甘雨的 cp14。
配对名以 × 分隔，所以按分隔后的段落比对。
"""
import json
import os
import re

_PKG_DIR = os.path.dirname(os.path.abspath(__file__))
_CACHE = None

_CANDIDATE_PATHS = (
    os.path.join(_PKG_DIR, "catalog.json"),                    # 随包发布
    os.path.join(os.path.dirname(_PKG_DIR), "catalog.json"),   # 源码仓库根目录
)

# 配对名的分隔符：cp14 是「神里绫华×优菈×甘雨」，cp24 是「甘雨×绫华」。
# 英文名用「 x 」连接（如 "Ganyu x Keqing"），但**空格本身不是分隔符** ——
# "Kamisato Ayaka x Yoimiya" 里两个空格属于同一个角色名，按空格切会把
# 「神里绫华」拆成 kamisato / ayaka，导致搜 ayaka 命中错误的那套。
PAIR_SEP = re.compile(r"[×·、,，/|+]")
_PAIR_X = re.compile(r"\s+[xX]\s+")


def catalog_path():
    for p in _CANDIDATE_PATHS:
        if os.path.exists(p):
            return p
    raise IOError("找不到 catalog.json（尝试过: %s）" % ", ".join(_CANDIDATE_PATHS))


def load_catalog(refresh=False):
    global _CACHE
    if _CACHE is not None and not refresh:
        return _CACHE
    with open(catalog_path(), encoding="utf-8") as f:
        _CACHE = json.load(f)
    return _CACHE


def packs():
    return load_catalog()["packs"]


def _norm(s):
    return (s or "").strip().lower()


def _segments(s):
    """把配对名切成角色段。

    '神里绫华×优菈×甘雨'      -> ['神里绫华','优菈','甘雨']
    'Kamisato Ayaka x Yoimiya' -> ['kamisato ayaka','yoimiya']
    """
    v = _norm(s)
    out = []
    for part in PAIR_SEP.split(v):
        for sub in _PAIR_X.split(part):
            sub = sub.strip()
            if sub:
                out.append(sub)
    return out


def score(pack, key):
    """匹配度打分，越大越匹配；0 表示不匹配。

    优先级：id 精确 > 配对段精确 > 整体子串 > 别名
    「配对段精确」是给中文名用的：搜「甘雨」要命中 cp15（甘雨×刻晴），
    而不是只把甘雨列为第三人的 cp14。
    """
    k = _norm(key)
    if not k:
        return 0
    best = 0

    # 1) id / 套件名
    #    注意 nameEn 是 "CP24 · Ganyu x Ayaka" 这种「编号 + 角色英文名」，
    #    与 charEn 内容重复；若也参与匹配，搜 ganyu 会三套同分（都靠 nameEn 命中），
    #    首位的加权就被抹平了。所以英文检索只认 charEn，不看 nameEn。
    for weight, value in ((1000, pack.get("id")), (880, pack.get("name"))):
        v = _norm(value)
        if not v:
            continue
        if v == k:
            best = max(best, weight + 10)
        elif k in v:
            best = max(best, weight)

    # 2) 角色名：整段相等优先于子串；同为整段时，**位置靠前**的优先
    for weight, value in ((900, pack.get("char")), (840, pack.get("charEn"))):
        v = _norm(value)
        if not v:
            continue
        if v == k:
            best = max(best, weight + 20)
            continue
        segs = _segments(value)
        if k in segs:
            # 「甘雨」在 cp15 里是首位（甘雨×刻晴），在 cp14 里是第三人
            # （神里绫华×优菈×甘雨）—— 前者才是用户想要的，给首位一点加权。
            pos = segs.index(k)
            best = max(best, weight + 10 - min(pos, 5))
        elif any(k in s for s in segs):
            # 是某一个「段」的子串（如 ganyu ⊂ "kamisato ayaka"？不是；
            # 如 ayaka ⊂ "kamisato ayaka" 是）——比整体子串可信
            pos = next(i for i, s in enumerate(segs) if k in s)
            best = max(best, weight - 10 - min(pos, 5))
        elif len(segs) <= 2 and k in v:
            best = max(best, weight - 20)      # 双子配对里是子串
        elif k in v:
            best = max(best, weight - 60)      # 三人以上配对里只是被提到

    # 3) 别名
    for alias in pack.get("aliases") or []:
        a = _norm(alias)
        if not a:
            continue
        if a == k:
            best = max(best, 710)
        elif k in a:
            best = max(best, 700)
    return best


def find_pack(cat, key, default=None):
    """找到一套 CP。

    纯数字优先当序号解（`gc show 5` 是第 5 套）。这里没有 CP 的 cpN 别名冲突问题
    —— 因为 id 就是 cpN 本身，`cp5` 不是纯数字，会走正常匹配。
    """
    key = (key or "").strip()
    if not key:
        return default
    if key.isdigit():
        n = int(key)
        for p in cat["packs"]:
            if p.get("no") == n:
                return p
    ranked = sorted(((score(p, key), -p.get("no", 9999), p) for p in cat["packs"]),
                    key=lambda t: (-t[0], -t[1]))
    if ranked and ranked[0][0] > 0:
        return ranked[0][2]
    return default


def search(cat, key):
    key = (key or "").strip()
    if not key:
        return []
    ranked = [(score(p, key), p) for p in cat["packs"]]
    ranked = [t for t in ranked if t[0] > 0]
    ranked.sort(key=lambda t: -t[0])
    return [p for _s, p in ranked]


def modes_of(pack):
    """该套支持的摆法 [(id, desc), ...]。

    直接读 catalog 里 `mode_list` —— 那是 `tools/probe_modes.py`
    **向各套引擎问出来的**（`skin_core.all_modes()`），不是按张数推算的。
    推算会错：CP1 只有 single/cover 两族（6 种，没有 showall），
    其余套件的 showall 也不带编号后缀。
    """
    out = []
    for m in pack.get("mode_list") or []:
        out.append((m["id"], m.get("desc") or ""))
    if out:
        return out
    # 兜底：catalog 是旧格式时按张数推（不理想，但比空好）
    modes = []
    for i in range(1, len(pack.get("sources") or []) + 1):
        modes.append(("single%d" % i, "卡片式"))
        modes.append(("cover%d" % i, "满屏"))
    return modes


def visible(pack):
    """该套在本机可用的安装目标。"""
    caps = pack.get("caps") or {}
    return [k for k in ("wallpaper", "desktop", "vscode", "deepking") if caps.get(k)]
