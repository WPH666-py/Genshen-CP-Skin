# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 4 —— 柯莱 × 安柏 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件是**单张样式**: 只有一张素材 `01-collei.jpg`(森林里的双人合影)。用户可在
三种观感之间切换:

    single1  默认    模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1   满屏    cover 铺满整屏, 无边框
    showall  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1 (Genshen-Skin-CP1, 米提亚 × 沃雅妮莎)、CP2 (Genshen-skin-CP2,
奥黛塔 × 沃雅妮莎)、CP3 (Genshen-skin-CP3, 三人群像) 的命名空间完全隔离:
包名 / 命令前缀 / 运行时目录 / vscode 扩展 ID / DeepKing 皮肤 id 均不冲突,
四个套件可以同时安装、各自切换。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp4"        # PyPI 分发包名
APP_SLUG = "genshen-cp4"                 # 命令前缀 / 运行时目录名
APP_NAME = "原神CP4"
DISPLAY_NAME = "原神 CP 壁纸套件 4 · 柯莱 × 安柏"
REPO_NAME = "Genshen-skin-CP4"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP4"

# 与其它套件并列展示用
SERIES = "CP4"
PAIR = "柯莱 × 安柏"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 本套件只有这一张。加图只需在此追加文件名 + 在 IMAGE_META 里补一条,
# 样式列表(MODES)会自动跟着变。
IMAGE_FILES = ["01-collei.jpg"]
IMAGE_NAMES = ["林间"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
IMAGE_META = {
    "01-collei.jpg": {
        "title": "林间",
        "desc": "森林里的双人合影: 绿发紫瞳的柯莱与红枣色长发的安柏相拥, "
                "脚下是草地与黄花, 前景有绿色小生物与红色兔兔伯爵",
        # 桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
        # 取两人的脸与上半身
        "pet_crop": (0.52, 0.34, 0.32),
        # 满屏模式的取景偏向: 素材 1600x2272(比例 0.704), 对 16:9 要裁掉较多高度。
        # 画面上部是两人的脸、下部是草地与黄花, 取景窗上移保住主要人物。
        "cover_bias": (0.52, 0.30),
    },
}

# ---------------------------------------------------------------- 布局
# 「单张样式」: 同一张素材的三种呈现方式, 用户随时切换。
#   single1  = 模糊填充背景 + 居中圆角卡片(默认; 构图完整)
#   cover1   = 按 cover 裁切铺满整屏(满屏无边框, 用 cover_bias 保住人物)
#   showall  = 等比缩放完整放进纯色底(一个像素都不裁, 两侧留同色边)
MODES = [
    ("single1", IMAGE_NAMES[0] + " · 卡片"),
    ("cover1", IMAGE_NAMES[0] + " · 满屏"),
    ("showall", IMAGE_NAMES[0] + " · 完整"),
]
DEFAULT_MODE = "single1"

# ---------------------------------------------------------------- DeepKing 皮肤
DEEPKING_SKIN_ID = "genshen-cp4-collei-amber"
DEEPKING_SKIN_NAME = "原神CP4 · 柯莱×安柏"
DEEPKING_SKIN_DESC = (
    "林间同人主题: 主色取自插画里柯莱的草绿发色与安柏的琥珀棕红, "
    "搭配林间暖阳黄。亮色为晨光米白, 夜景为深林墨绿。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp4-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp4-dark.jpg"
