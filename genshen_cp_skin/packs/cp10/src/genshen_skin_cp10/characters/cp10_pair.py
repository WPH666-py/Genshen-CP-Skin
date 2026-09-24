# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 10 —— 雷电影 × 八重神子 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**三张素材**(鸣神双人: 鸟居花下、沙发和装、雷电之吻), 每张三种摆法:

    single1..3   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..3    满屏    cover 铺满整屏, 无边框
    showall1..3  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1~CP9 的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 十个套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp10"       # PyPI 分发包名
APP_SLUG = "genshen-cp10"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP10"
DISPLAY_NAME = "原神 CP 壁纸套件 10 · 雷电影 × 八重神子"
REPO_NAME = "Genshen-skin-CP10"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP10"

# 与其它套件并列展示用
SERIES = "CP10"
PAIR = "雷电影 × 八重神子"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 三张插画, 比例反差极大(超竖 / 正方 / 横图)。
IMAGE_FILES = ["01-shrine.jpg", "02-sofa.jpg", "03-thunder.jpg"]
IMAGE_NAMES = ["鸟居", "沙发", "雷鸣"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-shrine.jpg": {
        "title": "鸟居",
        "desc": "樱枝与天青下的双人合影: 雷电影紫发紫瞳着紫白和服, 八重神子粉发比着剪刀手, "
                "左侧是朱红鸟居",
        # 942x883 近正方(1.067), 对 16:9 左右各裁一点; 两人脸在中上部, 取景窗略上移
        "pet_crop": (0.50, 0.34, 0.40),
        "cover_bias": (0.50, 0.36),
    },
    "02-sofa.jpg": {
        "title": "沙发",
        "desc": "沙发上依偎而坐: 八重神子着白底樱纹和装, 雷电影着紫色和装戴月牙发饰, "
                "背景是窗光与花环",
        # 600x1000 超竖图(0.600), 对 16:9 要裁掉大量高度;
        # 取景窗上移, 但别过头 —— 0.24 会把雷电影的脸切掉, 0.32 刚好保住两人
        "pet_crop": (0.50, 0.28, 0.28),
        "cover_bias": (0.50, 0.32),
    },
    "03-thunder.jpg": {
        "title": "雷鸣",
        "desc": "黑底紫雷的特写: 雷电影执剑俯身与八重神子相拥, 紫色雷光缠绕剑身",
        # 1832x1280 横图(1.431), 与 16:9 接近, 居中即可
        "pet_crop": (0.55, 0.50, 0.38),
        "cover_bias": (0.52, 0.46),
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
DEEPKING_SKIN_ID = "genshen-cp10-raiden-yae"
DEEPKING_SKIN_NAME = "原神CP10 · 雷电影×八重神子"
DEEPKING_SKIN_DESC = (
    "鸣神双人主题: 主色取自插画采样 —— 雷电影的紫电与八重神子的樱粉, "
    "搭配稻妻的天青与樱枝白。亮色为樱纸冷白, 夜景为墨紫夜色。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp10-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp10-dark.jpg"
