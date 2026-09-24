# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 11 —— 胡桃 × 香菱 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**三张素材**(锅巴与往生堂: 料理合影、锅巴火锅、灯笼夜市), 每张三种摆法:

    single1..3   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..3    满屏    cover 铺满整屏, 无边框
    showall1..3  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1~CP10 的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 十一个套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp11"       # PyPI 分发包名
APP_SLUG = "genshen-cp11"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP11"
DISPLAY_NAME = "原神 CP 壁纸套件 11 · 胡桃 × 香菱"
REPO_NAME = "Genshen-skin-CP11"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP11"

# 与其它套件并列展示用
SERIES = "CP11"
PAIR = "胡桃 × 香菱"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 三张插画, 都是横图(1.414 / 1.493 / 1.778)。
IMAGE_FILES = ["01-goofy.jpg", "02-hotpot.jpg", "03-lantern.jpg"]
IMAGE_NAMES = ["料理", "锅巴", "夜市"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸 / 挤出作者水印
IMAGE_META = {
    "01-goofy.jpg": {
        "title": "料理",
        "desc": "白底双人特写: 胡桃戴红框护目镜笑得灿烂, 香菱顶着熊耳帽比耶、"
                "手里托着一只包子",
        # 2048x1448 横图(1.414), 与 16:9 接近, 两人脸在中部偏上
        "pet_crop": (0.45, 0.42, 0.38),
        "cover_bias": (0.48, 0.42),
    },
    "02-hotpot.jpg": {
        "title": "锅巴",
        "desc": "暖光室内: 两人围着咕嘟冒泡的火锅比手势, 左上角是锅巴的白色虚影, "
                "右侧趴着一只熊玩偶",
        # 896x600 横图(1.493), 居中即可
        "pet_crop": (0.50, 0.46, 0.40),
        "cover_bias": (0.50, 0.46),
    },
    "03-lantern.jpg": {
        "title": "夜市",
        "desc": "灯笼夜市: 胡桃坐在石栏上举着点心, 香菱牵着一只熊玩偶, "
                "背景是朱红牌楼与漫天灯火",
        # 原图 800x450 是官方宣传图, **左上角带 Genshin logo**, 且恰好就是 16:9 ——
        # 满屏取景窗横向会用掉整张源图, 没有任何平移余地, 靠 cover_bias 无法规避。
        # 所以这里不靠取景, 而是**入库前已把素材预裁成 4:3**(x 从 130 起):
        # logo 止于 x≈90, 左边角色自 x≈167 起, 裁掉 130 左侧即可永久移除 logo,
        # 且三种摆法在任意屏幕比例下都不会再看到它。
        "pet_crop": (0.52, 0.46, 0.38),
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
DEEPKING_SKIN_ID = "genshen-cp11-hutao-xiangling"
DEEPKING_SKIN_NAME = "原神CP11 · 胡桃×香菱"
DEEPKING_SKIN_DESC = (
    "锅巴与往生堂: 主色取自插画采样 —— 胡桃的赤红与香菱的暖橙, "
    "搭配灯笼夜市的栗棕与深绯。亮色为暖宣纸白, 夜景为深栗夜色。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp11-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp11-dark.jpg"
