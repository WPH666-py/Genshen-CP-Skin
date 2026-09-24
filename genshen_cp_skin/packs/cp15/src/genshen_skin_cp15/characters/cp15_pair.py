# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 15 —— 甘雨 × 刻晴 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**三张素材**(甘雨与刻晴: 灯宵夜游、樱桥散步、厨房早餐), 每张三种摆法:

    single1..3   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..3    满屏    cover 铺满整屏, 无边框
    showall1..3  完整    contain 等比放进纯色底, 保证一个像素都不裁

与其它套件的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 各套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp15"       # PyPI 分发包名
APP_SLUG = "genshen-cp15"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP15"
DISPLAY_NAME = "原神 CP 壁纸套件 15 · 甘雨 × 刻晴"
REPO_NAME = "Genshen-skin-CP15"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP15"

# 与其它套件并列展示用
SERIES = "CP15"
PAIR = "甘雨 × 刻晴"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 三张插画。01 的 ar 是 1.7781, 与 16:9 几乎相同(横向可平移 0.4px), 等于整张原图。
IMAGE_FILES = ["01-lantern.jpg", "02-bridge.jpg", "03-kitchen.jpg"]
IMAGE_NAMES = ["灯宵", "樱桥", "厨房"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-lantern.jpg": {
        "title": "灯宵",
        "desc": "灯宵夜游: 甘雨趴在栏杆上回望, 刻晴提着灯笼站在右侧; "
                "背景是漫天孔明灯、满月与远处的璃月楼阁",
        # 2276x1280, ar=1.7781 —— 与 16:9 的 1.7778 几乎相同, 取景窗 2276x1280
        # 等于整张原图(横向仅 0.4px 余量), 居中即可。
        "pet_crop": (0.24, 0.50, 0.40),
        "cover_bias": (0.50, 0.50),
    },
    "02-bridge.jpg": {
        "title": "樱桥",
        "desc": "樱花桥上的散步: 甘雨穿白色上衣与深色短裙挥手, 刻晴围绿围巾、"
                "提着白色手提包; 背景是樱枝、水面与远处的都市轮廓",
        # 1920x1547 (ar 1.2411)。满屏取景窗 1920x1080 —— 横向零裁切, 纵向余量 467px。
        # 两人头顶在上方, 取景窗上移(0.36)以免切到发顶。
        # 注: 原图左下角有画师署名, 按用户决定保留原样(见 README)。
        "pet_crop": (0.50, 0.42, 0.42),
        "cover_bias": (0.50, 0.36),
    },
    "03-kitchen.jpg": {
        "title": "厨房",
        "desc": "厨房里的早餐: 甘雨在料理台前打蛋, 刻晴围着粉色围裙掌勺煎蛋; "
                "背景是明亮的白色厨房与餐具",
        # 1256x837 (ar 1.5006)。取景窗 1256x706 —— 横向零裁切, 纵向余量 130px。
        "pet_crop": (0.50, 0.45, 0.42),
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
DEEPKING_SKIN_ID = "genshen-cp15-ganyu-keqing"
DEEPKING_SKIN_NAME = "原神CP15 · 甘雨×刻晴"
DEEPKING_SKIN_DESC = (
    "冰与雷的双子: 主色取自插画采样 —— 甘雨的冰蓝与刻晴的夜紫, "
    "搭配樱粉与灯宵的暖光。亮色为霜白晨光, 夜景为深紫夜色。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp15-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp15-dark.jpg"
