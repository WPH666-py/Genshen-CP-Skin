# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 20 —— 散兵 × 荧 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**三张素材**(散兵与荧: 触碰、依偎、水畔), 每张三种摆法:

    single1..3   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..3    满屏    cover 铺满整屏, 无边框
    showall1..3  完整    contain 等比放进纯色底, 保证一个像素都不裁

与其它套件的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 各套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp20"       # PyPI 分发包名
APP_SLUG = "genshen-cp20"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP20"
DISPLAY_NAME = "原神 CP 壁纸套件 20 · 散兵 × 荧"
REPO_NAME = "Genshen-skin-CP20"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP20"

# 与其它套件并列展示用
SERIES = "CP20"
PAIR = "散兵 × 荧"

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
IMAGE_FILES = ["01-touch.jpg", "02-close.jpg", "03-water.jpg"]
IMAGE_NAMES = ["触碰", "依偎", "水畔"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-touch.jpg": {
        "title": "触碰",
        "desc": "留白花瓣中的对望: 散兵戴着宽檐斗笠俯身托起荧的下巴, 两人侧脸相对; "
                "荧金发别着紫色小花, 散兵深蓝发配蓝瞳",
        # 4093x2894 (ar 1.4143)。满屏取景窗 4093x2302 —— 横向零裁切, 纵向余量 592px。
        # 两人的脸在中上部, 取景窗略上移保住整张脸。
        "pet_crop": (0.46, 0.42, 0.42),
        "cover_bias": (0.50, 0.42),
    },
    "02-close.jpg": {
        "title": "依偎",
        "desc": "浅色底的双人合影: 荧戴白花冠笑着看向镜头, 散兵在她身侧微笑; "
                "散兵背后是蓝金纹样的斗笠与深蓝披风",
        # 1312x1195 (ar 1.0979) —— 本套件最窄的一张。取景窗 1312x738,
        # 只占源高 62%, 纵向余量 457px。两人的脸在上半部, 取景窗必须上移(0.34)。
        "pet_crop": (0.46, 0.38, 0.42),
        "cover_bias": (0.50, 0.34),
    },
    "03-water.jpg": {
        "title": "水畔",
        "desc": "水畔夜色中的相依: 散兵着白衬衫俯身, 荧仰头望着他; "
                "背景是深墨蓝的水面、浮动光影与朱红的落花",
        # 3076x1922 (ar 1.6004)。取景窗 3076x1730 —— 横向零裁切, 纵向余量 192px。
        "pet_crop": (0.62, 0.55, 0.40),
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
DEEPKING_SKIN_ID = "genshen-cp20-scaramouche-lumine"
DEEPKING_SKIN_NAME = "原神CP20 · 散兵×荧"
DEEPKING_SKIN_DESC = (
    "深靛与暖金: 主色取自插画采样 —— 散兵的深靛紫发与荧的暖金, "
    "搭配水畔的深墨蓝与朱红落花。亮色为月白宣纸, 夜景为深靛夜色。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp20-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp20-dark.jpg"
