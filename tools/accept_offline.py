# -*- coding: utf-8 -*-
"""最终验收：全新 venv 里跑 `gc` 全链路（离线）。

只验证真正会被用户执行的入口：`gc` 可执行文件本身。
"""
import os
import re
import subprocess
import sys

VENV = r"D:\projects-py\Genshen-skins\_venv_gc"
GC = os.path.join(VENV, "Scripts", "gc.exe")
HOME = r"D:\projects-py\Genshen-skins\_gc_home_accept"

FAIL = []


def run(args, expect=0, label=None):
    label = label or " ".join(args)
    env = dict(os.environ)
    env["GENSHEN_CP_HOME"] = HOME
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    env["GENSHEN_NO_PROXY"] = "1"
    r = subprocess.run([GC] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env, timeout=900)
    ok = (r.returncode == expect)
    print("  [%s] %-44s rc=%s" % ("OK " if ok else "FAIL", label, r.returncode))
    if not ok:
        FAIL.append(label)
        for line in (r.stdout or "").splitlines()[-6:]:
            print("        " + line)
        for line in (r.stderr or "").splitlines()[-6:]:
            print("        E " + line)
    return (r.stdout or "") + (r.stderr or "")


def rows(out):
    ids = []
    for line in out.splitlines():
        m = re.match(r"^\s*(\d+)\s+(cp\d+)\s", line)
        if m:
            ids.append(m.group(2))
    return ids


def main():
    print("GENSHEN_CP_HOME = %s\n" % HOME)
    print("=== 1. 目录 ===")
    out = run(["list"], label="gc list")
    ids = rows(out)
    print("        表格行数: %d" % len(ids))
    if len(ids) != 24:
        FAIL.append("list 行数 != 24")
    if "共 24 套" not in out:
        FAIL.append("list 总数说明缺失")

    print("\n=== 2. 详情与检索 ===")
    for key, want in (("cp24", "Genshen-skin-CP24"),
                      ("24", "第 24 套"),
                      ("甘雨", "cp15"),
                      ("ganyu", "cp15"),
                      ("cp1", "Genshen-Skin-CP1")):
        out = run(["show", key], label="gc show %s" % key)
        if want not in out:
            FAIL.append("show %s 输出缺少 %r" % (key, want))

    print("\n=== 3. 换壁纸（离线）===")
    run(["wallpaper", "cp24", "cover1"], label="gc wallpaper cp24 cover1")
    out = run(["wallpaper", "cp24", "--list"], label="gc wallpaper cp24 --list")
    if "single1" not in out or "showall1" not in out:
        FAIL.append("cp24 摆法清单不完整")

    print("\n=== 4. 一键安装（跳过联网的 IDE 步骤）===")
    run(["install", "cp15", "--mode", "2", "--no-ide", "--no-pet"],
        label="gc install cp15 --no-ide --no-pet")

    print("\n=== 5. 导出 ===")
    outp = os.path.join(HOME, "exports")
    run(["export", "cp7", "--out", outp], label="gc export cp7")

    print("\n=== 6. 命令总览与诊断 ===")
    out = run(["cmd"], label="gc cmd")
    for key in ("gc install cp24", "gc wallpaper cp24", "gc list"):
        if key not in out:
            FAIL.append("总览缺少 %r" % key)
    run(["paths"], label="gc paths")
    run(["doctor"], label="gc doctor")

    print("\n=== 7. 卸载 ===")
    run(["uninstall", "cp24"], label="gc uninstall cp24")

    print()
    if FAIL:
        print("失败项 %d：" % len(FAIL))
        for f in FAIL:
            print("  " + f)
        return 1
    print("VERDICT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
