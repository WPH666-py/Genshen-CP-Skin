@echo off
chcp 65001 >nul
title 原神CP壁纸套件1 · 米提亚 x 沃雅妮莎 — 安装器
setlocal

echo ============================================================
echo   原神 CP 壁纸套件 1 · 米提亚 x 沃雅妮莎
echo ============================================================
echo.

rem ---- 找 Python ----
set PY=
where python >nul 2>nul && set PY=python
if "%PY%"=="" (
  where py >nul 2>nul && set PY=py -3
)
if "%PY%"=="" (
  echo [错误] 未找到 Python 3。
  echo   请先安装: winget install Python.Python.3.11
  echo   或到 https://www.python.org/downloads/ 下载安装(勾选 Add to PATH^)
  echo.
  pause
  exit /b 1
)

rem ---- 确保 pip 包已装(提供 genshin-cp1 命令) ----
%PY% -c "import genshin_skin_cp1" >nul 2>nul
if errorlevel 1 (
  echo [1/2] 正在安装 genshin-skin-cp1 ... ^(国内网络会自动回退到清华源^)
  %PY% -m pip install --quiet --disable-pip-version-check genshin-skin-cp1
  if errorlevel 1 (
    echo       官方源失败, 改用清华镜像 ...
    %PY% -m pip install --quiet --disable-pip-version-check genshin-skin-cp1 -i https://pypi.tuna.tsinghua.edu.cn/simple
  )
) else (
  echo [1/2] 已检测到 genshin-skin-cp1, 跳过安装。
)

rem ---- 一键安装: 生成壁纸 + 设为桌面 + 注册 IDE ----
echo [2/2] 正在安装壁纸与 IDE 集成 ...
%PY% -c "import genshin_skin_cp1" >nul 2>nul
if errorlevel 1 (
  echo.
  echo [提示] pip 安装未成功, 改用仓库源码模式运行 ...
  set PYTHONPATH=%~dp0src
  %PY% -m genshin_skin_cp1.autoinstall
) else (
  %PY% -m genshin_skin_cp1.autoinstall
)

echo.
echo ============================================================
echo   安装结束。常用命令:
echo     genshin-cp1 2          换成第 2 张(共舞)
echo     genshin-cp1 random     随机换一张
echo     genshin-cp1 switcher   可视化切换器
echo     genshin-cp1 pet        桌面桌宠
echo ============================================================
pause
