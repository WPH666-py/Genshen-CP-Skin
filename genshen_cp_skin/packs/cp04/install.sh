#!/usr/bin/env bash
# 原神 CP 壁纸套件 4 · 柯莱 x 安柏 —— 安装器 (macOS / Linux)
set -e
cd "$(dirname "$0")"

PY=python3
command -v python3 >/dev/null 2>&1 || PY=python
if ! command -v "$PY" >/dev/null 2>&1; then
  echo "[错误] 未找到 Python 3, 请先安装:"
  echo "  macOS        : brew install python"
  echo "  Ubuntu/Debian: sudo apt install -y python3 python3-pil"
  exit 1
fi

echo "============================================================"
echo "  原神 CP 壁纸套件 4 · 柯莱 x 安柏"
echo "============================================================"
echo

if "$PY" -c "import genshen_skin_cp4" >/dev/null 2>&1; then
  echo "[1/2] 已检测到 genshen-skin-cp4"
  RUN=("$PY" -m genshen_skin_cp4.engine.autoinstall)
else
  echo "[1/2] 以仓库源码方式运行(无需预先 pip 安装)"
  RUN=(env PYTHONPATH="$(pwd)/src" "$PY" -m genshen_skin_cp4.engine.autoinstall)
fi

echo "[2/2] 正在安装壁纸与 IDE 集成 ..."
"${RUN[@]}"

echo
echo "============================================================"
echo "  安装结束。常用命令(源码方式请把 genshen-cp4 换成"
echo "  python -m genshen_skin_cp4.engine.cli):"
echo "    genshen-cp4 2          换成第 2 张(星轨)"
echo "    genshen-cp4 random     随机换一张"
echo "    genshen-cp4 switcher   可视化切换器"
echo "    genshen-cp4 pet        桌面桌宠"
echo "    genshen-cp4 deepking   DeepKing 界面皮肤"
echo "============================================================"
