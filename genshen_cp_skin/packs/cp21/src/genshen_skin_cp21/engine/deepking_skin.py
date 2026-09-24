# -*- coding: utf-8 -*-
"""
原神CP21 · 魈×荧 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp21.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的深靛墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp21 deepking)会把本调色板写成 genshen-cp21.skin.json,
并生成可视化预览 genshen-cp21-preview.html, 方便导入前先看效果。
"""
from ..characters import cp21_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 暖阳米白(夕照亮部)
LIGHT = {
    "bg": "#fdfaf1",
    "bgText": "#212a24",
    "sidebarBg": "#f3ede0",
    "sidebarText": "#28322b",
    "sidebarHover": "#dfeae6",
    "sidebarSelected": "#c4d9d3",
    "sidebarHeader": "#7b8a7e",
    "editorBg": "#fdfaf1",
    "tabsBg": "#faf6ec",
    "tabBg": "#f1ebdd",
    "tabText": "#536054",
    "tabActiveBg": "#fdfaf1",
    "tabActiveText": "#212a24",
    "aiBg": "#fcf9f1",
    "aiText": "#212a24",
    "aiTabText": "#536054",
    "userBubbleBg": "#d8e5df",
    "userBubbleText": "#212a24",
    "aiBubbleBg": "#fdfaf1",
    "aiBubbleText": "#212a24",
    "aiBubbleBorder": "#c9cdb8",
    "systemBubbleBg": "#fff4dd",
    "systemBubbleText": "#8a5a00",
    "inputBg": "#fdfaf1",
    "inputText": "#212a24",
    "inputBorder": "#a9b5a0",
    "accent": "#3f7d78",
    "accentText": "#ffffff",
    "border": "#c9cdb8",
    "chipBg": "#e3e9dc",
    "chipText": "#2f5a56",
    "chipBorder": "#a9b5a0",
}

# ─────────────────────────────────────────────── 夜景 · 深靛墨黑(夜海)
DARK = {
    "bg": "#131d1a",
    "bgText": "#e6efe9",
    "sidebarBg": "#1c2925",
    "sidebarText": "#c0cfc6",
    "sidebarHover": "#283933",
    "sidebarSelected": "#374d45",
    "sidebarHeader": "#7e9086",
    "editorBg": "#131d1a",
    "tabsBg": "#17221f",
    "tabBg": "#1c2925",
    "tabText": "#87998f",
    "tabActiveBg": "#283933",
    "tabActiveText": "#e6efe9",
    "aiBg": "#1c2925",
    "aiText": "#e6efe9",
    "aiTabText": "#87998f",
    "userBubbleBg": "#2c534c",
    "userBubbleText": "#eef5f1",
    "aiBubbleBg": "#22302b",
    "aiBubbleText": "#e6efe9",
    "aiBubbleBorder": "#3b524a",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#ecd9a0",
    "inputBg": "#1f2c27",
    "inputText": "#e6efe9",
    "inputBorder": "#3b524a",
    "accent": "#5fa8a0",
    "accentText": "#08110f",
    "border": "#3b524a",
    "chipBg": "#2b423b",
    "chipText": "#cfe3da",
    "chipBorder": "#5c7d72",
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
