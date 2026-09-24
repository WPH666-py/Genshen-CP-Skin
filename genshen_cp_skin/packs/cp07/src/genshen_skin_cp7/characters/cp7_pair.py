# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 7 —— 娜维娅 × 克洛琳德 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**三张素材**(枫丹双人: 花园洛丽塔、海滩泳装、下午茶), 每张都能切换三种摆法:

    single1..3   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..3    满屏    cover 铺满整屏, 无边框
    showall1..3  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1~CP6 的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 七个套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp7"        # PyPI 分发包名
APP_SLUG = "genshen-cp7"                 # 命令前缀 / 运行时目录名
APP_NAME = "原神CP7"
DISPLAY_NAME = "原神 CP 壁纸套件 7 · 娜维娅 × 克洛琳德"
REPO_NAME = "Genshen-skin-CP7"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP7"

# 与其它套件并列展示用
SERIES = "CP7"
PAIR = "娜维娅 × 克洛琳德"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 三张枫丹双人插画, 比例各不相同(竖图 / 16:9 / 正方)。
IMAGE_FILES = ["01-garden.jpg", "02-beach.jpg", "03-tea.jpg"]
IMAGE_NAMES = ["花园", "海滩", "下午茶"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-garden.jpg": {
        "title": "花园",
        "desc": "淡彩花园前的双人立绘: 克洛琳德着蓝色洛丽塔长裙, 娜维娅着琥珀金礼裙, "
                "背景是柔焦的花瓣",
        # 1200x1600 竖图(0.75), 两人上下错开, 对 16:9 要裁掉较多高度, 取景窗上移
        "pet_crop": (0.52, 0.34, 0.30),
        "cover_bias": (0.50, 0.34),
    },
    "02-beach.jpg": {
        "title": "海滩",
        "desc": "海滩遮阳伞下: 克洛琳德与娜维娅的夏日泳装合影, 背景是碧海椰林",
        # 4096x2304 正好 16:9(1.778), 几乎不需要裁
        "pet_crop": (0.50, 0.45, 0.42),
        "cover_bias": (0.50, 0.48),
    },
    "03-tea.jpg": {
        "title": "下午茶",
        "desc": "茶座对坐: 娜维娅举着马卡龙, 克洛琳德端着红茶, 桌上三层点心架",
        # 986x986 正方(1.000), 对 16:9 左右要各裁一点, 居中即可
        "pet_crop": (0.50, 0.46, 0.40),
        "cover_bias": (0.50, 0.48),
    },
}


# ---------------------------------------------------------------- 布局
# 三张素材 × 三种摆法。MODES 由上面的清单自动推导, 不用手写。
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
DEEPKING_SKIN_ID = "genshen-cp7-navia-clorinde"
DEEPKING_SKIN_NAME = "原神CP7 · 娜维娅×克洛琳德"
DEEPKING_SKIN_DESC = (
    "枫丹双人主题: 主色取自插画采样 —— 娜维娅的琥珀金与克洛琳德的深蓝紫, "
    "搭配淡雾蓝与花园粉白。亮色为象牙粉白, 夜景为深蓝紫。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp7-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp7-dark.jpg"
