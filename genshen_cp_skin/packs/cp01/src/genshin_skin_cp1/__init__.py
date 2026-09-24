# -*- coding: utf-8 -*-
"""
原神 CP 壁纸套件 1 —— 米提亚 x 沃雅妮莎
单张样式一键切换壁纸 / 桌面桌宠 / 多 IDE 皮肤

    import genshin_skin_cp1 as gs
    gs.build("single2")          # 合成第 2 张壁纸, 返回文件路径
    gs.set_wallpaper(path)       # 设为系统壁纸
"""
from .config import (  # noqa: F401
    APP_DIR,
    APP_NAME,
    APP_SLUG,
    ASSETS_DIR,
    DISPLAY_NAME,
    IMAGE_FILES,
    IMAGE_NAMES,
    MODES,
    PACKAGE_NAME,
    REPO_NAME,
    REPO_URL,
    VERSION,
)
from .skin_core import (  # noqa: F401
    asset_path,
    build,
    build_all,
    compose,
    ensure_dirs,
    ensure_pillow,
    mode_label,
    prepare_console,
    screen_size,
    set_wallpaper,
    wallpaper_path,
)

__all__ = [
    "APP_DIR",
    "APP_NAME",
    "APP_SLUG",
    "ASSETS_DIR",
    "DISPLAY_NAME",
    "IMAGE_FILES",
    "IMAGE_NAMES",
    "MODES",
    "PACKAGE_NAME",
    "REPO_NAME",
    "REPO_URL",
    "VERSION",
    "asset_path",
    "build",
    "build_all",
    "compose",
    "ensure_dirs",
    "ensure_pillow",
    "mode_label",
    "prepare_console",
    "screen_size",
    "set_wallpaper",
    "wallpaper_path",
]

__version__ = VERSION
