# -*- coding: utf-8 -*-
"""
原神CP11 · 胡桃×香菱 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp11.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp11 deepking)会把本调色板写成 genshen-cp11.skin.json,
并生成可视化预览 genshen-cp11-preview.html, 方便导入前先看效果。
"""
from ..characters import cp11_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fffaf5",
    "bgText": "#2b1a16",
    "sidebarBg": "#f9ece1",
    "sidebarText": "#35211a",
    "sidebarHover": "#f7e0d4",
    "sidebarSelected": "#eec8b4",
    "sidebarHeader": "#8d6f64",
    "editorBg": "#fffaf5",
    "tabsBg": "#fdf3ea",
    "tabBg": "#f7e7da",
    "tabText": "#6b4d42",
    "tabActiveBg": "#fffaf5",
    "tabActiveText": "#2b1a16",
    "aiBg": "#fdf5ee",
    "aiText": "#2b1a16",
    "aiTabText": "#6b4d42",
    "userBubbleBg": "#f2d2c0",
    "userBubbleText": "#2b1a16",
    "aiBubbleBg": "#fffaf5",
    "aiBubbleText": "#2b1a16",
    "aiBubbleBorder": "#dfc2ad",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fffaf5",
    "inputText": "#2b1a16",
    "inputBorder": "#c9a288",
    "accent": "#b8352f",
    "accentText": "#ffffff",
    "border": "#dfc2ad",
    "chipBg": "#f4ddce",
    "chipText": "#8a2620",
    "chipBorder": "#c9a288",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#1e1512",
    "bgText": "#f2e8e0",
    "sidebarBg": "#2a1e19",
    "sidebarText": "#d3bcae",
    "sidebarHover": "#3a2921",
    "sidebarSelected": "#4d372c",
    "sidebarHeader": "#9a7f72",
    "editorBg": "#1e1512",
    "tabsBg": "#241a16",
    "tabBg": "#2a1e19",
    "tabText": "#a68c7e",
    "tabActiveBg": "#3a2921",
    "tabActiveText": "#f2e8e0",
    "aiBg": "#2a1e19",
    "aiText": "#f2e8e0",
    "aiTabText": "#a68c7e",
    "userBubbleBg": "#5e2620",
    "userBubbleText": "#f8eeea",
    "aiBubbleBg": "#33241d",
    "aiBubbleText": "#f2e8e0",
    "aiBubbleBorder": "#523a2e",
    "systemBubbleBg": "#3a2f14",
    "systemBubbleText": "#ecd39a",
    "inputBg": "#2e211b",
    "inputText": "#f2e8e0",
    "inputBorder": "#523a2e",
    "accent": "#e05a4a",
    "accentText": "#180c09",
    "border": "#523a2e",
    "chipBg": "#452f26",
    "chipText": "#f0d8c8",
    "chipBorder": "#7d5644",
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
