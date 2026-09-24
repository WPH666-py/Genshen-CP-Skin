# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 9 —— 神里绫华 × 宵宫 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**两张素材**(稻妻双人: 湖畔樱吹雪、社殿石阶), 每张三种摆法:

    single1..2   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..2    满屏    cover 铺满整屏, 无边框
    showall1..2  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1~CP8 的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 九个套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp9"        # PyPI 分发包名
APP_SLUG = "genshen-cp9"                 # 命令前缀 / 运行时目录名
APP_NAME = "原神CP9"
DISPLAY_NAME = "原神 CP 壁纸套件 9 · 神里绫华 × 宵宫"
REPO_NAME = "Genshen-skin-CP9"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP9"

# 与其它套件并列展示用
SERIES = "CP9"
PAIR = "神里绫华 × 宵宫"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 两张稻妻双人插画, 都是横图。
IMAGE_FILES = ["01-lake.jpg", "02-stairs.jpg"]
IMAGE_NAMES = ["湖畔", "石阶"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-lake.jpg": {
        "title": "湖畔",
        "desc": "樱吹雪的湖畔: 宵宫回头笑着牵住绫华的手, 背景是水面、樱枝与远处的社殿屋顶",
        # 2448x1530 横图(1.600), 与 16:9 接近, 居中即可
        "pet_crop": (0.52, 0.52, 0.38),
        "cover_bias": (0.50, 0.52),
    },
    "02-stairs.jpg": {
        "title": "石阶",
        "desc": "社殿石阶上的双人合影: 宵宫着橙红短装, 绫华着青蓝和服, 金色纸鹤与樱瓣环绕",
        # 1920x1080 正好 16:9(1.778), 满屏时零裁切
        "pet_crop": (0.50, 0.48, 0.40),
        "cover_bias": (0.50, 0.50),
    },
}


# ---------------------------------------------------------------- 布局
# 两张素材 × 三种摆法。MODES 由上面的清单自动推导, 不用手写。
def _build_modes():
    """按 IMAGE_NAMES 自动生成 卡片/满屏/完整 三组模式。"""
    out = []
    for suffix, label in (("single", "卡片"), ("cover", "满屏"), ("showall", "完整")):
        for i, name in enumerate(IMAGE_NAMES):
            out.append(("%s%d" % (suffix, i + 1), "%s · %s" % (name, label)))
    return out


MODES = _build_modes()
DEFAULT_MODE = "single1"

# ---------------------------------------------------------------- DeepKing 皮肤
DEEPKING_SKIN_ID = "genshen-cp9-ayaka-yoimiya"
DEEPKING_SKIN_NAME = "原神CP9 · 神里绫华×宵宫"
DEEPKING_SKIN_DESC = (
    "稻妻双人主题: 主色取自插画采样 —— 宵宫的橙金与绫华的青蓝墨色, "
    "搭配满屏的樱粉与紫藤淡紫。亮色为樱纸暖白, 夜景为深藤紫。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp9-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp9-dark.jpg"
