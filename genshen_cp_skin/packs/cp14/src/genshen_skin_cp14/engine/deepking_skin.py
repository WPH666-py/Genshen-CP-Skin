# -*- coding: utf-8 -*-
"""
原神CP14 · 神里绫华×优菈×甘雨 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp14.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp14 deepking)会把本调色板写成 genshen-cp14.skin.json,
并生成可视化预览 genshen-cp14-preview.html, 方便导入前先看效果。
"""
from ..characters import cp14_trio as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#f9fbfd",
    "bgText": "#1b2836",
    "sidebarBg": "#eaf1f8",
    "sidebarText": "#223140",
    "sidebarHover": "#dfeaf5",
    "sidebarSelected": "#c6dbeb",
    "sidebarHeader": "#78899c",
    "editorBg": "#f9fbfd",
    "tabsBg": "#f3f8fc",
    "tabBg": "#e6eff7",
    "tabText": "#506478",
    "tabActiveBg": "#f9fbfd",
    "tabActiveText": "#1b2836",
    "aiBg": "#f6fafd",
    "aiText": "#1b2836",
    "aiTabText": "#506478",
    "userBubbleBg": "#d3e3f2",
    "userBubbleText": "#1b2836",
    "aiBubbleBg": "#f9fbfd",
    "aiBubbleText": "#1b2836",
    "aiBubbleBorder": "#c2d5e6",
    "systemBubbleBg": "#fff6dd",
    "systemBubbleText": "#8a6200",
    "inputBg": "#f9fbfd",
    "inputText": "#1b2836",
    "inputBorder": "#a3bed6",
    "accent": "#7ba7cc",
    "accentText": "#10202e",
    "border": "#c2d5e6",
    "chipBg": "#deeaf6",
    "chipText": "#2c5478",
    "chipBorder": "#a3bed6",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#151d27",
    "bgText": "#e7eef6",
    "sidebarBg": "#1e2a37",
    "sidebarText": "#c4d3e1",
    "sidebarHover": "#2a3949",
    "sidebarSelected": "#384b60",
    "sidebarHeader": "#7e8fa2",
    "editorBg": "#151d27",
    "tabsBg": "#19222d",
    "tabBg": "#1e2a37",
    "tabText": "#8b9cad",
    "tabActiveBg": "#2a3949",
    "tabActiveText": "#e7eef6",
    "aiBg": "#1e2a37",
    "aiText": "#e7eef6",
    "aiTabText": "#8b9cad",
    "userBubbleBg": "#2f5477",
    "userBubbleText": "#eef5fb",
    "aiBubbleBg": "#232f3e",
    "aiBubbleText": "#e7eef6",
    "aiBubbleBorder": "#3c5064",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#ecd9a0",
    "inputBg": "#212c39",
    "inputText": "#e7eef6",
    "inputBorder": "#3c5064",
    "accent": "#9cc6e6",
    "accentText": "#0a141d",
    "border": "#3c5064",
    "chipBg": "#2c3e52",
    "chipText": "#d2e6f5",
    "chipBorder": "#5b7d9c",
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
