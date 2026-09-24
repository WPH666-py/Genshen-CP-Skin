# -*- coding: utf-8 -*-
"""genshen_cp_skin —— 原神 CP 壁纸套件合集（24 套），一个安装包全部带走。

与「一套一个仓库」的做法不同，这里把 24 套的**源图与各自自带引擎**都打进包里，
所以装完即可离线使用：`gc install cp24` 不联网、不需要 git。

命令入口 `gc`（Genshen CP）：
    gc list                 列出 24 套
    gc show cp24            看某套的素材与摆法
    gc install cp24         一键：壁纸 + IDE 扩展 + 桌宠
    gc wallpaper cp24       换摆法
    gc cmd                  全部命令总览
"""
__version__ = "1.0.0"
__all__ = ["load_catalog", "find_pack", "packs", "list_metas", "__version__"]


def load_catalog(refresh=False):
    from . import catalog as _c
    return _c.load_catalog(refresh=refresh)


def packs():
    return load_catalog()["packs"]


def list_metas():
    """每套的简要信息，供 UI / AI 快速枚举。"""
    return [{"id": p["id"], "no": p["no"], "name": p["name"],
             "char": p["char"], "accent": p["accent"],
             "sources": len(p.get("sources") or []), "modes": p.get("modes")}
            for p in packs()]


def find_pack(key):
    from . import catalog as _c
    return _c.find_pack(load_catalog(), key)
