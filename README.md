# 🎴 原神 CP 壁纸套件合集 · Genshen CP Skin

**24 套原神 CP 壁纸，一个安装包全部带走。每套的源图与自带引擎都在包内，
装完即可离线使用 —— 不需要 git，也不需要访问 GitHub。**

把本仓库地址交给任意一个有本机权限的 AI 助手（DeepSeek Harness / claude-code /
kimi-code / CodeX / Trae / Cursor 等），说一句「装 CP24 壁纸」，AI 就会读
[AGENTS.md](AGENTS.md) 自动装好。

```text
请安装 https://github.com/WPH666-py/Genshen-CP-Skin 的 cp24 壁纸
```

支持 **VSCode · Trae · CodeX · Cursor · Windsurf · VSCodium**
· **PyCharm / IntelliJ / WebStorm**（背景图）· **Windows 桌面桌宠**
· **claude-code / kimi-code / Harness**（MCP + DSH）。

> 素材版权归米哈游（miHoYo / HoYoverse），仅供个人学习娱乐，请勿商用。

---

## 为什么是「一个包」而不是「24 个仓库」

CP 系列原先是一套一个仓库（`Genshen-skin-CP1` … `CP24`）。那样每装一套都要：

1. 从 GitHub 拉整个仓库（国内 raw 经常不通，要靠加速通道回退）
2. 装完才第一次能用

现在改成安装包自带素材：

| | 一套一仓库（旧） | 本包（新） |
|---|---|---|
| 取素材 | 每次联网拉仓库 | **包内自带，零网络** |
| 需要 git | 是 | **否** |
| 装第二套 | 再拉一次 | **已在包里，秒装** |
| 体积 | 各自 3~10 MB | 整包 23 MB（含 24 套） |
| 换壁纸 | 引擎现算 | 引擎现算（**按你的屏幕分辨率**） |

包内只带**必需**的东西（源图 + 引擎代码，共 23 MB）。
VSIX 扩展（44 MB）、吉祥物、缩略图这类可选件仍按需联网取一次，取到即缓存。

**24 个源仓库仍然保留**（`Genshen-skin-CP1` … `CP24`），它们是素材与版权的原始出处，
也是可选件的上游。本包不取代它们，只是让安装这件事变得离线可用。

---

## 安装

### ① pip 一条命令（推荐）

```powershell
py -3 -m pip install genshen-cp-skin

gc list               # 看全部 24 套
gc install cp24       # 一键：壁纸 + IDE 扩展 + 桌宠
gc cmd                # 全部命令总览（或直接敲 gc）
```

> **macOS / Linux 把 `py -3` 换成 `python3`**，其余完全一样。
> `gc` 不在 PATH 里时用 `py -3 -m genshen_cp_skin <命令>`。

**国内网络装不上 pip 包时**改用镜像：

```powershell
py -3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple genshen-cp-skin   # 清华
py -3 -m pip install -i https://mirrors.ustc.edu.cn/pypi/simple genshen-cp-skin    # 中科大
py -3 -m pip install -i https://mirrors.aliyun.com/pypi/simple genshen-cp-skin     # 阿里云
```

### ② 给 AI 一句话

见顶部示例。AI 读 `AGENTS.md` 与 `catalog.json`，自己识别环境并装好。

### ③ 手动（不装 pip 包）

```bash
git clone https://github.com/WPH666-py/Genshen-CP-Skin
cd Genshen-CP-Skin
py -3 -m pip install -e .
gc list
```

---

## 命令

| 命令 | 作用 |
|---|---|
| `gc list` | 列出全部 24 套与各自可用环境 |
| `gc show <套件>` | 某套详情（素材清单 / 摆法 / 扩展 ID / 安装方式） |
| `gc install <套件>` | 一键安装：桌面壁纸 + IDE 扩展 + 桌宠 |
| `gc install <套件> --mode 2` | 指定摆法（默认 `random`） |
| `gc install <套件> --no-ide --no-pet` | 只换壁纸 |
| `gc wallpaper <套件> [摆法]` | 换壁纸；`--list` 看这套有哪些摆法 |
| `gc wallpaper <套件> all` | 一次生成全部摆法 |
| `gc wallpaper <套件> random` | 随机换一种 |
| `gc export <套件> --out 目录` | 导出整屏壁纸（PyCharm 背景图用） |
| `gc pet <套件>` | 桌面桌宠；`--stop` / `--autostart` / `--uninstall` |
| `gc ide <套件>` | 装 VSIX 扩展；`--list` 看编辑器 / `--uninstall` 卸 |
| `gc deepking <套件>` | DeepKing 皮肤规范包；`--check` 校验 / `--what` 看提取内容 |
| `gc uninstall <套件>` | 卸载本地副本（`--keep-files` 保留素材） |
| `gc env` / `gc doctor` / `gc paths` | 环境 / 体检 / 本地目录 |
| `gc mirror` | 查看 / 设置 pip 镜像与 GitHub 加速通道 |
| `gc cmd` | 全部命令总览（`gc` / `gc help` / `gc ?` 同效） |

找某套皮肤，四种写法都行：

```powershell
gc show cp24      # 编号
gc show 24        # 序号
gc show 甘雨       # 角色名
gc show ganyu     # 拼音
```

---

## 三种摆法是什么

每张素材都能摆成三种样子，**按你的屏幕分辨率实时合成**：

| 摆法 | 说明 |
|---|---|
| `single1` | **卡片式（默认）**：模糊填充背景 + 居中圆角卡片，构图完整不裁切 |
| `cover1` | **满屏**：cover 铺满整屏，无边框 |
| `showall1` | **完整**：等比放进同色纯色底，一个像素都不裁，两侧留边 |

编号对应素材张数：3 张素材的套件有 `single1/2/3`、`cover1/2/3`、`showall1/2/3`。

> 摆法数量以**各套引擎自报**为准（`gc wallpaper <套件> --list`）。
> 例如 `cp1` 只有 `single` 与 `cover` 两族（6 种，没有 `showall`），
> 大部分单图套件是 3 种，三图套件是 9 种。

---

## 套件目录（24 套）

| # | ID | 套件 | 素材 | 摆法 | 主题色 | 源仓库 |
|---|---|---|---|---|---|---|
| 1 | `cp1` | 原神CP1 · 米提亚×沃雅妮莎 | 3 张 | 6 种 | `#3f8fd8` | [Genshen-Skin-CP1](https://github.com/WPH666-py/Genshen-Skin-CP1) |
| 2 | `cp2` | 原神CP2 · 奥黛塔×沃雅妮莎 | 1 张 | 3 种 | `#3a6fd8` | [Genshen-skin-CP2](https://github.com/WPH666-py/Genshen-skin-CP2) |
| 3 | `cp3` | 原神CP3 · 米提亚×奥黛塔×沃雅妮莎 | 1 张 | 3 种 | `#2f9e8f` | [Genshen-skin-CP3](https://github.com/WPH666-py/Genshen-skin-CP3) |
| 4 | `cp4` | 原神CP4 · 柯莱×安柏 | 1 张 | 3 种 | `#4f9e4a` | [Genshen-skin-CP4](https://github.com/WPH666-py/Genshen-skin-CP4) |
| 5 | `cp5` | 原神CP5 · 桑多涅×哥伦比娅 | 3 张 | 9 种 | `#a8326e` | [Genshen-skin-CP5](https://github.com/WPH666-py/Genshen-skin-CP5) |
| 6 | `cp6` | 原神CP6 · 玛拉妮×基尼奇×卡其娜 | 2 张 | 6 种 | `#2e9ec4` | [Genshen-skin-CP6](https://github.com/WPH666-py/Genshen-skin-CP6) |
| 7 | `cp7` | 原神CP7 · 娜维娅×克洛琳德 | 3 张 | 9 种 | `#b8863f` | [Genshen-skin-CP7](https://github.com/WPH666-py/Genshen-skin-CP7) |
| 8 | `cp8` | 原神CP8 · 胡桃×芙宁娜 | 3 张 | 9 种 | `#c8433a` | [Genshen-skin-CP8](https://github.com/WPH666-py/Genshen-skin-CP8) |
| 9 | `cp9` | 原神CP9 · 神里绫华×宵宫 | 2 张 | 6 种 | `#e8734a` | [Genshen-skin-CP9](https://github.com/WPH666-py/Genshen-skin-CP9) |
| 10 | `cp10` | 原神CP10 · 雷电影×八重神子 | 3 张 | 9 种 | `#8a5fb0` | [Genshen-skin-CP10](https://github.com/WPH666-py/Genshen-skin-CP10) |
| 11 | `cp11` | 原神CP11 · 胡桃×香菱 | 3 张 | 9 种 | `#b8352f` | [Genshen-skin-CP11](https://github.com/WPH666-py/Genshen-skin-CP11) |
| 12 | `cp12` | 原神CP12 · 行秋×重云 | 3 张 | 9 种 | `#2f6bab` | [Genshen-skin-CP12](https://github.com/WPH666-py/Genshen-skin-CP12) |
| 13 | `cp13` | 原神CP13 · 钟离×凝光 | 1 张 | 3 种 | `#c9a43f` | [Genshen-skin-CP13](https://github.com/WPH666-py/Genshen-skin-CP13) |
| 14 | `cp14` | 原神CP14 · 神里绫华×优菈×甘雨 | 1 张 | 3 种 | `#7ba7cc` | [Genshen-skin-CP14](https://github.com/WPH666-py/Genshen-skin-CP14) |
| 15 | `cp15` | 原神CP15 · 甘雨×刻晴 | 3 张 | 9 种 | `#8fbde0` | [Genshen-skin-CP15](https://github.com/WPH666-py/Genshen-skin-CP15) |
| 16 | `cp16` | 原神CP16 · 温迪×芭芭拉 | 1 张 | 3 种 | `#c9a227` | [Genshen-skin-CP16](https://github.com/WPH666-py/Genshen-skin-CP16) |
| 17 | `cp17` | 原神CP17 · 奥黛塔×沃雅妮莎×米提亚×阿罗夏 | 1 张 | 3 种 | `#6b79ad` | [Genshen-skin-CP17](https://github.com/WPH666-py/Genshen-skin-CP17) |
| 18 | `cp18` | 原神CP18 · 散兵×万叶 | 3 张 | 9 种 | `#3d3a6b` | [Genshen-skin-CP18](https://github.com/WPH666-py/Genshen-skin-CP18) |
| 19 | `cp19` | 原神CP19 · 空×荧 | 3 张 | 9 种 | `#c9a44a` | [Genshen-skin-CP19](https://github.com/WPH666-py/Genshen-skin-CP19) |
| 20 | `cp20` | 原神CP20 · 散兵×荧 | 3 张 | 9 种 | `#3f3c63` | [Genshen-skin-CP20](https://github.com/WPH666-py/Genshen-skin-CP20) |
| 21 | `cp21` | 原神CP21 · 魈×荧 | 3 张 | 9 种 | `#3f7d78` | [Genshen-skin-CP21](https://github.com/WPH666-py/Genshen-skin-CP21) |
| 22 | `cp22` | 原神CP22 · 荧×达达利亚 | 1 张 | 3 种 | `#5c78b0` | [Genshen-skin-CP22](https://github.com/WPH666-py/Genshen-skin-CP22) |
| 23 | `cp23` | 原神CP23 · 荧×诺艾尔 | 1 张 | 3 种 | `#b03a35` | [Genshen-skin-CP23](https://github.com/WPH666-py/Genshen-skin-CP23) |
| 24 | `cp24` | 原神CP24 · 甘雨×绫华 | 1 张 | 3 种 | `#b62230` | [Genshen-skin-CP24](https://github.com/WPH666-py/Genshen-skin-CP24) |

完整机器可读目录见 [genshen_cp_skin/catalog.json](genshen_cp_skin/catalog.json)。

---

## 本地文件都在哪

| 内容 | 位置 |
|---|---|
| 铺开的套件（含自带引擎） | `~/.genshen-cp-skin/<源仓库名>/` |
| 合成的壁纸 | `~/.genshen-cp<NN>/wallpapers/`（由各套引擎决定） |
| 包内素材（只读） | `<site-packages>/genshen_cp_skin/packs/` |

`GENSHEN_CP_HOME` 可改本地根目录。安装过程不改动你已有的文件，也不写进你的项目目录。

---

## 已知边界（如实说明）

- **摆法数量各套不同**：以 `gc wallpaper <套件> --list` 为准，本 README 的表也是实测值。
- **换壁纸需要 Pillow**：首次用到时自动 `pip install pillow`。真离线环境下需先自行装好。
- **VSIX 与吉祥物需要联网取一次**：包内不带（VSIX 共 44 MB），取到后缓存。
- **运行时目录名不统一**：`cp1` 用 `~/.genshin-cp1`，其余用 `~/.genshen-cp24` 这类拼写
  —— 这是各源仓库的历史遗留，本包如实沿用，不擅自改名（改了会让老用户的缓存失效）。
- **桌宠仅 Windows**；壁纸合成与设置跨平台（macOS 走 AppleScript，Linux 走 gsettings/xfce/feh）。
- **素材版权**：归米哈游（miHoYo / HoYoverse），**不得商用**。部分素材带作者水印，
  各源仓库的 `README.md` / `版权说明` 里写明了保留原因。

---

## 版权

本安装器与文档以 [MIT](LICENSE) 发布。

立绘、壁纸等素材版权归**米哈游（miHoYo / HoYoverse）**，仅供个人学习与娱乐使用，
**不得用于商业用途**，不在 MIT 许可范围内。
