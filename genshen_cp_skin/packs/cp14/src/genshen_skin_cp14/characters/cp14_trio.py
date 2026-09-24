# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 14 —— 神里绫华 × 优菈 × 甘雨 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件只有**一张素材**(氷元素学科教室三人合影), 提供三种摆法:

    single1   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1    满屏    cover 铺满整屏, 无边框
    showall1  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1~CP13 的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 十四个套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp14"       # PyPI 分发包名
APP_SLUG = "genshen-cp14"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP14"
DISPLAY_NAME = "原神 CP 壁纸套件 14 · 神里绫华 × 优菈 × 甘雨"
REPO_NAME = "Genshen-skin-CP14"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP14"

# 与其它套件并列展示用
SERIES = "CP14"
PAIR = "神里绫华 × 优菈 × 甘雨"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 只有一张插画, 无水印/logo, 无需预裁。
IMAGE_FILES = ["01-classroom.jpg"]
IMAGE_NAMES = ["氷元素学科"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-classroom.jpg": {
        "title": "氷元素学科",
        "desc": "教室课桌前的三人合影: 左侧甘雨白紫发戴红丝带, 中间优菈冰蓝发, "
                "右侧神里绫华紫发比耶; 身后墨绿黑板上写着「氷元素学科」",
        # 1256x925 横图(1.3578)。满屏取景窗 1256x706 —— **横向用满整幅、零裁切**,
        # 纵向有 219px 余量。取景窗要**上移**才能同时保住黑板标题与三人的头顶:
        # 0.54 会切掉黑板与发顶, 0.30 刚好。
        "pet_crop": (0.50, 0.46, 0.40),
        "cover_bias": (0.50, 0.30),
    },
}


# ---------------------------------------------------------------- 布局
# 单张素材 × 三种摆法。MODES 由上面的清单自动推导, 不用手写。
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
DEEPKING_SKIN_ID = "genshen-cp14-ayaka-eula-ganyu"
DEEPKING_SKIN_NAME = "原神CP14 · 神里绫华×优菈×甘雨"
DEEPKING_SKIN_DESC = (
    "氷元素学科: 主色取自插画采样 —— 三位冰系角色的冰蓝发色与蓝灰格纹校服, "
    "搭配教室的墨绿黑板与木质课桌暖调。亮色为霜白晨光, 夜景为深蓝墨夜色。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp14-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp14-dark.jpg"
