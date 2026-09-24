# -*- coding: utf-8 -*-
"""
原神CP9 · 神里绫华×宵宫 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp9.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp9 deepking)会把本调色板写成 genshen-cp9.skin.json,
并生成可视化预览 genshen-cp9-preview.html, 方便导入前先看效果。
"""
from ..characters import cp9_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fdf8fa",
    "bgText": "#2a2138",
    "sidebarBg": "#f3eef8",
    "sidebarText": "#33293f",
    "sidebarHover": "#f7e6ea",
    "sidebarSelected": "#eed2da",
    "sidebarHeader": "#877996",
    "editorBg": "#fdf8fa",
    "tabsBg": "#faf4f8",
    "tabBg": "#f2e9f2",
    "tabText": "#66587a",
    "tabActiveBg": "#fdf8fa",
    "tabActiveText": "#2a2138",
    "aiBg": "#fbf5f9",
    "aiText": "#2a2138",
    "aiTabText": "#66587a",
    "userBubbleBg": "#f5d9dd",
    "userBubbleText": "#2a2138",
    "aiBubbleBg": "#fdf8fa",
    "aiBubbleText": "#2a2138",
    "aiBubbleBorder": "#dbc8da",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fdf8fa",
    "inputText": "#2a2138",
    "inputBorder": "#c9aac4",
    "accent": "#e8734a",
    "accentText": "#ffffff",
    "border": "#dbc8da",
    "chipBg": "#f4dfe4",
    "chipText": "#9c4222",
    "chipBorder": "#c9aac4",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#1a1626",
    "bgText": "#ece8f4",
    "sidebarBg": "#251f36",
    "sidebarText": "#cdc4de",
    "sidebarHover": "#322a47",
    "sidebarSelected": "#423858",
    "sidebarHeader": "#8b81a1",
    "editorBg": "#1a1626",
    "tabsBg": "#1f1a2d",
    "tabBg": "#251f36",
    "tabText": "#968cac",
    "tabActiveBg": "#322a47",
    "tabActiveText": "#ece8f4",
    "aiBg": "#251f36",
    "aiText": "#ece8f4",
    "aiTabText": "#968cac",
    "userBubbleBg": "#5e3350",
    "userBubbleText": "#f6eef3",
    "aiBubbleBg": "#2a2440",
    "aiBubbleText": "#ece8f4",
    "aiBubbleBorder": "#463b5e",
    "systemBubbleBg": "#3a2f14",
    "systemBubbleText": "#ecd39a",
    "inputBg": "#282138",
    "inputText": "#ece8f4",
    "inputBorder": "#463b5e",
    "accent": "#f58b5e",
    "accentText": "#1a0f0a",
    "border": "#463b5e",
    "chipBg": "#3b2f52",
    "chipText": "#e6d6ea",
    "chipBorder": "#6f5a86",
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
