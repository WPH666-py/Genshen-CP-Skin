# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 16 —— 温迪 × 芭芭拉 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件只有**一张素材**(自拍镜头前的双人合影), 提供三种摆法:

    single1   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1    满屏    cover 铺满整屏, 无边框
    showall1  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1~CP14 的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 各套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp16"       # PyPI 分发包名
APP_SLUG = "genshen-cp16"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP16"
DISPLAY_NAME = "原神 CP 壁纸套件 16 · 温迪 × 芭芭拉"
REPO_NAME = "Genshen-skin-CP16"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP16"

# 与其它套件并列展示用
SERIES = "CP16"
PAIR = "温迪 × 芭芭拉"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 只有一张插画。画面里的 REC / HD / 时间码 / 四角框线是**刻意的摄像机取景框设计**,
# 不是水印, 因此无需任何修补。
IMAGE_FILES = ["01-rec.jpg"]
IMAGE_NAMES = ["自拍"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-rec.jpg": {
        "title": "自拍",
        "desc": "镜头前的双人自拍: 温迪黑绿发扎双辫、竖拇指, 芭芭拉金发比双剪刀手; "
                "画面带 REC 红点、HD 标识、时间码与四角框线, 背景是晴空白云",
        # 2304x1440 (ar=1.6)。满屏取景窗 2304x1296 —— **横向零裁切**, 纵向余量 144px。
        # 取景窗居中(0.5): 上下各裁 72px; 画面上下的框线与时间码都在安全区内。
        "pet_crop": (0.28, 0.45, 0.42),
        "cover_bias": (0.50, 0.50),
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
DEEPKING_SKIN_ID = "genshen-cp16-venti-barbara"
DEEPKING_SKIN_NAME = "原神CP16 · 温迪×芭芭拉"
DEEPKING_SKIN_DESC = (
    "镜头前的双子: 主色取自插画采样 —— 芭芭拉的暖金发色与温迪的薄荷绿, "
    "搭配晴空的天青与深蓝。亮色为晴空米白, 夜景为深蓝夜色。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp16-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp16-dark.jpg"
