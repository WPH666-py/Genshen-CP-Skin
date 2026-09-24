# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 12 —— 行秋 × 重云 · 角色与素材定义

这是**唯一需要为本套件改动的文件**。引擎(engine/)与各 CLI/IDE 适配层全部
读取本文件里的常量, 因此把本文件换成别的角色组合, 整套工具即刻复用。

本套件有**三张素材**(冰与水的双人: 月下对坐、蓝伞同撑、晴空天台), 每张三种摆法:

    single1..3   卡片式  模糊填充背景 + 居中圆角卡片, 构图完整不裁切
    cover1..3    满屏    cover 铺满整屏, 无边框
    showall1..3  完整    contain 等比放进纯色底, 保证一个像素都不裁

与 CP1~CP11 的命名空间完全隔离: 包名 / 命令前缀 / 运行时目录 /
vscode 扩展 ID / DeepKing 皮肤 id 均不冲突, 十二个套件可以同时安装。
"""

# ---------------------------------------------------------------- 身份
VERSION = "0.1.0"
PACKAGE_NAME = "genshen-skin-cp12"       # PyPI 分发包名
APP_SLUG = "genshen-cp12"                # 命令前缀 / 运行时目录名
APP_NAME = "原神CP12"
DISPLAY_NAME = "原神 CP 壁纸套件 12 · 行秋 × 重云"
REPO_NAME = "Genshen-skin-CP12"
REPO_URL = "https://github.com/WPH666-py/Genshen-skin-CP12"

# 与其它套件并列展示用
SERIES = "CP12"
PAIR = "行秋 × 重云"

# ---------------------------------------------------------------- 运行时目录
# 生成物一律放这里, 不改动仓库/安装目录
import os as _os

APP_DIR = _os.path.join(_os.path.expanduser("~"), "." + APP_SLUG)
WALLPAPER_DIR = _os.path.join(APP_DIR, "wallpapers")
CACHE_DIR = _os.path.join(APP_DIR, "cache")

# 素材目录: 引擎包数据(engine/assets), 由 engine.skin_core 解析
ASSETS_DIR = ""

# ---------------------------------------------------------------- 素材
# 三张插画。注意三张都**窄于 16:9**(1.333 / 1.365 / 1.412),
# 因此满屏取景窗横向会用满整张源图(可平移 x=0), 只能上下裁。
IMAGE_FILES = ["01-moon.jpg", "02-umbrella.jpg", "03-sky.jpg"]
IMAGE_NAMES = ["月下", "蓝伞", "晴空"]

# 每张素材的说明(画廊/README 用), 键为 IMAGE_FILES 中的文件名
#   pet_crop   桌宠取景: (中心x比例, 中心y比例, 半边长占最短边比例)
#   cover_bias 满屏取景偏向, 用于避免裁到脸
IMAGE_META = {
    "01-moon.jpg": {
        "title": "月下",
        "desc": "满月前的双人对坐: 重云持冰蓝长剑与雪花, 行秋托腮含笑, "
                "左下角是嫩芽黄的花丛",
        # 1101x826 横图(1.333), 取景窗 1101x619, 纵向余量 207
        "pet_crop": (0.50, 0.42, 0.40),
        "cover_bias": (0.50, 0.40),
    },
    "02-umbrella.jpg": {
        "title": "蓝伞",
        "desc": "蓝伞与花枝下: 重云着白底蓝纹中式外袍, 行秋执折扇比耶, "
                "水蓝色史莱姆与雪花点缀四周",
        # 原图 688x600, **右下角带画师水印**(y≈570..600)。
        # 这张窄于 16:9, 取景窗横向用满整张源图、只能上下裁, 所以靠 cover_bias
        # **无法**把水印移出画面 —— 入库前已预裁掉 y>=504, 水印永久移除,
        # 同时两人与伞面完整保留。
        "pet_crop": (0.52, 0.40, 0.42),
        "cover_bias": (0.50, 0.40),
    },
    "03-sky.jpg": {
        "title": "晴空",
        "desc": "晴空天台: 重云穿白色连帽衫吃冰棍, 行秋着校服外套读着书, "
                "左侧趴着一只猫",
        # 850x602 横图(1.412), 取景窗 850x478, 纵向余量 124
        "pet_crop": (0.46, 0.46, 0.42),
        "cover_bias": (0.46, 0.46),
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
DEEPKING_SKIN_ID = "genshen-cp12-xingqiu-chongyun"
DEEPKING_SKIN_NAME = "原神CP12 · 行秋×重云"
DEEPKING_SKIN_DESC = (
    "冰与水的双色: 主色取自插画采样 —— 行秋的靛蓝与重云的霜白冰蓝, "
    "搭配满月的暖月华与嫩芽黄。亮色为霜白晨光, 夜景为深靛夜色。32 槽位逐项校色。"
)
# DeepKing 转换器只认 assets/background/ 下的图片作为编辑区水印
DEEPKING_MASCOT_LIGHT = "assets/background/mascot-cp12-light.jpg"
DEEPKING_MASCOT_DARK = "assets/background/mascot-cp12-dark.jpg"
