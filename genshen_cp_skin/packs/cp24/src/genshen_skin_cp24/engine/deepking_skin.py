# -*- coding: utf-8 -*-
"""
原神CP24 · 甘雨×绫华 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp24.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp24 deepking)会把本调色板写成 genshen-cp24.skin.json,
并生成可视化预览 genshen-cp24-preview.html, 方便导入前先看效果。
"""
from ..characters import cp24_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fdfbfc",
    "bgText": "#2b1a21",
    "sidebarBg": "#f5eef1",
    "sidebarText": "#36232b",
    "sidebarHover": "#f7dfe3",
    "sidebarSelected": "#eec3ca",
    "sidebarHeader": "#8a6c78",
    "editorBg": "#fdfbfc",
    "tabsBg": "#fbf5f7",
    "tabBg": "#f3e9ed",
    "tabText": "#5c414c",
    "tabActiveBg": "#fdfbfc",
    "tabActiveText": "#2b1a21",
    "aiBg": "#fcf7f9",
    "aiText": "#2b1a21",
    "aiTabText": "#5c414c",
    "userBubbleBg": "#f2d5da",
    "userBubbleText": "#2b1a21",
    "aiBubbleBg": "#fdfbfc",
    "aiBubbleText": "#2b1a21",
    "aiBubbleBorder": "#d6c1cb",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fdfbfc",
    "inputText": "#2b1a21",
    "inputBorder": "#bda3ae",
    "accent": "#b62230",
    "accentText": "#ffffff",
    "border": "#d6c1cb",
    "chipBg": "#f4e1e6",
    "chipText": "#8c1d29",
    "chipBorder": "#bda3ae",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#211318",
    "bgText": "#f5e8ec",
    "sidebarBg": "#2d1c22",
    "sidebarText": "#dbc0c8",
    "sidebarHover": "#3f2831",
    "sidebarSelected": "#553641",
    "sidebarHeader": "#9e8089",
    "editorBg": "#211318",
    "tabsBg": "#26161c",
    "tabBg": "#2d1c22",
    "tabText": "#a98b95",
    "tabActiveBg": "#3f2831",
    "tabActiveText": "#f5e8ec",
    "aiBg": "#2d1c22",
    "aiText": "#f5e8ec",
    "aiTabText": "#a98b95",
    "userBubbleBg": "#6b2631",
    "userBubbleText": "#fceef1",
    "aiBubbleBg": "#332027",
    "aiBubbleText": "#f5e8ec",
    "aiBubbleBorder": "#563743",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#ecd9a0",
    "inputBg": "#2a1a20",
    "inputText": "#f5e8ec",
    "inputBorder": "#563743",
    "accent": "#d94250",
    "accentText": "#1c0c0f",
    "border": "#563743",
    "chipBg": "#442a33",
    "chipText": "#f2dbe0",
    "chipBorder": "#8a5f68",
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
