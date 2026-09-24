#!/usr/bin/env bash
# 原神 CP 壁纸套件 1 · 米提亚 x 沃雅妮莎 —— 安装器 (macOS / Linux)
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
echo "  原神 CP 壁纸套件 1 · 米提亚 x 沃雅妮莎"
echo "============================================================"
echo

if "$PY" -c "import genshin_skin_cp1" >/dev/null 2>&1; then
  echo "[1/2] 已检测到 genshin-skin-cp1, 跳过安装。"
else
  echo "[1/2] 正在安装 genshin-skin-cp1 ... (国内网络会自动回退到清华源)"
  if ! "$PY" -m pip install --quiet --disable-pip-version-check genshin-skin-cp1; then
    echo "      官方源失败, 改用清华镜像 ..."
    "$PY" -m pip install --quiet --disable-pip-version-check genshin-skin-cp1 \
      -i https://pypi.tuna.tsinghua.edu.cn/simple || true
  fi
fi

echo "[2/2] 正在安装壁纸与 IDE 集成 ..."
if "$PY" -c "import genshin_skin_cp1" >/dev/null 2>&1; then
  "$PY" -m genshin_skin_cp1.autoinstall
else
  echo "      pip 安装未成功, 改用仓库源码模式运行 ..."
  PYTHONPATH="$(pwd)/src" "$PY" -m genshin_skin_cp1.autoinstall
fi

echo
echo "============================================================"
echo "  安装结束。常用命令:"
echo "    genshin-cp1 2          换成第 2 张(共舞)"
echo "    genshin-cp1 random     随机换一张"
echo "    genshin-cp1 switcher   可视化切换器"
echo "    genshin-cp1 pet        桌面桌宠"
echo "============================================================"
