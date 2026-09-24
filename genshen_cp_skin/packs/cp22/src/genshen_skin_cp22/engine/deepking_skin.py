# -*- coding: utf-8 -*-
"""
原神CP22 · 荧×达达利亚 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp22.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp22 deepking)会把本调色板写成 genshen-cp22.skin.json,
并生成可视化预览 genshen-cp22-preview.html, 方便导入前先看效果。
"""
from ..characters import cp22_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fdfbfa",
    "bgText": "#2a2130",
    "sidebarBg": "#f3eef0",
    "sidebarText": "#332a3b",
    "sidebarHover": "#e2e6f2",
    "sidebarSelected": "#c9d3ea",
    "sidebarHeader": "#857a92",
    "editorBg": "#fdfbfa",
    "tabsBg": "#faf6f7",
    "tabBg": "#f1ebed",
    "tabText": "#5a4f67",
    "tabActiveBg": "#fdfbfa",
    "tabActiveText": "#2a2130",
    "aiBg": "#fcf9f9",
    "aiText": "#2a2130",
    "aiTabText": "#5a4f67",
    "userBubbleBg": "#dbe1f0",
    "userBubbleText": "#2a2130",
    "aiBubbleBg": "#fdfbfa",
    "aiBubbleText": "#2a2130",
    "aiBubbleBorder": "#cdc4d4",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fdfbfa",
    "inputText": "#2a2130",
    "inputBorder": "#a9a0bc",
    "accent": "#5c78b0",
    "accentText": "#ffffff",
    "border": "#cdc4d4",
    "chipBg": "#e5e2ef",
    "chipText": "#3f5382",
    "chipBorder": "#a9a0bc",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#1a1524",
    "bgText": "#ece7f2",
    "sidebarBg": "#241d31",
    "sidebarText": "#c7bfd4",
    "sidebarHover": "#312843",
    "sidebarSelected": "#423758",
    "sidebarHeader": "#877d99",
    "editorBg": "#1a1524",
    "tabsBg": "#1e1829",
    "tabBg": "#241d31",
    "tabText": "#8f86a1",
    "tabActiveBg": "#312843",
    "tabActiveText": "#ece7f2",
    "aiBg": "#241d31",
    "aiText": "#ece7f2",
    "aiTabText": "#8f86a1",
    "userBubbleBg": "#37416b",
    "userBubbleText": "#eff1f8",
    "aiBubbleBg": "#2a2239",
    "aiBubbleText": "#ece7f2",
    "aiBubbleBorder": "#453a58",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#ecd9a0",
    "inputBg": "#271f35",
    "inputText": "#ece7f2",
    "inputBorder": "#453a58",
    "accent": "#7d9ad4",
    "accentText": "#101528",
    "border": "#453a58",
    "chipBg": "#33304f",
    "chipText": "#d9e0f0",
    "chipBorder": "#63689a",
}

PALETTE_SLOTS = (
    "bg", "bgText", "sidebarBg", "sidebarText", "sidebarHover", "sidebarSelected",
    "sidebarHeader", "editorBg", "tabsBg", "tabBg", "tabText", "tabActiveBg",
    "tabActiveText", "aiBg", "aiText", "aiTabText", "userBubbleBg", "userBubbleText",
    "aiBubbleBg", "aiBubbleText", "aiBubbleBorder", "systemBubbleBg", "systemBubbleText",
    "inputBg", "inputText", "inputBorder", "accent", "accentText", "border",
    "chipBg", "chipText", "chipBorder",
)


def definition(mascot_light=None, mascot_dark=None, source=None):
    """返回完整的 DeepKing SkinDefinition(手工校色版)。"""
    skin = {
        "id": SKIN_ID,
        "name": SKIN_NAME,
        "builtin": False,
        "description": SKIN_DESC,
        "palettes": {"light": dict(LIGHT), "dark": dict(DARK)},
    }
    if source:
        skin["source"] = source
    if mascot_light or mascot_dark:
        skin["mascot"] = {
            "light": mascot_light or mascot_dark,
            "dark": mascot_dark or mascot_light,
        }
    return skin


def validate():
    """自检: 槽位齐全、色值合法、亮暗确实一浅一深、文字对比度够。"""
    from . import _color as col

    problems = []
    for label, pa in (("light", LIGHT), ("dark", DARK)):
        missing = [k for k in PALETTE_SLOTS if k not in pa]
        extra = [k for k in pa if k not in PALETTE_SLOTS]
        if missing:
            problems.append("%s 缺少槽位: %s" % (label, ", ".join(missing)))
        if extra:
            problems.append("%s 多余槽位: %s" % (label, ", ".join(extra)))
        for k, v in pa.items():
            if not col.is_hex(v):
                problems.append("%s.%s 不是合法 # 十六进制: %r" % (label, k, v))
    if not col.is_light_color(LIGHT["bg"]):
        problems.append("light.bg 不是浅色: %s" % LIGHT["bg"])
    if col.is_light_color(DARK["bg"]):
        problems.append("dark.bg 不是深色: %s" % DARK["bg"])
    for label, pa in (("light", LIGHT), ("dark", DARK)):
        for fg, bg in (("bgText", "bg"), ("sidebarText", "sidebarBg"),
                       ("aiBubbleText", "aiBubbleBg"), ("tabText", "tabsBg")):
            lf = sum(col.to_rgb(pa[fg])) / 3.0
            lb = sum(col.to_rgb(pa[bg])) / 3.0
            if abs(lf - lb) < 60:
                problems.append("%s: %s 与 %s 亮度太接近(%d), 文字可能看不清"
                                % (label, fg, bg, abs(lf - lb)))
    return problems
