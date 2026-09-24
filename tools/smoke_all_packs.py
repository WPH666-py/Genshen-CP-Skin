# -*- coding: utf-8 -*-
"""离线冒烟：让每一套都真的合成一次壁纸（只合成，不设置系统壁纸）。

这是"包自带素材可用"的最终判据 —— 目录铺开只是前提，出图才算数。
用各套引擎都支持的 `copy` 子命令（只合成不设置），避免反复改系统壁纸。

注意：各套的运行时目录名不统一（历史遗留）：
    cp1  -> ~/.genshin-cp1      （genshin）
    cp24 -> ~/.genshen-cp24     （genshen）
所以这里不猜目录名，改成"跑之前记下 ~ 下所有 .genshen*-cp* 目录的快照，跑完比对新出现的文件"。
"""
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

from genshen_cp_skin import catalog as cat_mod      # noqa: E402
from genshen_cp_skin import engine, repo            # noqa: E402

HOME = os.environ.get("GENSHEN_CP_HOME") or repo.home_dir()
os.environ["GENSHEN_CP_HOME"] = HOME
USERHOME = os.path.expanduser("~")


def snapshot():
    """~ 下所有 .genshen*-cp* 目录里的 jpg 快照。"""
    out = set()
    try:
        names = os.listdir(USERHOME)
    except OSError:
        return out
    for n in names:
        low = n.lower()
        if not low.startswith(".gensh") or "-cp" not in low:
            continue
        wp = os.path.join(USERHOME, n, "wallpapers")
        if not os.path.isdir(wp):
            continue
        try:
            for f in os.listdir(wp):
                if f.endswith(".jpg"):
                    out.add((n, f))
        except OSError:
            pass
    return out


def main():
    cat = cat_mod.load_catalog()
    print("GENSHEN_CP_HOME = %s" % HOME)
    print("离线冒烟：%d 套（只合成，不设置系统壁纸）\n" % cat["count"])
    ok = []
    bad = []
    for p in cat["packs"]:
        before = snapshot()
        try:
            rc = engine.run(p, ["copy", "--size", "1920x1080"])
        except Exception as e:
            bad.append((p["id"], "异常: %s" % e))
            print("  FAIL %-5s 异常: %s" % (p["id"], e))
            continue
        after = snapshot()
        new = sorted(after - before)
        mine = sorted(f for (d, f) in after if d.lower().endswith("-cp%d" % p["cp"]))
        expect = p["modes"]
        if rc == 0 and len(mine) >= expect:
            ok.append(p["id"])
            print("  OK   %-5s rc=%s 产出 %2d 张（期望 %d）%s"
                  % (p["id"], rc, len(mine), expect,
                     ("  新增 " + ", ".join(f for _d, f in new[:2])) if new else ""))
        else:
            bad.append((p["id"], "rc=%s 产出 %d/%d" % (rc, len(mine), expect)))
            print("  FAIL %-5s rc=%s 产出 %d 张（期望 %d）"
                  % (p["id"], rc, len(mine), expect))

    print()
    print("成功 %d / 失败 %d" % (len(ok), len(bad)))
    for pid, why in bad:
        print("  %s: %s" % (pid, why))
    print()
    print("VERDICT:", "PASS" if not bad else "FAIL")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
