# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 21 —— 魈 × 荧 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**三张素材**(魈与荧: 秋叶、拥抱、脸红), 每张三种摆法:

    single1..3   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..3    满屏    cover 铺满整屏, 无边框
    showall1..3  完整    contain 等比放进纯色底, 保证一个像素都不裁

与其它套件的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 各套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp21"       # PyPI 分发包名
APP_SLUG = "genshen-cp21"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP21"
DISPLAY_NAME = "原神 CP 壁纸套件 21 · 魈 × 荧"
REPO_NAME = "Genshen-skin-CP21"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP21"

# 与其它套件并列展示用
SERIES = "CP21"
PAIR = "魈 × 荧"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 三张插画, 都窄于 16:9 -> 满屏时横向零裁切, 只裁上下。
# 注意: 03 源图仅 611x458, 满屏时会放大 3.14x, 比前两张明显偏软(见 README)。
IMAGE_FILES = ["01-autumn.jpg", "02-hug.jpg", "03-blush.jpg"]
IMAGE_NAMES = ["秋叶", "拥抱", "脸红"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-autumn.jpg": {
        "title": "秋叶",
        "desc": "秋叶纷飞中的对视: 魈与荧在漫天橙黄落叶里贴近, 几乎额头相触; "
                "魈墨绿发配琥珀金瞳, 荧金发别着白色小花",
        # 2560x1602 (ar 1.5980)。满屏取景窗 2560x1440 —— 横向零裁切, 纵向余量 162px。
        # 两人面部在中上部, 取景窗略上移。
        "pet_crop": (0.40, 0.44, 0.42),
        "cover_bias": (0.50, 0.42),
    },
    "02-hug.jpg": {
        "title": "拥抱",
        "desc": "白底上的拥抱: 荧笑着搂住魈的肩, 魈红着脸闭眼; "
                "画面带爱心与星星的小符号, 气氛轻松",
        # 1269x1155 (ar 1.0987) —— 本套件第二窄。取景窗 1269x714,
        # 只占源高 62%, 纵向余量 441px。两人的脸在上半部, 取景窗上移(0.34)。
        "pet_crop": (0.50, 0.38, 0.42),
        "cover_bias": (0.50, 0.34),
    },
    "03-blush.jpg": {
        "title": "脸红",
        "desc": "并肩而立的两人: 荧双手捧脸笑着, 魈闭眼红着脸站在旁边; "
                "魈颈间挂着白色串珠与紫珠装饰",
        # 611x458 (ar 1.3341)。取景窗 611x344 —— 横向零裁切, 纵向余量 114px。
        # **源图分辨率偏低**(仅 0.28 MP), 满屏时会放大 3.14x, 观感比前两张软。
        "pet_crop": (0.62, 0.46, 0.42),
        "cover_bias": (0.50, 0.46),
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
DEEPKING_SKIN_ID = "genshen-cp21-xiao-lumine"
DEEPKING_SKIN_NAME = "原神CP21 · 魈×荧"
DEEPKING_SKIN_DESC = (
    "秋叶与墨绿: 主色取自插画采样 —— 魈的青绿发色与荧的暖金, "
    "搭配秋叶橙与米白底。亮色为暖米白, 夜景为墨绿夜色。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp21-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp21-dark.jpg"
