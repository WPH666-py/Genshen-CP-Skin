# -*- coding: utf-8 -*-
"""
原神CP7 · 娜维娅×克洛琳德 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp7.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp7 deepking)会把本调色板写成 genshen-cp7.skin.json,
并生成可视化预览 genshen-cp7-preview.html, 方便导入前先看效果。
"""
from ..characters import cp7_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fffaf7",
    "bgText": "#1e2436",
    "sidebarBg": "#eef3fa",
    "sidebarText": "#26304a",
    "sidebarHover": "#e2ebf6",
    "sidebarSelected": "#cddbef",
    "sidebarHeader": "#7d879e",
    "editorBg": "#fffaf7",
    "tabsBg": "#f6f9fd",
    "tabBg": "#ebf1f9",
    "tabText": "#5a6480",
    "tabActiveBg": "#fffaf7",
    "tabActiveText": "#1e2436",
    "aiBg": "#f8fbfe",
    "aiText": "#1e2436",
    "aiTabText": "#5a6480",
    "userBubbleBg": "#f0e2cd",
    "userBubbleText": "#1e2436",
    "aiBubbleBg": "#fffaf7",
    "aiBubbleText": "#1e2436",
    "aiBubbleBorder": "#dccdb4",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fffaf7",
    "inputText": "#1e2436",
    "inputBorder": "#c9b08a",
    "accent": "#b8863f",
    "accentText": "#ffffff",
    "border": "#dccdb4",
    "chipBg": "#f2e7d5",
    "chipText": "#7a5a24",
    "chipBorder": "#c9b08a",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#16182a",
    "bgText": "#e8e9f3",
    "sidebarBg": "#1f2338",
    "sidebarText": "#c6cadd",
    "sidebarHover": "#2b3049",
    "sidebarSelected": "#3a4060",
    "sidebarHeader": "#8288a1",
    "editorBg": "#16182a",
    "tabsBg": "#1a1d31",
    "tabBg": "#1f2338",
    "tabText": "#8f95ad",
    "tabActiveBg": "#2b3049",
    "tabActiveText": "#e8e9f3",
    "aiBg": "#1f2338",
    "aiText": "#e8e9f3",
    "aiTabText": "#8f95ad",
    "userBubbleBg": "#3d3562",
    "userBubbleText": "#f0eef7",
    "aiBubbleBg": "#23283f",
    "aiBubbleText": "#e8e9f3",
    "aiBubbleBorder": "#3d4460",
    "systemBubbleBg": "#3a2f14",
    "systemBubbleText": "#ecd39a",
    "inputBg": "#21253b",
    "inputText": "#e8e9f3",
    "inputBorder": "#3d4460",
    "accent": "#d9a95c",
    "accentText": "#171307",
    "border": "#3d4460",
    "chipBg": "#342a45",
    "chipText": "#ecd9c0",
    "chipBorder": "#6b5a86",
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
