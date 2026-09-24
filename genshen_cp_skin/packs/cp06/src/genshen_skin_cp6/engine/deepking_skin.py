# -*- coding: utf-8 -*-
"""
原神CP6 · 玛拉妮×基尼奇×卡其娜 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp6.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp6 deepking)会把本调色板写成 genshen-cp6.skin.json,
并生成可视化预览 genshen-cp6-preview.html, 方便导入前先看效果。
"""
from ..characters import cp6_trio as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fffcf6",
    "bgText": "#14263a",
    "sidebarBg": "#eaf3f7",
    "sidebarText": "#1c3348",
    "sidebarHover": "#ddeef5",
    "sidebarSelected": "#c4e1ec",
    "sidebarHeader": "#71879c",
    "editorBg": "#fffcf6",
    "tabsBg": "#f3f8fa",
    "tabBg": "#e6f1f6",
    "tabText": "#4c657c",
    "tabActiveBg": "#fffcf6",
    "tabActiveText": "#14263a",
    "aiBg": "#f6fbfc",
    "aiText": "#14263a",
    "aiTabText": "#4c657c",
    "userBubbleBg": "#c9e5f0",
    "userBubbleText": "#14263a",
    "aiBubbleBg": "#fffcf6",
    "aiBubbleText": "#14263a",
    "aiBubbleBorder": "#bcd8e4",
    "systemBubbleBg": "#fff3dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fffcf6",
    "inputText": "#14263a",
    "inputBorder": "#9fc9da",
    "accent": "#2e9ec4",
    "accentText": "#ffffff",
    "border": "#bcd8e4",
    "chipBg": "#d5ebf3",
    "chipText": "#1d6a86",
    "chipBorder": "#9fc9da",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#0d1a26",
    "bgText": "#e4eef5",
    "sidebarBg": "#142534",
    "sidebarText": "#c0d3e0",
    "sidebarHover": "#1d3446",
    "sidebarSelected": "#29485f",
    "sidebarHeader": "#7e94a4",
    "editorBg": "#0d1a26",
    "tabsBg": "#11202c",
    "tabBg": "#142534",
    "tabText": "#8aa0b1",
    "tabActiveBg": "#1d3446",
    "tabActiveText": "#e4eef5",
    "aiBg": "#142534",
    "aiText": "#e4eef5",
    "aiTabText": "#8aa0b1",
    "userBubbleBg": "#245e78",
    "userBubbleText": "#ecf5f9",
    "aiBubbleBg": "#182c3d",
    "aiBubbleText": "#e4eef5",
    "aiBubbleBorder": "#2e4d63",
    "systemBubbleBg": "#3a2c14",
    "systemBubbleText": "#e8cf9a",
    "inputBg": "#162735",
    "inputText": "#e4eef5",
    "inputBorder": "#2e4d63",
    "accent": "#56c1e0",
    "accentText": "#07141c",
    "border": "#2e4d63",
    "chipBg": "#20404f",
    "chipText": "#c6e6f0",
    "chipBorder": "#3d7a92",
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
