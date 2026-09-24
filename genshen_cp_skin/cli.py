# -*- coding: utf-8 -*-
"""genshen_cp_skin.cli —— `gc` 命令行。

    gc list / show / install / wallpaper / pet / ide / deepking
    gc paths / env / doctor / mirror / uninstall / cmd

设计取向与 `gs`（Desktop-Skin）一致：命令名短、中文名可查、`gc cmd` 打印总览。
"""
import argparse
import json
import os
import sys

from . import __version__
from . import catalog as cat_mod
from . import engine, mirror, proxy, repo, targets

# ---------------------------------------------------------------------------
# 输出小工具
# ---------------------------------------------------------------------------
def _out(s=""):
    try:
        print(s)
    except UnicodeEncodeError:
        sys.stdout.write(s.encode("utf-8", "replace").decode("utf-8", "replace") + "\n")


def setup_console():
    """Windows GBK 控制台：尽量切 UTF-8，切不了也别崩。"""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def mirror_name(args):
    return getattr(args, "mirror", None) or os.environ.get("GENSHEN_MIRROR")


def resolve(key):
    pack = cat_mod.find_pack(cat_mod.load_catalog(), key)
    if not pack:
        _out("没找到 %r。用 `gc list` 看全部 %d 套。" % (key, cat_mod.load_catalog()["count"]))
        cands = cat_mod.search(cat_mod.load_catalog(), key)[:5]
        if cands:
            _out("最接近的几套：")
            for c in cands:
                _out("  %-6s %s" % (c["id"], c["name"]))
        raise SystemExit(2)
    return pack


def caps_text(pack):
    caps = pack.get("caps") or {}
    names = {"wallpaper": "壁纸", "desktop": "桌宠", "vscode": "IDE扩展", "deepking": "DeepKing"}
    return " ".join(names[k] for k in ("wallpaper", "desktop", "vscode", "deepking")
                    if caps.get(k)) or "（无）"


# ---------------------------------------------------------------------------
# list / show / catalog
# ---------------------------------------------------------------------------
def cmd_list(args):
    cat = cat_mod.load_catalog()
    want = getattr(args, "kind", None)
    _out("%s · 共 %d 套" % (cat.get("family") or "原神 CP 壁纸套件", cat["count"]))
    _out("素材（源图 + 引擎）随包自带，装完即可离线使用")
    _out("仓库: %s" % cat.get("homepage"))
    _out()
    _out("%-3s %-7s %-30s %-9s %-6s %-6s %s"
         % ("#", "ID", "套件", "主题色", "素材", "摆法", "可用环境"))
    _out("-" * 88)
    shown = 0
    for p in cat["packs"]:
        _out("%-3d %-7s %-30s %-9s %-6d %-6d %s"
             % (p["no"], p["id"], p["name"], p["accent"],
                len(p["sources"]), p["modes"], caps_text(p)))
        shown += 1
    _out()
    _out("装某套:  gc install cp24        例: gc install cp1")
    _out("按角色找: gc show 甘雨            也支持 cp24 / 24 / 拼音")
    return 0


def cmd_show(args):
    pack = resolve(args.key)
    _out(pack["name"])
    _out("  ID / 序号   : %s / 第 %d 套" % (pack["id"], pack["no"]))
    _out("  角色        : %s" % pack["char"])
    _out("  主题色      : %s" % pack["accent"])
    if pack.get("tagline"):
        _out("  标语        : %s" % pack["tagline"])
    _out("  源仓库      : %s" % pack["url"])
    _out("  可用环境    : %s" % caps_text(pack))
    _out()
    _out("  素材 %d 张（已在包内）:" % len(pack["sources"]))
    for i, s in enumerate(pack["sources"], 1):
        _out("    %d. %s" % (i, os.path.basename(s)))
    modes = cat_mod.modes_of(pack)
    _out("  摆法 %d 种:" % len(modes))
    for mid, desc in modes:
        _out("    %-9s %s" % (mid, desc))
    ext = pack.get("ext") or {}
    if ext.get("id"):
        _out("  扩展 ID     : %s  (%s)" % (ext["id"], ext.get("displayName") or ""))
    _out()
    _out("  安装:")
    _out("    gc install %s            # 一键（壁纸 + 扩展 + 桌宠）" % pack["id"])
    _out("    gc wallpaper %s single1  # 只换壁纸（指定摆法）" % pack["id"])
    _out("    gc wallpaper %s all      # 一次生成全部摆法" % pack["id"])
    _out("    gc wallpaper %s --list   # 看摆法清单" % pack["id"])
    return 0


def cmd_catalog(args):
    cat = cat_mod.load_catalog()
    if args.json:
        _out(json.dumps(cat, ensure_ascii=False, indent=2))
        return 0
    if args.md:
        _out("# %s（%d 套）" % (cat.get("family"), cat["count"]))
        _out()
        _out("| # | ID | 套件 | 角色 | 素材 | 摆法 | 主题色 | IDE扩展 | 桌宠 | DeepKing | 源仓库 |")
        _out("|---|---|---|---|---|---|---|---|---|---|---|")
        for p in cat["packs"]:
            c = p["caps"]
            _out("| %d | `%s` | %s | %s | %d | %d | `%s` | %s | %s | %s | [%s](%s) |"
                 % (p["no"], p["id"], p["name"], p["char"], len(p["sources"]),
                    p["modes"], p["accent"],
                    "✅" if c.get("vscode") else "—",
                    "✅" if c.get("desktop") else "—",
                    "✅" if c.get("deepking") else "—",
                    p["repo"], p["url"]))
        return 0
    _out("catalog: %s" % cat_mod.catalog_path())
    _out("共 %d 套，schema=%s" % (cat["count"], cat.get("schema")))
    return 0


def cmd_paths(args):
    cat = cat_mod.load_catalog()
    _out("本地根目录 : %s" % repo.home_dir())
    _out("套件目录   : %s" % os.path.join(repo.home_dir(), "<源仓库名>"))
    _out("包内素材   : %s" % repo.packs_dir())
    _out("catalog    : %s" % cat_mod.catalog_path())
    _out()
    ready = [p["id"] for p in cat["packs"] if repo.is_ready(p)]
    _out("已铺开 %d/%d 套: %s" % (len(ready), cat["count"],
                                  "、".join(ready) or "（无）"))
    return 0


# ---------------------------------------------------------------------------
# 壁纸 / 安装
# ---------------------------------------------------------------------------
MODE_ALIAS = {"1": "single1", "2": "cover1", "3": "showall1",
              "card": "single1", "cover": "cover1", "showall": "showall1",
              "single": "single1"}


def _run_engine(pack, argv, label=None):
    if label:
        _out("执行自带引擎：%s" % " ".join(argv))
        _out()
    try:
        rc = engine.run(pack, argv)
    except Exception as e:
        _out("[gc] 出错: %s" % e)
        return 1
    return rc


def cmd_wallpaper(args):
    pack = resolve(args.key)
    if args.list:
        modes = cat_mod.modes_of(pack)
        _out("%s 的摆法（%d 种）:" % (pack["name"], len(modes)))
        for mid, desc in modes:
            _out("  %-9s %s" % (mid, desc))
        _out()
        _out("用法: gc wallpaper %s <摆法|random|all>" % pack["id"])
        return 0
    mode = str(getattr(args, "mode", None) or "random")
    return _run_engine(pack, [MODE_ALIAS.get(mode.lower(), mode)])


def cmd_export(args):
    pack = resolve(args.key)
    argv = ["all"]
    if getattr(args, "out", None):
        argv += ["--out", args.out]
    if getattr(args, "size", None):
        argv += ["--size", args.size]
    return _run_engine(pack, argv)


def do_ide(pack, args, quiet=False):
    """装 VSIX。VSIX 不随包（44 MB），按需联网取一次。"""
    vsix_rel = pack.get("vsix")
    if not vsix_rel:
        if not quiet:
            _out("[gc] %s 暂未提供 VSIX 扩展，跳过 IDE 安装" % pack["char"])
        return []
    eds = targets.detect_editors()
    if getattr(args, "editor", None):
        one = targets.find_editor(args.editor)
        if not one:
            _out("[gc] 没找到编辑器 %r" % args.editor)
            return []
        eds = [one]
    if not eds:
        if not quiet:
            _out("[gc] 没检测到 VSCode / Trae / CodeX 等编辑器，跳过扩展安装")
        return []

    vsix = os.path.join(repo.skin_dir(pack["repo"]), vsix_rel)
    try:
        repo.download_to(pack, vsix_rel, vsix, quiet=quiet)
    except Exception as e:
        _out("[gc] 取 VSIX 失败（这一步需要联网）: %s" % e)
        return []

    done = []
    for ed in eds:
        ok, note = targets.install_vsix(ed, vsix, quiet=quiet)
        _out("[gc] %s: %s" % (ed["name"], note))
        if ok:
            done.append(ed["name"])
    return done


def cmd_ide(args):
    pack = resolve(args.key)
    if args.uninstall:
        ext = (pack.get("ext") or {}).get("id")
        if not ext:
            _out("[gc] %s 没有记录扩展 ID，无法自动卸载" % pack["id"])
            return 1
        done = []
        for ed in targets.installed_vsix_editors(ext):
            ok, note = targets.uninstall_vsix(ed, ext, quiet=False)
            _out("[gc] %s: %s" % (ed["name"], note))
            if ok:
                done.append(ed["name"])
        if not done:
            _out("[gc] 没找到装过 %s 的编辑器" % ext)
        return 0
    if args.list:
        eds = targets.detect_editors()
        _out("检测到 %d 个编辑器:" % len(eds))
        for e in eds:
            _out("  %-12s %s" % (e["name"], e.get("cli") or e.get("extdir") or ""))
        return 0
    return 0 if do_ide(pack, args) else 1


def cmd_pet(args):
    pack = resolve(args.key)
    if not (pack.get("caps") or {}).get("desktop"):
        _out("[gc] %s 的自带引擎没有桌宠子命令" % pack["id"])
        return 1
    if args.stop:
        return _run_engine(pack, ["pet", "--stop"])
    if args.uninstall:
        return _run_engine(pack, ["pet", "--uninstall"])
    argv = ["pet"]
    if args.autostart:
        argv.append("--autostart")
    return _run_engine(pack, argv)


def cmd_deepking(args):
    pack = resolve(args.key)
    argv = ["deepking"]
    if getattr(args, "check", False):
        argv.append("--check")
    if getattr(args, "what", False):
        argv.append("--what")
    if getattr(args, "out", None):
        argv += ["--out", args.out]
    return _run_engine(pack, argv)


def cmd_install(args):
    pack = resolve(args.key)
    _out("=== 安装 %s ===" % pack["name"])
    _out("源仓库 %s" % pack["url"])
    _out("素材已在包内，本步骤不需要联网")
    _out()

    did = []
    if not args.no_wallpaper:
        mode = MODE_ALIAS.get(str(getattr(args, "mode", None) or "random").lower(),
                             str(getattr(args, "mode", None) or "random"))
        if _run_engine(pack, [mode]) == 0:
            did.append("桌面壁纸")
    if not args.no_ide and (pack.get("caps") or {}).get("vscode"):
        if do_ide(pack, args):
            did.append("IDE 扩展")
    if not args.no_pet and (pack.get("caps") or {}).get("desktop"):
        try:
            if _run_engine(pack, ["pet"]) == 0:
                did.append("桌面桌宠")
        except Exception as e:
            _out("[gc] 桌宠启动失败: %s" % e)

    _out()
    _out("完成：%s" % ("、".join(did) if did else "没有安装任何目标（可能都被 --no-* 跳过了）"))
    _out()
    _out("后续：")
    for line in engine.install_hint(pack):
        _out("  " + line)
    return 0


def cmd_uninstall(args):
    pack = resolve(args.key)
    _out("=== 卸载 %s ===" % pack["name"])
    if not args.keep_files:
        d = repo.skin_dir(pack["repo"])
        if os.path.isdir(d):
            if repo.rmtree(d):
                _out("[gc] 已删除本地副本 %s" % d)
            else:
                _out("[gc] 未能完全删除 %s（可能被占用）" % d)
    else:
        _out("[gc] 保留本地副本（--keep-files）")
    _out()
    _out("桌宠/自启若已开启，用 `gc pet %s --uninstall` 清理。" % pack["id"])
    return 0


# ---------------------------------------------------------------------------
# 体检 / 镜像
# ---------------------------------------------------------------------------
def cmd_env(args):
    info = targets.describe_env()
    for k, v in info.items():
        _out("%-14s: %s" % (k, v))
    return 0


def cmd_doctor(args):
    _out("# gc 体检")
    _out()
    try:
        import PIL
        _out("Pillow         : %s" % getattr(PIL, "__version__", "已装"))
    except ImportError:
        _out("Pillow         : 未安装（换壁纸需要它，脚本会自动装）")
    _out("Python         : %s" % sys.version.split()[0])
    _out("本地根目录     : %s" % repo.home_dir())
    _out("包内套件       : %d 套" % len(cat_mod.load_catalog()["packs"]))
    _out()
    _out("提示：素材随包自带，装壁纸不需要网络；只有 VSIX 与吉祥物要联网取。")
    return 0


def cmd_mirror(args):
    if getattr(args, "set", None):
        name = args.set
        if name not in mirror.PIP_MIRRORS:
            _out("[gc] 未知镜像 %r，可选: %s"
                 % (name, " | ".join(mirror.PIP_MIRRORS)))
            return 2
        os.environ["GENSHEN_MIRROR"] = name
        _out("[gc] 本次会话镜像已设为 %s（%s）"
             % (name, mirror.PIP_MIRRORS[name]["name"]))
        _out("[gc] 要长期生效，请设环境变量 GENSHEN_MIRROR=%s" % name)
        return 0
    _out("PyPI 镜像（装 Pillow 时用）:")
    for name in mirror.MIRROR_ORDER:
        m = mirror.PIP_MIRRORS[name]
        _out("  %-9s %-16s %s" % (name, m["name"], m["index"]))
    _out()
    _out("GitHub 加速（取 VSIX 时按顺序尝试）:")
    for p in mirror.GITHUB_PROXIES:
        _out("  %-12s %s" % (p["name"], p.get("raw") or p.get("clone") or "直连"))
    _out()
    _out("代理：%s" % proxy.describe())
    _out("  GENSHEN_NO_PROXY=1 关闭自动探测；GENSHEN_PROXY=http://host:port 手动指定")
    return 0


COMMANDS_HELP = """原神 CP 壁纸套件合集 · 全部命令总览

用法： gc <命令> [参数]        直接敲 `gc` 就是这一页

共 24 套 CP 壁纸套件。**每套的源图与自带引擎都在包内**，
所以装壁纸全程不需要联网，也不依赖 GitHub 是否可用。

── 看目录 ─────────────────────────────────────────────────────────
  list                     列出全部 24 套与各自可用环境
  show <套件>              某套详情（素材清单 / 摆法 / 扩展 ID）
  catalog                  打印机器可读目录      --md 表格  --json 原始
  paths                    显示各类本地目录

── 装 / 卸 ─────────────────────────────────────────────────────────
  install <套件>           一键安装：桌面壁纸 + IDE 扩展 + 桌面桌宠
       --mode 1|2|3|random      指定摆法（默认 random）
       --editor vscode|trae|codex   只装到指定编辑器
       --no-wallpaper / --no-ide / --no-pet   跳过其中某一步
  uninstall <套件>         卸载本地副本（--keep-files 保留素材）

── 壁纸（每套 3~9 种摆法）───────────────────────────────────────────
  wallpaper <套件> [摆法]  换壁纸。摆法 = single1 / cover1 / showall1 …
       --list                   列出这套的全部摆法
       也接受简写：1=卡片式 2=满屏 3=完整 random=随机 all=全部生成
  export <套件> [--out 目录]     导出整屏壁纸给 PyCharm / JetBrains 当背景图

── 单平台 ──────────────────────────────────────────────────────────
  pet <套件>               桌面桌宠（--stop 停 / --autostart 开机自启 /
                           --uninstall 卸桌宠）
  ide <套件>               VSIX 扩展；--list 看编辑器 / --editor 指定 /
                           --uninstall 卸
  deepking <套件>          DeepKing 皮肤规范包（--check 校验 / --what 看提取内容）

── 诊断 / 镜像 ─────────────────────────────────────────────────────
  env                      检测本机环境（IDE / 屏幕分辨率 / 代理）
  doctor                   体检：Pillow / Python / 本地目录
  mirror [--set tuna|ustc|aliyun|tencent|official]   查看 / 设置镜像
  cmd / commands           显示本页（`help` / `?` 同效）

找某套可以用：cpN、序号、角色名、拼音、别名。
  gc show cp24        gc show 24        gc show 甘雨
  gc install cp15     gc show 温迪       gc show ganyu

常用示例
  gc list
  gc install cp24
  gc show 甘雨
  gc wallpaper cp24 cover1
  gc wallpaper cp7 all
  gc pet cp24
  gc uninstall cp24

等价写法（随便挑一种）
  gc list
  python -m genshen_cp_skin list
  python -m genshen-cp-skin list

文档： https://github.com/WPH666-py/Genshen-CP-Skin
"""


def cmd_commands(args):
    _out(COMMANDS_HELP.rstrip())
    return 0


# ---------------------------------------------------------------------------
# parser
# ---------------------------------------------------------------------------
def build_parser():
    ap = argparse.ArgumentParser(
        prog="gc",
        description="原神 CP 壁纸套件合集（24 套）：素材随包自带，离线可用",
        epilog="更多用法见 https://github.com/WPH666-py/Genshen-CP-Skin",
    )
    ap.add_argument("-V", "--version", action="version",
                    version="genshen-cp-skin %s" % __version__)
    ap.add_argument("--mirror", default=None,
                    help="pip 镜像: tuna(清华,默认) | ustc | aliyun | tencent | official")
    sub = ap.add_subparsers(dest="cmd")

    p = sub.add_parser("commands", aliases=["cmd", "help", "?"],
                       help="显示全部命令总览（直接敲 gc 同效）")
    p.set_defaults(func=cmd_commands)

    p = sub.add_parser("list", help="列出全部 24 套")
    p.add_argument("--kind", default=None, help="预留：本包只有 CP 一族")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show", help="查看某套的详情")
    p.add_argument("key")
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("catalog", help="打印机器可读目录")
    p.add_argument("--json", action="store_true")
    p.add_argument("--md", action="store_true")
    p.set_defaults(func=cmd_catalog)

    sub.add_parser("paths", help="显示各类本地目录").set_defaults(func=cmd_paths)
    sub.add_parser("env", help="检测本机环境").set_defaults(func=cmd_env)
    sub.add_parser("doctor", help="体检：Pillow / Python / 目录").set_defaults(func=cmd_doctor)

    p = sub.add_parser("install", help="一键安装（壁纸 + IDE 扩展 + 桌宠）")
    p.add_argument("key")
    p.add_argument("--mode", default="random", help="摆法：1|2|3|random 或 single1/cover1/…")
    p.add_argument("--editor", default=None)
    p.add_argument("--no-wallpaper", action="store_true")
    p.add_argument("--no-ide", action="store_true")
    p.add_argument("--no-pet", action="store_true")
    p.set_defaults(func=cmd_install)

    p = sub.add_parser("wallpaper", help="切换桌面壁纸")
    p.add_argument("key")
    p.add_argument("mode", nargs="?", default=None)
    p.add_argument("--list", action="store_true")
    p.set_defaults(func=cmd_wallpaper)

    p = sub.add_parser("export", help="导出整屏壁纸（PyCharm 背景图）")
    p.add_argument("key")
    p.add_argument("--out", default=None)
    p.add_argument("--size", default=None)
    p.set_defaults(func=cmd_export)

    p = sub.add_parser("pet", help="桌面桌宠")
    p.add_argument("key")
    p.add_argument("--stop", action="store_true")
    p.add_argument("--autostart", action="store_true")
    p.add_argument("--uninstall", action="store_true")
    p.set_defaults(func=cmd_pet)

    p = sub.add_parser("ide", help="安装 VSIX 扩展")
    p.add_argument("key")
    p.add_argument("--list", action="store_true")
    p.add_argument("--editor", default=None)
    p.add_argument("--uninstall", action="store_true")
    p.set_defaults(func=cmd_ide)

    p = sub.add_parser("deepking", help="导出 DeepKing 皮肤规范包")
    p.add_argument("key")
    p.add_argument("--check", action="store_true")
    p.add_argument("--what", action="store_true")
    p.add_argument("--out", default=None)
    p.set_defaults(func=cmd_deepking)

    p = sub.add_parser("uninstall", help="卸载本地副本")
    p.add_argument("key")
    p.add_argument("--keep-files", action="store_true")
    p.set_defaults(func=cmd_uninstall)

    p = sub.add_parser("mirror", help="查看 / 设置镜像")
    p.add_argument("--set", default=None)
    p.set_defaults(func=cmd_mirror)

    return ap


def main(argv=None):
    setup_console()
    ap = build_parser()
    args = ap.parse_args(argv)
    if not getattr(args, "func", None):
        return cmd_commands(args)
    try:
        return args.func(args)
    except SystemExit:
        raise
    except KeyboardInterrupt:
        _out("\n[gc] 已中断")
        return 130
    except Exception as e:
        _out("[gc] 出错: %s" % e)
        if os.environ.get("GC_DEBUG"):
            import traceback
            traceback.print_exc()
        return 1
