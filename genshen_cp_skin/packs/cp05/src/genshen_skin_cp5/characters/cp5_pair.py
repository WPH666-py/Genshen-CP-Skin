# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 5 —— 桑多涅 × 哥伦比娅 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**三张素材**(同一对角色、三套装扮与场景), 每张都能切换三种摆法:

    single1..3   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..3    满屏    cover 铺满整屏, 无边框
    showall1..3  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1~CP4 的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 五个套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp5"        # PyPI 分发包名
APP_SLUG = "genshen-cp5"                 # 命令前缀 / 运行时目录名
APP_NAME = "原神CP5"
DISPLAY_NAME = "原神 CP 壁纸套件 5 · 桑多涅 × 哥伦比娅"
REPO_NAME = "Genshen-skin-CP5"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP5"

# 与其它套件并列展示用
SERIES = "CP5"
PAIR = "桑多涅 × 哥伦比娅"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 三张同一对角色、不同装扮与场景。加图只需追加文件名 + 在 IMAGE_META 补一条,
# 样式列表(MODES)会自动跟着变。
IMAGE_FILES = ["01-street.jpg", "02-cafe.jpg", "03-close.jpg"]
IMAGE_NAMES = ["纸牌", "甜点", "相依"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-street.jpg": {
        "title": "纸牌",
        "desc": "夜景街头: 桑多涅与哥伦比娅执红绸, 扑克牌与锁链环绕, 紫红光幕",
        "pet_crop": (0.34, 0.44, 0.34),
        "cover_bias": (0.50, 0.44),
    },
    "02-cafe.jpg": {
        "title": "甜点",
        "desc": "阳光下的甜品店门前: 两人着校服合影, 摆着剪刀手与手机",
        # 这张是 0.735 的竖图, 对 16:9 需裁掉较多高度, 取景窗上移保住脸
        "pet_crop": (0.50, 0.28, 0.30),
        "cover_bias": (0.50, 0.26),
    },
    "03-close.jpg": {
        "title": "相依",
        "desc": "浅色底特写: 哥伦比娅靠着桑多涅的肩, 两人闭着眼笑",
        "pet_crop": (0.50, 0.32, 0.36),
        "cover_bias": (0.50, 0.42),
    },
}


# ---------------------------------------------------------------- 布局
# 三张素材 × 三种摆法。MODES 由上面的清单自动推导, 不用手写。
def _build_modes():
    out = []
    for suffix, label in (("single", "卡片"), ("cover", "满屏"), ("showall", "完整")):
        for i, name in enumerate(IMAGE_NAMES):
            out.append(("%s%d" % (suffix, i + 1), "%s · %s" % (name, label)))
    return out


MODES = _build_modes()
DEFAULT_MODE = "single1"

# ---------------------------------------------------------------- DeepKing 皮肤
DEEPKING_SKIN_ID = "genshen-cp5-sandrone-columbina"
DEEPKING_SKIN_NAME = "原神CP5 · 桑多涅×哥伦比娅"
DEEPKING_SKIN_DESC = (
    "夜与晨的双色主题: 主色取自插画里桑多涅的紫红发色与哥伦比娅的金发蓝眼, "
    "搭配街灯暖黄。亮色为晨光象牙白, 夜景为夜紫墨黑。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp5-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp5-dark.jpg"
