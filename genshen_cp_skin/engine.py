# -*- coding: utf-8 -*-
"""genshen_cp_skin.engine —— 调用某一套自带的引擎。

CP 的壁纸合成逻辑在各套自己的引擎里（按用户屏幕分辨率现算），
本包不重写它，而是把它**拉起来用**：铺开仓库树 -> 加 sys.path -> 调它的 main()。

这样 `gc` 的行为与用户直接跑官方引擎完全一致，不会出现两套实现走偏。
"""
import importlib
import os
import sys

from . import repo


def ensure_local(pack, quiet=False):
    """确保该套已铺开，返回仓库根目录。"""
    dst = repo.materialize(pack, quiet=quiet)
    if dst:
        return dst
    # 包里没有（理论上不会发生）——退回到"已克隆的本地副本"
    return repo.skin_dir(pack["repo"])


def cli_path(pack, root=None):
    root = root or ensure_local(pack, quiet=True)
    rel = (pack.get("engine") or {}).get("cli")
    if not rel:
        return None
    p = os.path.join(root, rel.replace("/", os.sep))
    return p if os.path.isfile(p) else None


def is_available(pack):
    return cli_path(pack, root=repo.skin_dir(pack["repo"])) is not None


def run(pack, argv, quiet=False):
    """以 `argv` 调用该套自带引擎，返回退出码。

    不另起进程：直接把 `<仓库>/src` 放进 sys.path 再 import。
    引擎内部全是相对导入，所以外层目录叫什么名字都不影响。
    """
    root = ensure_local(pack, quiet=quiet)
    cli = cli_path(pack, root=root)
    if not cli:
        raise RuntimeError("%s 里没找到引擎 cli.py（期望 %s）"
                           % (pack["repo"], (pack.get("engine") or {}).get("cli")))
    src = os.path.join(root, "src")
    module = (pack.get("engine") or {}).get("module")
    if not module:
        raise RuntimeError("%s 的 catalog 条目缺少 engine.module" % pack["id"])

    added = False
    if src not in sys.path:
        sys.path.insert(0, src)
        added = True
    saved = sys.argv
    try:
        try:
            mod = importlib.import_module(module)
        except ImportError as e:
            raise RuntimeError("无法导入 %s 的引擎（%s）: %s" % (pack["repo"], module, e))
        fn = getattr(mod, "main", None)
        if fn is None:
            raise RuntimeError("引擎 %s 没有 main()" % cli)
        sys.argv = [os.path.basename(cli)] + list(argv)
        return int(fn() or 0)
    finally:
        sys.argv = saved
        if added:
            try:
                sys.path.remove(src)
            except ValueError:
                pass
        # 引擎模块可能与其它套重名（都是 <pkg>.engine.*），用完即清，避免串味
        for name in list(sys.modules):
            if name.split(".")[0] in {module.split(".")[0]}:
                sys.modules.pop(name, None)


def describe_modes(pack):
    from . import catalog
    return catalog.modes_of(pack)


def install_hint(pack):
    """给用户/AI 的后续操作提示。"""
    return [
        "换摆法   gc wallpaper %s cover1     # 或 single1 / showall1" % pack["id"],
        "全部生成 gc wallpaper %s all" % pack["id"],
        "看摆法   gc wallpaper %s --list" % pack["id"],
        "卸载     gc uninstall %s" % pack["id"],
    ]
