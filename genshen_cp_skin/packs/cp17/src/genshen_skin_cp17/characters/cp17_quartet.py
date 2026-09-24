# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 17 —— 奥黛塔 × 沃雅妮莎 × 米提亚 × 阿罗夏 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件只有**一张素材**(2x2 四宫格, 四位角色各占一格), 提供三种摆法:

    showall1  完整    contain 等比放进纯色底, 保证一个像素都不裁  <- 本套件默认
    single1   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1    满屏    cover 铺满整屏, 无边框

**为什么默认是「完整」而不是其它套件的「卡片式」**
素材是 1104x1480 的竖图(ar 0.746), 而屏幕通常是 16:9(1.778)。竖图铺满 16:9
必须上下裁掉大半 —— 满屏取景窗只占源高的 42%, 会正好从四宫格中间横切过去,
四位角色都只剩一部分。所以默认用「完整」: 整张图完整显示, 左右留同色边,
四格都看得见。用户想要满屏效果时仍可显式用 `genshen-cp17 cover`。

与其它套件的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 各套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp17"       # PyPI 分发包名
APP_SLUG = "genshen-cp17"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP17"
DISPLAY_NAME = "原神 CP 壁纸套件 17 · 奥黛塔 × 沃雅妮莎 × 米提亚 × 阿罗夏"
REPO_NAME = "Genshen-skin-CP17"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP17"

# 与其它套件并列展示用
SERIES = "CP17"
PAIR = "奥黛塔 × 沃雅妮莎 × 米提亚 × 阿罗夏"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 只有一张插画: 2x2 四宫格, 左上奥黛塔、右上沃雅妮莎、左下米提亚、右下阿罗夏。
# 四位都穿深蓝/灰蓝校服, 背景是浅色底 + 淡樱粉与铃兰等吉祥物纹样。
IMAGE_FILES = ["01-quartet.jpg"]
IMAGE_NAMES = ["四人合影"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-quartet.jpg": {
        "title": "四人合影",
        "desc": "2x2 四宫格校服合影: 左上奥黛塔(青绿发, 抱蓝色吉祥物)、"
                "右上沃雅妮莎(银发, 校服领结)、左下米提亚(银白发, 背双肩包)、"
                "右下阿罗夏(银卷发, 眨眼比耶); 四人皆深蓝校服, 背景浅色底配淡樱粉",
        # 1104x1480 竖图(ar 0.7459)。满屏取景窗 1104x621 —— 横向用满整幅,
        # 纵向只占源高 42%, 会从四宫格中间横切。因此默认走 showall1(完整)。
        "pet_crop": (0.28, 0.24, 0.34),
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
# 竖图铺满 16:9 会横切四宫格, 所以默认用「完整」而不是「卡片式」。
DEFAULT_MODE = "showall1"

# ---------------------------------------------------------------- DeepKing 皮肤
DEEPKING_SKIN_ID = "genshen-cp17-odette-voyanisa-mitiya-arosha"
DEEPKING_SKIN_NAME = "原神CP17 · 奥黛塔×沃雅妮莎×米提亚×阿罗夏"
DEEPKING_SKIN_DESC = (
    "四格合影: 主色取自插画采样 —— 四人校服的雾蓝与薰衣草紫, "
    "搭配浅色底的霜白与淡樱粉。亮色为霜白晨光, 夜景为深靛蓝夜色。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp17-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp17-dark.jpg"
