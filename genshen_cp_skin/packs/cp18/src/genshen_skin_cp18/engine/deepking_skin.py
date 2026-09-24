# -*- coding: utf-8 -*-
"""
原神CP18 · 散兵×万叶 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp18.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp18 deepking)会把本调色板写成 genshen-cp18.skin.json,
并生成可视化预览 genshen-cp18-preview.html, 方便导入前先看效果。
"""
from ..characters import cp18_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fbfafc",
    "bgText": "#1e1c33",
    "sidebarBg": "#eeeef4",
    "sidebarText": "#26243f",
    "sidebarHover": "#e3e2f0",
    "sidebarSelected": "#cdcbe4",
    "sidebarHeader": "#78769a",
    "editorBg": "#fbfafc",
    "tabsBg": "#f5f5f9",
    "tabBg": "#eae9f2",
    "tabText": "#514f72",
    "tabActiveBg": "#fbfafc",
    "tabActiveText": "#1e1c33",
    "aiBg": "#f8f7fb",
    "aiText": "#1e1c33",
    "aiTabText": "#514f72",
    "userBubbleBg": "#d8d6ea",
    "userBubbleText": "#1e1c33",
    "aiBubbleBg": "#fbfafc",
    "aiBubbleText": "#1e1c33",
    "aiBubbleBorder": "#c7c5dd",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fbfafc",
    "inputText": "#1e1c33",
    "inputBorder": "#aaa7ca",
    "accent": "#3d3a6b",
    "accentText": "#ffffff",
    "border": "#c7c5dd",
    "chipBg": "#e4e3f1",
    "chipText": "#3b3968",
    "chipBorder": "#aaa7ca",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#15142a",
    "bgText": "#e7e6f3",
    "sidebarBg": "#1e1d3a",
    "sidebarText": "#c1bfd8",
    "sidebarHover": "#2a2950",
    "sidebarSelected": "#3a3868",
    "sidebarHeader": "#817fa2",
    "editorBg": "#15142a",
    "tabsBg": "#191832",
    "tabBg": "#1e1d3a",
    "tabText": "#8a88ab",
    "tabActiveBg": "#2a2950",
    "tabActiveText": "#e7e6f3",
    "aiBg": "#1e1d3a",
    "aiText": "#e7e6f3",
    "aiTabText": "#8a88ab",
    "userBubbleBg": "#3a3670",
    "userBubbleText": "#efeef7",
    "aiBubbleBg": "#232244",
    "aiBubbleText": "#e7e6f3",
    "aiBubbleBorder": "#3e3d68",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#ecd9a0",
    "inputBg": "#211f40",
    "inputText": "#e7e6f3",
    "inputBorder": "#3e3d68",
    "accent": "#6d6ab0",
    "accentText": "#100f22",
    "border": "#3e3d68",
    "chipBg": "#2e2c56",
    "chipText": "#d7d5ec",
    "chipBorder": "#5f5c9c",
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
