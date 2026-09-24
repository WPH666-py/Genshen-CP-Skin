# -*- coding: utf-8 -*-
"""
原神CP10 · 雷电影×八重神子 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp10.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp10 deepking)会把本调色板写成 genshen-cp10.skin.json,
并生成可视化预览 genshen-cp10-preview.html, 方便导入前先看效果。
"""
from ..characters import cp10_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fdf9fb",
    "bgText": "#241a2c",
    "sidebarBg": "#f3edf7",
    "sidebarText": "#2e2237",
    "sidebarHover": "#f3e4ec",
    "sidebarSelected": "#e6d0e0",
    "sidebarHeader": "#816f90",
    "editorBg": "#fdf9fb",
    "tabsBg": "#faf5f9",
    "tabBg": "#f2eaf5",
    "tabText": "#5e4d6e",
    "tabActiveBg": "#fdf9fb",
    "tabActiveText": "#241a2c",
    "aiBg": "#fbf6fa",
    "aiText": "#241a2c",
    "aiTabText": "#5e4d6e",
    "userBubbleBg": "#f0d6e2",
    "userBubbleText": "#241a2c",
    "aiBubbleBg": "#fdf9fb",
    "aiBubbleText": "#241a2c",
    "aiBubbleBorder": "#d6c3e2",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fdf9fb",
    "inputText": "#241a2c",
    "inputBorder": "#b79cc9",
    "accent": "#8a5fb0",
    "accentText": "#ffffff",
    "border": "#d6c3e2",
    "chipBg": "#efdcea",
    "chipText": "#613a86",
    "chipBorder": "#b79cc9",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#1a1420",
    "bgText": "#eee8f2",
    "sidebarBg": "#251c2e",
    "sidebarText": "#cdc0d8",
    "sidebarHover": "#33263f",
    "sidebarSelected": "#433352",
    "sidebarHeader": "#90809e",
    "editorBg": "#1a1420",
    "tabsBg": "#1f1826",
    "tabBg": "#251c2e",
    "tabText": "#9a8ba8",
    "tabActiveBg": "#33263f",
    "tabActiveText": "#eee8f2",
    "aiBg": "#251c2e",
    "aiText": "#eee8f2",
    "aiTabText": "#9a8ba8",
    "userBubbleBg": "#5d3268",
    "userBubbleText": "#f5eef8",
    "aiBubbleBg": "#2a2036",
    "aiBubbleText": "#eee8f2",
    "aiBubbleBorder": "#473859",
    "systemBubbleBg": "#3a2f14",
    "systemBubbleText": "#ecd39a",
    "inputBg": "#281f33",
    "inputText": "#eee8f2",
    "inputBorder": "#473859",
    "accent": "#b184d4",
    "accentText": "#150e1a",
    "border": "#473859",
    "chipBg": "#3a2b4d",
    "chipText": "#e0cef0",
    "chipBorder": "#6d5590",
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
