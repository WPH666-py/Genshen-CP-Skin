# -*- coding: utf-8 -*-
"""
原神CP5 · 桑多涅×哥伦比娅 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp4.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留插画的夜紫墨黑, 而不是派生算法给出的中性灰。

安装器(genshen-cp4 deepking)会把本调色板写成 genshen-cp4.skin.json,
并生成可视化预览 genshen-cp4-preview.html, 方便导入前先看效果。
"""
from ..characters import cp4_pair as C

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 晨光象牙(学园日光)
LIGHT = {
    "bg": "#fdfbf7",
    "bgText": "#241726",
    "sidebarBg": "#f4eef2",
    "sidebarText": "#33203a",
    "sidebarHover": "#f0e2ec",
    "sidebarSelected": "#e3cddd",
    "sidebarHeader": "#8d7691",
    "editorBg": "#fdfbf7",
    "tabsBg": "#f8f2f6",
    "tabBg": "#f1e7ee",
    "tabText": "#6b5570",
    "tabActiveBg": "#fdfbf7",
    "tabActiveText": "#241726",
    "aiBg": "#faf5f8",
    "aiText": "#241726",
    "aiTabText": "#6b5570",
    "userBubbleBg": "#eccfdf",
    "userBubbleText": "#241726",
    "aiBubbleBg": "#fdfbf7",
    "aiBubbleText": "#241726",
    "aiBubbleBorder": "#dbc6d8",
    "systemBubbleBg": "#fff6dd",
    "systemBubbleText": "#8a6200",
    "inputBg": "#fdfbf7",
    "inputText": "#241726",
    "inputBorder": "#c9a8c3",
    "accent": "#a8326e",
    "accentText": "#ffffff",
    "border": "#dbc6d8",
    "chipBg": "#eddae6",
    "chipText": "#7d2153",
    "chipBorder": "#c9a8c3",
}

# ─────────────────────────────────────────────── 夜景 · 夜紫墨黑(夜街紫光)
DARK = {
    "bg": "#17101c",
    "bgText": "#efe6f2",
    "sidebarBg": "#221728",
    "sidebarText": "#d0bcd6",
    "sidebarHover": "#2e1f36",
    "sidebarSelected": "#3d2a47",
    "sidebarHeader": "#907d98",
    "editorBg": "#17101c",
    "tabsBg": "#1c1422",
    "tabBg": "#221728",
    "tabText": "#9d8aa5",
    "tabActiveBg": "#2e1f36",
    "tabActiveText": "#efe6f2",
    "aiBg": "#221728",
    "aiText": "#efe6f2",
    "aiTabText": "#9d8aa5",
    "userBubbleBg": "#5c2350",
    "userBubbleText": "#f6ecf4",
    "aiBubbleBg": "#281a30",
    "aiBubbleText": "#efe6f2",
    "aiBubbleBorder": "#453050",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#e8d9a0",
    "inputBg": "#251a2c",
    "inputText": "#efe6f2",
    "inputBorder": "#453050",
    "accent": "#d1498c",
    "accentText": "#160f1b",
    "border": "#453050",
    "chipBg": "#3b2743",
    "chipText": "#e4cfe2",
    "chipBorder": "#6d4577",
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
    from ..engine import _color as col

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
