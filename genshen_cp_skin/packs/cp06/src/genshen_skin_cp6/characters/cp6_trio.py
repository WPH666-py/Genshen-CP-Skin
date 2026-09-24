# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 6 —— 玛拉妮 × 基尼奇 × 卡其娜 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**两张素材**(纳塔三人组: 玛拉妮、基尼奇、卡其娜), 每张都能切换三种摆法:

    single1..2   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..2    满屏    cover 铺满整屏, 无边框
    showall1..2  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1~CP5 的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 六个套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp6"        # PyPI 分发包名
APP_SLUG = "genshen-cp6"                 # 命令前缀 / 运行时目录名
APP_NAME = "原神CP6"
DISPLAY_NAME = "原神 CP 壁纸套件 6 · 玛拉妮 × 基尼奇 × 卡其娜"
REPO_NAME = "Genshen-skin-CP6"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP6"

# 与其它套件并列展示用
SERIES = "CP6"
PAIR = "玛拉妮 × 基尼奇 × 卡其娜"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 两张纳塔三人组插画。加图只需追加文件名 + 在 IMAGE_META 补一条,
# 样式列表(MODES)会自动跟着变。
IMAGE_FILES = ["01-natlan.jpg", "02-group.jpg"]
IMAGE_NAMES = ["午后", "三人"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-natlan.jpg": {
        "title": "午后",
        "desc": "暖色调插画: 基尼奇与玛拉妮并肩而坐闭目小憩, 卡其娜在右侧端着点心, "
                "背后是彩色挂毯与花纹地毯",
        # 横图(1.440), 三人分布在左中右, 居中取景即可
        "pet_crop": (0.50, 0.42, 0.40),
        "cover_bias": (0.50, 0.44),
    },
    "02-group.jpg": {
        "title": "三人",
        "desc": "夕阳下的三人合影: 基尼奇在左, 玛拉妮在中间吐舌笑, 卡其娜在右, "
                "暖橙到粉紫的渐变天空",
        # 这张正好是 16:9(1.775), 与屏幕比例接近, 几乎不需要裁
        "pet_crop": (0.50, 0.45, 0.40),
        "cover_bias": (0.50, 0.48),
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
DEEPKING_SKIN_ID = "genshen-cp6-mualani-kinich-kachina"
DEEPKING_SKIN_NAME = "原神CP6 · 玛拉妮×基尼奇×卡其娜"
DEEPKING_SKIN_DESC = (
    "纳塔暖色主题: 主色取自插画里玛拉妮的碧蓝与基尼奇的红棕, 搭配卡其娜的赭金; "
    "亮色为暖阳米白, 夜景为深靛墨黑。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp6-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp6-dark.jpg"
