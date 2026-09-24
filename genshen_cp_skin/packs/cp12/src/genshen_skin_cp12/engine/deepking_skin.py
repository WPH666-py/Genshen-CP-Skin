# -*- coding: utf-8 -*-
"""
原神CP12 · 行秋×重云 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp12.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp12 deepking)会把本调色板写成 genshen-cp12.skin.json,
并生成可视化预览 genshen-cp12-preview.html, 方便导入前先看效果。
"""
from ..characters import cp12_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#f8fbfe",
    "bgText": "#16233a",
    "sidebarBg": "#e9f2fa",
    "sidebarText": "#1d2c46",
    "sidebarHover": "#dcebf7",
    "sidebarSelected": "#c3dcef",
    "sidebarHeader": "#748aa8",
    "editorBg": "#f8fbfe",
    "tabsBg": "#f2f8fc",
    "tabBg": "#e4eef8",
    "tabText": "#4b6280",
    "tabActiveBg": "#f8fbfe",
    "tabActiveText": "#16233a",
    "aiBg": "#f5fafd",
    "aiText": "#16233a",
    "aiTabText": "#4b6280",
    "userBubbleBg": "#cfe2f3",
    "userBubbleText": "#16233a",
    "aiBubbleBg": "#f8fbfe",
    "aiBubbleText": "#16233a",
    "aiBubbleBorder": "#bcd4e8",
    "systemBubbleBg": "#fff6dd",
    "systemBubbleText": "#8a6200",
    "inputBg": "#f8fbfe",
    "inputText": "#16233a",
    "inputBorder": "#9dbfdb",
    "accent": "#2f6bab",
    "accentText": "#ffffff",
    "border": "#bcd4e8",
    "chipBg": "#dbeaf6",
    "chipText": "#1f4d80",
    "chipBorder": "#9dbfdb",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#131a2b",
    "bgText": "#e6ecf7",
    "sidebarBg": "#1c2540",
    "sidebarText": "#c2d0e2",
    "sidebarHover": "#263352",
    "sidebarSelected": "#33446a",
    "sidebarHeader": "#7b8ea8",
    "editorBg": "#131a2b",
    "tabsBg": "#171f33",
    "tabBg": "#1c2540",
    "tabText": "#8698b2",
    "tabActiveBg": "#263352",
    "tabActiveText": "#e6ecf7",
    "aiBg": "#1c2540",
    "aiText": "#e6ecf7",
    "aiTabText": "#8698b2",
    "userBubbleBg": "#2d4a72",
    "userBubbleText": "#eef4fb",
    "aiBubbleBg": "#202a47",
    "aiBubbleText": "#e6ecf7",
    "aiBubbleBorder": "#36486b",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#ecd9a0",
    "inputBg": "#1e2740",
    "inputText": "#e6ecf7",
    "inputBorder": "#36486b",
    "accent": "#5b9ad8",
    "accentText": "#0a1220",
    "border": "#36486b",
    "chipBg": "#2a3859",
    "chipText": "#cfe0f2",
    "chipBorder": "#55719c",
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
