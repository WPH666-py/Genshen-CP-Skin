# -*- coding: utf-8 -*-
"""
原神CP17 · 奥黛塔×沃雅妮莎×米提亚×阿罗夏 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp17.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp17 deepking)会把本调色板写成 genshen-cp17.skin.json,
并生成可视化预览 genshen-cp17-preview.html, 方便导入前先看效果。
"""
from ..characters import cp17_quartet as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fbfbfd",
    "bgText": "#1e2338",
    "sidebarBg": "#eceef5",
    "sidebarText": "#262b44",
    "sidebarHover": "#e2e6f2",
    "sidebarSelected": "#ccd4e8",
    "sidebarHeader": "#7b83a3",
    "editorBg": "#fbfbfd",
    "tabsBg": "#f5f6fa",
    "tabBg": "#e9ecf4",
    "tabText": "#545c7d",
    "tabActiveBg": "#fbfbfd",
    "tabActiveText": "#1e2338",
    "aiBg": "#f8f9fc",
    "aiText": "#1e2338",
    "aiTabText": "#545c7d",
    "userBubbleBg": "#d6dcee",
    "userBubbleText": "#1e2338",
    "aiBubbleBg": "#fbfbfd",
    "aiBubbleText": "#1e2338",
    "aiBubbleBorder": "#c6cde2",
    "systemBubbleBg": "#fff6dd",
    "systemBubbleText": "#8a6200",
    "inputBg": "#fbfbfd",
    "inputText": "#1e2338",
    "inputBorder": "#a9b3d0",
    "accent": "#6b79ad",
    "accentText": "#ffffff",
    "border": "#c6cde2",
    "chipBg": "#e3e7f2",
    "chipText": "#3d4a7a",
    "chipBorder": "#a9b3d0",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#171a2a",
    "bgText": "#e8ebf5",
    "sidebarBg": "#20253a",
    "sidebarText": "#c2c9dd",
    "sidebarHover": "#2c3350",
    "sidebarSelected": "#3b4468",
    "sidebarHeader": "#828aa8",
    "editorBg": "#171a2a",
    "tabsBg": "#1b1f30",
    "tabBg": "#20253a",
    "tabText": "#8b93ae",
    "tabActiveBg": "#2c3350",
    "tabActiveText": "#e8ebf5",
    "aiBg": "#20253a",
    "aiText": "#e8ebf5",
    "aiTabText": "#8b93ae",
    "userBubbleBg": "#35406b",
    "userBubbleText": "#eef1f8",
    "aiBubbleBg": "#242a42",
    "aiBubbleText": "#e8ebf5",
    "aiBubbleBorder": "#3e4767",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#ecd9a0",
    "inputBg": "#222840",
    "inputText": "#e8ebf5",
    "inputBorder": "#3e4767",
    "accent": "#8f9dd0",
    "accentText": "#0f1220",
    "border": "#3e4767",
    "chipBg": "#2e3552",
    "chipText": "#d6ddf0",
    "chipBorder": "#5d689a",
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
