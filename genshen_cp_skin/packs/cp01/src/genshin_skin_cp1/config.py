# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 1 —— 全局标识与素材清单

改这里就能把本引擎复用成任意一套「单张样式」壁纸包:
只有 IMAGE_FILES / IMAGE_NAMES / GRID_* 需要换, 其余脚本无需改动。

与 WPH666-py 的其它套件 (AI-Family-Skin-Suit* / Deepseek-Skin-Suit*)
命名空间完全隔离: 包名、命令前缀、运行时目录 (~/.genshin-cp1) 均不冲突,
可同时安装、各自切换。
"""
import os

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshin-skin-cp1"      # PyPI 分发包名
APP_SLUG = "genshin-cp1"               # 命令前缀 / 运行时目录名
APP_NAME = "原神CP1"
DISPLAY_NAME = "原神 CP 壁纸套件 1 · 米提亚 × 沃雅妮莎"
REPO_NAME = "Genshen-Skin-CP1"
REPO_URL = "https://github.com/WPH666-py/Genshen-Skin-CP1"

# ---------------------------------------------------------------- 目录
APP_DIR = os.path.join(os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = os.path.join(APP_DIR, "cache")

# 素材目录: 由 skin_core 解析(wheel 内包数据 或 git 仓库 assets/)
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
IMAGE_FILES = ["01-heart.jpg", "02-dance.jpg", "03-sorry.jpg"]
IMAGE_NAMES = ["比心", "共舞", "道歉"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
IMAGE_META = {
    "01-heart.jpg": {
        "title": "比心",
        "desc": "青绿长发少女与银白发少年双手相合成心, 蓝色波点背景",
        "pet_crop": (0.50, 0.50, 0.46),
    },
    "02-dance.jpg": {
        "title": "共舞",
        "desc": "夜色蓝调中执手共舞, 音符与星光环绕",
        "pet_crop": (0.50, 0.48, 0.46),
    },
    "03-sorry.jpg": {
        "title": "道歉",
        "desc": "白旗投降式道歉, 少女抱臂气鼓鼓",
        "pet_crop": (0.50, 0.52, 0.46),
    },
}

# ---------------------------------------------------------------- 布局
# 本套件 = 「单张样式」: 每张素材各自成为一张整屏壁纸。
#   single* = 模糊填充背景 + 居中圆角卡片(竖图不裁切, 构图完整)
#   cover*  = 按 cover 裁切铺满整屏(满屏无边框, 适合横图, 竖图会裁掉上下)
MODES = [
    ("single1", IMAGE_NAMES[0]),
    ("single2", IMAGE_NAMES[1]),
    ("single3", IMAGE_NAMES[2]),
    ("cover1", IMAGE_NAMES[0] + " (满屏)"),
    ("cover2", IMAGE_NAMES[1] + " (满屏)"),
    ("cover3", IMAGE_NAMES[2] + " (满屏)"),
]
DEFAULT_MODE = "single1"
# ---------------------------------------------------------------- DeepKing 皮肤
# 供引擎的 DeepKing 适配层读取(与 characters/ 形态的 CP2 保持同名常量)
DEEPKING_SKIN_ID = "genshin-cp1-mitiya-voyanisa"
DEEPKING_SKIN_NAME = "原神CP1 · 米提亚×沃雅妮莎"
DEEPKING_SKIN_DESC = (
    "米提亚与沃雅妮莎的蓝调同人主题: 日景青蓝取自「比心」, "
    "夜景蓝紫取自「共舞」。32 槽位逐项校色, 亮/暗双套。"
)
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp1-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp1-dark.jpg"

# 与并列套件对照用
SERIES = "CP1"
PAIR = "米提亚 × 沃雅妮莎"
