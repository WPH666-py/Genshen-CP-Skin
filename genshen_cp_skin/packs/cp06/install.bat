@echo off
chcp 65001 >nul
title 原神CP6 壁纸套件 · 玛拉妮 x 基尼奇 x 卡其娜 — 安装器
setlocal

echo ============================================================
echo   原神 CP 壁纸套件 6 · 玛拉妮 x 基尼奇 x 卡其娜
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
  echo   或到 https://www.python.org/downloads/ 下载安装^(勾选 Add to PATH^)
  echo.
  pause
  exit /b 1
)

rem ---- 已 pip 安装过就直接用命令, 否则走仓库源码 ----
%PY% -c "import genshen_skin_cp6" >nul 2>nul
if errorlevel 1 (
  echo [1/2] 以仓库源码方式运行^(无需预先 pip 安装^)
  set PYTHONPATH=%~dp0src
) else (
  echo [1/2] 已检测到 genshen-skin-cp6
)

echo [2/2] 正在安装壁纸与 IDE 集成 ...
%PY% -m genshen_skin_cp6.engine.autoinstall

echo.
echo ============================================================
echo   安装结束。常用命令^(源码方式请把 genshen-cp6 换成
echo   python -m genshen_skin_cp6.engine.cli^):
echo     genshen-cp6 2          换成第 2 张(星轨)
echo     genshen-cp6 random     随机换一张
echo     genshen-cp6 switcher   可视化切换器
echo     genshen-cp6 pet        桌面桌宠
echo     genshen-cp6 deepking   DeepKing 界面皮肤
echo ============================================================
pause
