# -*- coding: utf-8 -*-
"""
原神CP23 · 荧×诺艾尔 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp23.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp23 deepking)会把本调色板写成 genshen-cp23.skin.json,
并生成可视化预览 genshen-cp23-preview.html, 方便导入前先看效果。
"""
from ..characters import cp23_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fefbf7",
    "bgText": "#2e211c",
    "sidebarBg": "#f7efe6",
    "sidebarText": "#382823",
    "sidebarHover": "#f6e2dd",
    "sidebarSelected": "#ecc8c0",
    "sidebarHeader": "#8b736a",
    "editorBg": "#fefbf7",
    "tabsBg": "#fcf6ef",
    "tabBg": "#f5ebe0",
    "tabText": "#5e473f",
    "tabActiveBg": "#fefbf7",
    "tabActiveText": "#2e211c",
    "aiBg": "#fdf8f3",
    "aiText": "#2e211c",
    "aiTabText": "#5e473f",
    "userBubbleBg": "#f0d8d2",
    "userBubbleText": "#2e211c",
    "aiBubbleBg": "#fefbf7",
    "aiBubbleText": "#2e211c",
    "aiBubbleBorder": "#d8c1ae",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fefbf7",
    "inputText": "#2e211c",
    "inputBorder": "#bfa38d",
    "accent": "#b03a35",
    "accentText": "#ffffff",
    "border": "#d8c1ae",
    "chipBg": "#f3e4dd",
    "chipText": "#8a3830",
    "chipBorder": "#bfa38d",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#221619",
    "bgText": "#f3e8e6",
    "sidebarBg": "#2e1e22",
    "sidebarText": "#d6bfbb",
    "sidebarHover": "#3f2a2f",
    "sidebarSelected": "#54383f",
    "sidebarHeader": "#9b807c",
    "editorBg": "#221619",
    "tabsBg": "#27191d",
    "tabBg": "#2e1e22",
    "tabText": "#a58b87",
    "tabActiveBg": "#3f2a2f",
    "tabActiveText": "#f3e8e6",
    "aiBg": "#2e1e22",
    "aiText": "#f3e8e6",
    "aiTabText": "#a58b87",
    "userBubbleBg": "#63332f",
    "userBubbleText": "#fbeeec",
    "aiBubbleBg": "#342227",
    "aiBubbleText": "#f3e8e6",
    "aiBubbleBorder": "#553a40",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#ecd9a0",
    "inputBg": "#2b1c20",
    "inputText": "#f3e8e6",
    "inputBorder": "#553a40",
    "accent": "#d9584f",
    "accentText": "#1c0d0b",
    "border": "#553a40",
    "chipBg": "#45292e",
    "chipText": "#f0d9d4",
    "chipBorder": "#8a5f60",
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
