# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 13 —— 钟离 × 凝光 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件只有**一张素材**(秋日璃月港茶叙), 提供三种摆法:

    single1   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1    满屏    cover 铺满整屏, 无边框
    showall1  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1~CP12 的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 十三个套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp13"       # PyPI 分发包名
APP_SLUG = "genshen-cp13"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP13"
DISPLAY_NAME = "原神 CP 壁纸套件 13 · 钟离 × 凝光"
REPO_NAME = "Genshen-skin-CP13"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP13"

# 与其它套件并列展示用
SERIES = "CP13"
PAIR = "钟离 × 凝光"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 只有一张插画。入库前已裁掉 y>=520, 移除右下角的画师署名。
IMAGE_FILES = ["01-tea.jpg"]
IMAGE_NAMES = ["茶叙"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-tea.jpg": {
        "title": "茶叙",
        "desc": "秋日璃月港的茶席: 凝光在左举杯回望, 钟离在右端杯对视, "
                "桌上摆着茶点与热菜, 背景是层叠的璃月楼阁与漫山红叶",
        # 原图 1000x562, ar=1.7794 —— 与 16:9 的 1.7778 几乎相同, 满屏取景窗
        # 999x562(横向可平移 0.9px、纵向 0px), 等于整张原图。因此**右下角的
        # 画师署名无法靠 cover_bias 规避**, 入库前已预裁掉 y>=520 永久移除
        # (署名位于 x≈887..963, y≈528..553)。
        "pet_crop": (0.22, 0.52, 0.34),
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
DEEPKING_SKIN_ID = "genshen-cp13-zhongli-ningguang"
DEEPKING_SKIN_NAME = "原神CP13 · 钟离×凝光"
DEEPKING_SKIN_DESC = (
    "秋日璃月港: 主色取自插画采样 —— 钟离的琥珀褐与凝光的璃月金, "
    "搭配秋枫的橙与远山的灰蓝。亮色为暖宣纸金, 夜景为深褐夜色。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp13-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp13-dark.jpg"
