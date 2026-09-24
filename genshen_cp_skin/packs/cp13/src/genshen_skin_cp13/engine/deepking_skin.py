# -*- coding: utf-8 -*-
"""
原神CP13 · 钟离×凝光 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp13.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp13 deepking)会把本调色板写成 genshen-cp13.skin.json,
并生成可视化预览 genshen-cp13-preview.html, 方便导入前先看效果。
"""
from ..characters import cp13_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fdf9f0",
    "bgText": "#2b1f16",
    "sidebarBg": "#f6ecdd",
    "sidebarText": "#35271a",
    "sidebarHover": "#f4e6cf",
    "sidebarSelected": "#e8d2ad",
    "sidebarHeader": "#8d7458",
    "editorBg": "#fdf9f0",
    "tabsBg": "#fbf3e6",
    "tabBg": "#f4e9d6",
    "tabText": "#6b543c",
    "tabActiveBg": "#fdf9f0",
    "tabActiveText": "#2b1f16",
    "aiBg": "#fcf6ea",
    "aiText": "#2b1f16",
    "aiTabText": "#6b543c",
    "userBubbleBg": "#efdcbb",
    "userBubbleText": "#2b1f16",
    "aiBubbleBg": "#fdf9f0",
    "aiBubbleText": "#2b1f16",
    "aiBubbleBorder": "#d8c3a2",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fdf9f0",
    "inputText": "#2b1f16",
    "inputBorder": "#c2a97e",
    "accent": "#c9a43f",
    "accentText": "#231a08",
    "border": "#d8c3a2",
    "chipBg": "#f2e4c9",
    "chipText": "#7d621c",
    "chipBorder": "#c2a97e",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#1c1510",
    "bgText": "#f2e9dd",
    "sidebarBg": "#281e16",
    "sidebarText": "#d3c0aa",
    "sidebarHover": "#382a1e",
    "sidebarSelected": "#4a3828",
    "sidebarHeader": "#9a8064",
    "editorBg": "#1c1510",
    "tabsBg": "#211913",
    "tabBg": "#281e16",
    "tabText": "#a68d72",
    "tabActiveBg": "#382a1e",
    "tabActiveText": "#f2e9dd",
    "aiBg": "#281e16",
    "aiText": "#f2e9dd",
    "aiTabText": "#a68d72",
    "userBubbleBg": "#5c451f",
    "userBubbleText": "#f8f1e4",
    "aiBubbleBg": "#302419",
    "aiBubbleText": "#f2e9dd",
    "aiBubbleBorder": "#4f3d2b",
    "systemBubbleBg": "#3a2f14",
    "systemBubbleText": "#ecd39a",
    "inputBg": "#2c2117",
    "inputText": "#f2e9dd",
    "inputBorder": "#4f3d2b",
    "accent": "#e0bd5a",
    "accentText": "#1a1206",
    "border": "#4f3d2b",
    "chipBg": "#42311f",
    "chipText": "#eddcbb",
    "chipBorder": "#77603c",
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
