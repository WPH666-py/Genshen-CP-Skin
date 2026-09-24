# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 18 —— 散兵 × 万叶 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**三张素材**(散兵与万叶: 并肩特写、轻吻、取景框合影), 每张三种摆法:

    single1..3   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..3    满屏    cover 铺满整屏, 无边框
    showall1..3  完整    contain 等比放进纯色底, 保证一个像素都不裁

与其它套件的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 各套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp18"       # PyPI 分发包名
APP_SLUG = "genshen-cp18"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP18"
DISPLAY_NAME = "原神 CP 壁纸套件 18 · 散兵 × 万叶"
REPO_NAME = "Genshen-skin-CP18"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP18"

# 与其它套件并列展示用
SERIES = "CP18"
PAIR = "散兵 × 万叶"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 三张插画。01/02 窄于 16:9(只裁上下), 03 正好 16:9(满屏即整张原图)。
IMAGE_FILES = ["01-close.jpg", "02-kiss.jpg", "03-rec.jpg"]
IMAGE_NAMES = ["特写", "轻吻", "取景"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-close.jpg": {
        "title": "特写",
        "desc": "浅色底的双人特写: 散兵抬手轻抚万叶的脸, 两人侧脸相对; "
                "万叶白发带枫红挑染, 散兵深蓝发配紫瞳",
        # 719x565 (ar 1.2726)。满屏取景窗 719x404 —— 横向零裁切, 纵向余量 161px。
        # 两人的脸在中上部, 取景窗上移(0.38)保住整张脸。
        "pet_crop": (0.44, 0.40, 0.44),
        "cover_bias": (0.50, 0.38),
    },
    "02-kiss.jpg": {
        "title": "轻吻",
        "desc": "留白背景下的轻吻: 散兵俯身亲吻万叶, 手托着他的脸颊; "
                "万叶白发红挑染, 散兵深蓝发配蓝色和风外袍",
        # 968x676 (ar 1.4320)。取景窗 968x544 —— 横向零裁切, 纵向余量 132px。
        "pet_crop": (0.50, 0.42, 0.44),
        "cover_bias": (0.50, 0.40),
    },
    "03-rec.jpg": {
        "title": "取景",
        "desc": "镜头取景框中的牵手: 散兵伸手去够万叶, 万叶伸手回应; "
                "画面带 ISO / 1080P / 1/250 / F2.7 / REC 的摄像机取景框设计",
        # 1920x1080 —— **正好 16:9**, 满屏取景窗等于整张原图(x/y 余量均为 0)。
        # 画面里的 ISO / 1080P / F2.7 / REC 是刻意的摄像机取景框设计, 不是水印。
        "pet_crop": (0.50, 0.45, 0.40),
        "cover_bias": (0.50, 0.50),
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
DEEPKING_SKIN_ID = "genshen-cp18-scaramouche-kazuha"
DEEPKING_SKIN_NAME = "原神CP18 · 散兵×万叶"
DEEPKING_SKIN_DESC = (
    "紫蓝与霜白: 主色取自插画采样 —— 散兵的深靛紫发与万叶的霜白, "
    "点缀万叶的枫红挑染与朱红腰饰。亮色为月白宣纸, 夜景为深靛夜色。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp18-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp18-dark.jpg"
