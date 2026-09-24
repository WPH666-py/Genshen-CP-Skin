# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 24 —— 甘雨 × 绫华 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件只有**一张素材**(甘雨与绫华的和服合影), 提供三种摆法:

    single1   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1    满屏    cover 铺满整屏, 无边框
    showall1  完整    contain 等比放进纯色底, 保证一个像素都不裁

与其它套件的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 各套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp24"       # PyPI 分发包名
APP_SLUG = "genshen-cp24"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP24"
DISPLAY_NAME = "原神 CP 壁纸套件 24 · 甘雨 × 绫华"
REPO_NAME = "Genshen-skin-CP24"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP24"

# 与其它套件并列展示用
SERIES = "CP24"
PAIR = "甘雨 × 绫华"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 只有一张插画: 甘雨与绫华的新年和服合影, 樱花、红伞与雪景。
IMAGE_FILES = ["01-kimono.jpg"]
IMAGE_NAMES = ["和服"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-kimono.jpg": {
        "title": "和服",
        "desc": "樱花雪景中的和服合影: 甘雨与绫华并肩而立, 一人着白底粉樱和服、"
                "一人着绯红金饰旗袍式外衣; 绫华撑着朱红油纸伞, "
                "背景是飘落的樱花、红色缎带与覆雪的屋檐",
        # 1728x1080 (ar 1.6000)。满屏取景窗 1728x972 —— 横向零裁切, 纵向余量 108px。
        # 两人的脸在**画面上部**, 取景窗贴顶(y=0)才保住头部;
        # 任何 by<=0.35 的取值都会被 clamp 到 y=0, 这里取 0.20 表达"贴顶"意图。
        "pet_crop": (0.42, 0.26, 0.44),
        "cover_bias": (0.50, 0.20),
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
DEEPKING_SKIN_ID = "genshen-cp24-ganyu-ayaka"
DEEPKING_SKIN_NAME = "原神CP24 · 甘雨×绫华"
DEEPKING_SKIN_DESC = (
    "绯红与霜蓝: 主色取自插画采样 —— 红伞与绯色和服的深红, "
    "搭配甘雨的霜蓝发与樱粉、雪景的冷白。亮色为雪白晨光, 夜景为深绯夜色。"
    "32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp24-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp24-dark.jpg"
