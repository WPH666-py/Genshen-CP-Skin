# -*- coding: utf-8 -*-
"""
原神CP19 · 空×荧 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp19.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp19 deepking)会把本调色板写成 genshen-cp19.skin.json,
并生成可视化预览 genshen-cp19-preview.html, 方便导入前先看效果。
"""
from ..characters import cp19_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fdfaf5",
    "bgText": "#262232",
    "sidebarBg": "#f3f0e9",
    "sidebarText": "#2d2839",
    "sidebarHover": "#f4ead6",
    "sidebarSelected": "#e9dab8",
    "sidebarHeader": "#837d90",
    "editorBg": "#fdfaf5",
    "tabsBg": "#faf7f1",
    "tabBg": "#f1ece2",
    "tabText": "#565064",
    "tabActiveBg": "#fdfaf5",
    "tabActiveText": "#262232",
    "aiBg": "#fcf8f1",
    "aiText": "#262232",
    "aiTabText": "#565064",
    "userBubbleBg": "#ece0c6",
    "userBubbleText": "#262232",
    "aiBubbleBg": "#fdfaf5",
    "aiBubbleText": "#262232",
    "aiBubbleBorder": "#d8cdb5",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fdfaf5",
    "inputText": "#262232",
    "inputBorder": "#b9ab8c",
    "accent": "#c9a44a",
    "accentText": "#231c08",
    "border": "#d8cdb5",
    "chipBg": "#f0e7d3",
    "chipText": "#7a601c",
    "chipBorder": "#b9ab8c",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#121a30",
    "bgText": "#e8ecf6",
    "sidebarBg": "#1a2540",
    "sidebarText": "#c2cbe0",
    "sidebarHover": "#253253",
    "sidebarSelected": "#33426b",
    "sidebarHeader": "#808ba6",
    "editorBg": "#121a30",
    "tabsBg": "#161f38",
    "tabBg": "#1a2540",
    "tabText": "#8a94af",
    "tabActiveBg": "#253253",
    "tabActiveText": "#e8ecf6",
    "aiBg": "#1a2540",
    "aiText": "#e8ecf6",
    "aiTabText": "#8a94af",
    "userBubbleBg": "#3c3a2e",
    "userBubbleText": "#f5f0e2",
    "aiBubbleBg": "#1f2a47",
    "aiBubbleText": "#e8ecf6",
    "aiBubbleBorder": "#384569",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#ecd9a0",
    "inputBg": "#1d2742",
    "inputText": "#e8ecf6",
    "inputBorder": "#384569",
    "accent": "#e0c069",
    "accentText": "#191406",
    "border": "#384569",
    "chipBg": "#2c3550",
    "chipText": "#e2dcc6",
    "chipBorder": "#6b6a7d",
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
