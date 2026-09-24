# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 3 —— 米提亚 × 奥黛塔 × 沃雅妮莎 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件是**单张样式**: 只有一张素材 `01-trio.jpg`(多对 CP 的群像)。用户可在
三种观感之间切换:

    single1  默认    模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1   满屏    cover 铺满整屏, 无边框(取景窗下压避开右上角作者水印)
    showall  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1 (Genshen-Skin-CP1, 米提亚 × 沃雅妮莎) 和 CP2 (Genshen-skin-CP2,
奥黛塔 × 沃雅妮莎) 的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 三个套件可以同时安装、各自切换。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp3"        # PyPI 分发包名
APP_SLUG = "genshen-cp3"                 # 命令前缀 / 运行时目录名
APP_NAME = "原神CP3"
DISPLAY_NAME = "原神 CP 壁纸套件 3 · 米提亚 × 奥黛塔 × 沃雅妮莎"
REPO_NAME = "Genshen-skin-CP3"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP3"

# 与其它套件并列展示用
SERIES = "CP3"
PAIR = "米提亚 × 奥黛塔 × 沃雅妮莎"

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
IMAGE_FILES = ["01-trio.jpg"]
IMAGE_NAMES = ["群像"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
IMAGE_META = {
    "01-trio.jpg": {
        "title": "群像",
        "desc": "多对 CP 的合照: 米提亚与绿发少年的拥抱、米提亚与白发少年的公主抱、"
                "沃雅妮莎与奥黛塔的相依, 浅灰底群像",
        # 桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
        # 居中偏右取景, 拿到中间那对(米提亚 × 白发少年)
        "pet_crop": (0.56, 0.44, 0.32),
        # 满屏模式的取景偏向: 素材 1279x1646(比例 0.777), 对 16:9 只需裁掉少量
        # 高度。右上角有作者水印(NG / @PidePideko5965), 因此把取景窗略微下压并
        # 左移, 既保住全部人物, 也把水印挤出画面。
        "cover_bias": (0.47, 0.58),
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
DEEPKING_SKIN_ID = "genshen-cp3-mitiya-odette-voyanisa"
DEEPKING_SKIN_NAME = "原神CP3 · 米提亚×奥黛塔×沃雅妮莎"
DEEPKING_SKIN_DESC = (
    "群像插画主题: 主色取自画面里的青绿长发与钴蓝礼服, 搭配浅灰底与薰衣草紫。"
    "亮色为浅灰净白界面, 夜景为深青蓝。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp3-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp3-dark.jpg"
