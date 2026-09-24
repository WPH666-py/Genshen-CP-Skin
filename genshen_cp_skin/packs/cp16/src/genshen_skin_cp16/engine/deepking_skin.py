# -*- coding: utf-8 -*-
"""
原神CP16 · 温迪×芭芭拉 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp16.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp16 deepking)会把本调色板写成 genshen-cp16.skin.json,
并生成可视化预览 genshen-cp16-preview.html, 方便导入前先看效果。
"""
from ..characters import cp16_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fdfbf6",
    "bgText": "#1f2b3d",
    "sidebarBg": "#eef4f8",
    "sidebarText": "#263447",
    "sidebarHover": "#f5ebd2",
    "sidebarSelected": "#ebdcb0",
    "sidebarHeader": "#7c8b9e",
    "editorBg": "#fdfbf6",
    "tabsBg": "#f7f3e9",
    "tabBg": "#edf1f5",
    "tabText": "#546479",
    "tabActiveBg": "#fdfbf6",
    "tabActiveText": "#1f2b3d",
    "aiBg": "#faf7f0",
    "aiText": "#1f2b3d",
    "aiTabText": "#546479",
    "userBubbleBg": "#e8ddbe",
    "userBubbleText": "#1f2b3d",
    "aiBubbleBg": "#fdfbf6",
    "aiBubbleText": "#1f2b3d",
    "aiBubbleBorder": "#d8c9a8",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fdfbf6",
    "inputText": "#1f2b3d",
    "inputBorder": "#b9a97f",
    "accent": "#c9a227",
    "accentText": "#231c05",
    "border": "#d8c9a8",
    "chipBg": "#f0e6cd",
    "chipText": "#7a6014",
    "chipBorder": "#b9a97f",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#151e2b",
    "bgText": "#e9eef5",
    "sidebarBg": "#1e2a3a",
    "sidebarText": "#c2cddb",
    "sidebarHover": "#2a3a4e",
    "sidebarSelected": "#384c64",
    "sidebarHeader": "#8291a3",
    "editorBg": "#151e2b",
    "tabsBg": "#19222f",
    "tabBg": "#1e2a3a",
    "tabText": "#8b99ab",
    "tabActiveBg": "#2a3a4e",
    "tabActiveText": "#e9eef5",
    "aiBg": "#1e2a3a",
    "aiText": "#e9eef5",
    "aiTabText": "#8b99ab",
    "userBubbleBg": "#4d431f",
    "userBubbleText": "#f7f2e4",
    "aiBubbleBg": "#232f40",
    "aiBubbleText": "#e9eef5",
    "aiBubbleBorder": "#3d5068",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#ecd9a0",
    "inputBg": "#202b3a",
    "inputText": "#e9eef5",
    "inputBorder": "#3d5068",
    "accent": "#e0bc4a",
    "accentText": "#1a1406",
    "border": "#3d5068",
    "chipBg": "#3a3620",
    "chipText": "#eee0b8",
    "chipBorder": "#7a6a35",
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
