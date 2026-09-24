# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 19 —— 空 × 荧 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**三张素材**(旅行者双子: 星海、窗边、林间), 每张三种摆法:

    single1..3   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..3    满屏    cover 铺满整屏, 无边框
    showall1..3  完整    contain 等比放进纯色底, 保证一个像素都不裁

与其它套件的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 各套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp19"       # PyPI 分发包名
APP_SLUG = "genshen-cp19"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP19"
DISPLAY_NAME = "原神 CP 壁纸套件 19 · 空 × 荧"
REPO_NAME = "Genshen-skin-CP19"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP19"

# 与其它套件并列展示用
SERIES = "CP19"
PAIR = "空 × 荧"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 三张插画。01 ar=1.7767 与 16:9 几乎相同(满屏即整张); 02/03 窄于 16:9, 只裁上下。
IMAGE_FILES = ["01-space.jpg", "02-window.jpg", "03-forest.jpg"]
IMAGE_NAMES = ["星海", "窗边", "林间"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸 / 挤出作者署名
IMAGE_META = {
    "01-space.jpg": {
        "title": "星海",
        "desc": "星空中的重逢: 荧着白色礼裙向上升, 空伸手去够她; "
                "背景是深蓝星海与地球弧线, 蓝金星带环绕两人",
        # 1066x600, ar=1.7767 —— 与 16:9 的 1.7778 几乎相同, 取景窗等于整张原图。
        "pet_crop": (0.36, 0.48, 0.40),
        "cover_bias": (0.50, 0.50),
    },
    "02-window.jpg": {
        "title": "窗边",
        "desc": "冬日窗边的相依: 空戴着围巾扶住荧, 两人着深蓝外套; "
                "背景是窗外的雪景与暖阳",
        # 1216x832 (ar 1.4615)。取景窗 1216x684 —— 横向零裁切, 纵向余量 148px。
        "pet_crop": (0.46, 0.44, 0.44),
        "cover_bias": (0.50, 0.46),
    },
    "03-forest.jpg": {
        "title": "林间",
        "desc": "林间的花冠少女与少年: 荧戴着白色花冠笑着招手, 空坐在旁边; "
                "背景是青绿的林间、蓝色蝴蝶与远处的浮空岛",
        # 1810x1280 (ar 1.4141)。取景窗 1810x1018 —— 横向零裁切, 纵向余量 262px。
        # **右下角有画师署名**(x≈1658..1774, y≈1200..1237)。取景窗取 0.48
        # (源 y≈113..1131)即可把署名排除在画面外, 无需修补素材。
        "pet_crop": (0.40, 0.52, 0.42),
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
DEEPKING_SKIN_ID = "genshen-cp19-aether-lumine"
DEEPKING_SKIN_NAME = "原神CP19 · 空×荧"
DEEPKING_SKIN_DESC = (
    "双子同行: 主色取自插画采样 —— 空与荧共有的暖金发色, "
    "搭配星海的深蓝与林间的青绿。亮色为暖白晨光, 夜景为深海星夜。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp19-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp19-dark.jpg"
