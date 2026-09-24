# -*- coding: utf-8 -*-
"""
原神CP15 · 甘雨×刻晴 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp15.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp15 deepking)会把本调色板写成 genshen-cp15.skin.json,
并生成可视化预览 genshen-cp15-preview.html, 方便导入前先看效果。
"""
from ..characters import cp15_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fafbfd",
    "bgText": "#1f1b2e",
    "sidebarBg": "#eef1f8",
    "sidebarText": "#272139",
    "sidebarHover": "#e0eaf5",
    "sidebarSelected": "#c7dcee",
    "sidebarHeader": "#7d7794",
    "editorBg": "#fafbfd",
    "tabsBg": "#f4f6fb",
    "tabBg": "#e8edf6",
    "tabText": "#544d6c",
    "tabActiveBg": "#fafbfd",
    "tabActiveText": "#1f1b2e",
    "aiBg": "#f7f9fc",
    "aiText": "#1f1b2e",
    "aiTabText": "#544d6c",
    "userBubbleBg": "#d3e3f1",
    "userBubbleText": "#1f1b2e",
    "aiBubbleBg": "#fafbfd",
    "aiBubbleText": "#1f1b2e",
    "aiBubbleBorder": "#c2d3e5",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fafbfd",
    "inputText": "#1f1b2e",
    "inputBorder": "#a8bfd6",
    "accent": "#8fbde0",
    "accentText": "#12222f",
    "border": "#c2d3e5",
    "chipBg": "#dfe9f4",
    "chipText": "#2f5878",
    "chipBorder": "#a8bfd6",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#191426",
    "bgText": "#ebe7f2",
    "sidebarBg": "#231c33",
    "sidebarText": "#c6bed7",
    "sidebarHover": "#302745",
    "sidebarSelected": "#3f3459",
    "sidebarHeader": "#877f9e",
    "editorBg": "#191426",
    "tabsBg": "#1d1729",
    "tabBg": "#231c33",
    "tabText": "#918aa6",
    "tabActiveBg": "#302745",
    "tabActiveText": "#ebe7f2",
    "aiBg": "#231c33",
    "aiText": "#ebe7f2",
    "aiTabText": "#918aa6",
    "userBubbleBg": "#33506d",
    "userBubbleText": "#f0f5fa",
    "aiBubbleBg": "#271f38",
    "aiBubbleText": "#ebe7f2",
    "aiBubbleBorder": "#423757",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#ecd9a0",
    "inputBg": "#251e35",
    "inputText": "#ebe7f2",
    "inputBorder": "#423757",
    "accent": "#a9d0ec",
    "accentText": "#0d1a24",
    "border": "#423757",
    "chipBg": "#2f3350",
    "chipText": "#d5e4f2",
    "chipBorder": "#5e6a94",
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
