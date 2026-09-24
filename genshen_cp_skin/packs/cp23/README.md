# 💙 原神 CP 壁纸套件 23 · 荧 × 诺艾尔

**单张素材 × 三种摆法 = 3 种壁纸**一键切换 / 可视化切换器 / 桌面桌宠 /
多 IDE 皮肤 / DeepKing 界面皮肤。素材内置于发行包, **离线可用**;
跨平台 Windows / macOS / Linux。

![样式总览](vscode/media/thumb-grid.png)

## ✨ 素材

**「拥抱」** —— 暖光中的拥抱: 荧从背后环住诺艾尔, 两人脸贴着脸笑;
诺艾尔银发配绿瞳、鬓边红玫瑰与女仆头饰, 荧金发别着蓝色缎带,
背景是柔粉花束与暖白窗光。

原图 2560×1759(ar 1.4554)。

> 两人的脸位于**画面上部**, 因此满屏取景窗是**贴顶**的(源 y 0..1440)——
> 这样才保住头部, 只裁掉画面下方。实测两人面部、诺艾尔的红玫瑰与
> 荧的蓝色缎带都完整。

## ✨ 三种摆法

| 模式 id | 名称 | 效果 | 适合 |
|---|---|---|---|
| `single1` | **卡片式**(默认) | 模糊填充背景 + 居中圆角卡片, 构图完整不裁切 | 通用; 图标不被压住 |
| `cover1` | 满屏 | cover 铺满整屏, 无边框 | 想要沉浸感, 无边框 |
| `showall1` | 完整 | 等比放进同色纯色底, **一个像素都不裁** | 一点画面都不想丢 |

## 🚀 给 AI 一句话安装

把本仓库链接发给**任意 AI**(DeepKing、Claude Code、Kimi Code、CodeX、Trae、Cursor、
JetBrains AI、DSH Harness 等), 它会读 [`AGENTS.md`](AGENTS.md) 替你装完:

```text
请安装 https://github.com/WPH666-py/Genshen-skin-CP23 的原神CP23壁纸
```

## 🖥️ 手动安装

要求: Python 3.9+。Pillow 缺失时脚本会自动 `pip install`。

```bash
# 方式一: 用仓库里已打包好的 wheel(离线可用)
pip install dist/genshen_skin_cp23-0.1.0-py3-none-any.whl
genshen-cp23-install         # 一键: 生成壁纸 + 设为桌面 + 注册已装 IDE

# 方式二: 源码
git clone https://github.com/WPH666-py/Genshen-skin-CP23.git
cd Genshen-skin-CP23
python -m genshen_skin_cp23.engine.autoinstall
```

Windows 用户也可以直接双击 `install.bat`。

## 🎨 常用命令

```bash
genshen-cp23               # 卡片式(默认)
genshen-cp23 card          # 同上, 显式指定
genshen-cp23 cover         # 满屏
genshen-cp23 showall       # 完整不裁
genshen-cp23 random        # 随机一种摆法
genshen-cp23 list          # 列出全部 3 种模式
genshen-cp23 switcher      # 可视化切换器(预览 + 一键应用 + 自动随机)
genshen-cp23 pet           # 桌面桌宠(拖动 / 右键菜单 / Esc 退出)
genshen-cp23 cycle 30      # 每 30 分钟自动随机换
genshen-cp23 all --out DIR # 一次生成 3 张到指定目录
genshen-cp23 deepking      # 生成 DeepKing 界面皮肤 + 离线预览
genshen-cp23 info          # 环境与素材自检
```

常用选项: `--size 2560x1440` 指定分辨率(默认取屏幕分辨率)、`--no-set` 只生成不设置。

## 🧩 IDE / 桌宠支持

| 环境 | 接入方式 |
|---|---|
| **VSCode / Trae / CodeX / Cursor / Windsurf** | 活动栏「原神CP23」→ 皮肤画廊 3 张卡片一键换; 命令面板搜 `原神CP23` |
| **DeepKing** | 设置 → 界面皮肤 → 粘贴本仓库地址, 自动生成玫红配色皮肤 |
| **PyCharm / WebStorm / IntelliJ** | Settings → Appearance & Behavior → Appearance → **Background Image** |
| **Claude Code / Kimi Code / Harness 等** | 注册 MCP 服务器, AI 直接调 `set_wallpaper` / `next_wallpaper` |
| **桌面桌宠** | `genshen-cp23 pet` —— 透明置顶圆形立绘, 可拖动、右键菜单 |

一键注册全部已装 IDE:

```bash
genshen-cp23-install --only vscode jetbrains mcp deepking
```

## 📁 目录

```
src/genshen_skin_cp23/
  characters/cp23_pair.py   角色与素材定义(换角色只改这一个文件)
  engine/                   皮肤引擎: 合成 / 壁纸设置 / CLI / 桌宠 / 切换器 /
                            MCP 服务器 / DeepKing 适配 / 自动安装
  deepking_skin.py          手工校色的 DeepKing 调色板(32 槽位)
src/client/                 DeepKing 配色变量 + 维护说明
vscode/                     VSCode/Trae/CodeX 扩展(含打包好的 .vsix)
ide/jetbrains/              JetBrains 背景图指引
tools/                      维护脚本(推送 / 引擎同步 / 线上契约校验)
AGENTS.md                   给 AI 的自动安装指引
```

## ❓ 常见问题

- **想换图**: 把图放进 `src/genshen_skin_cp23/engine/assets/`, 在
  `characters/cp23_pair.py` 的 `IMAGE_FILES` / `IMAGE_NAMES` / `IMAGE_META` 里改一处
  —— 模式列表会自动跟着变(单张是 3 种, 三张就是 9 种)。
- **壁纸尺寸**: 默认取主屏分辨率; 多显示器建议加 `--size 2560x1440`。
- **命令找不到**: Scripts 目录不在 PATH, 改用 `python -m genshen_skin_cp23.engine.cli`。
- **桌宠不透明**: 个别 Linux 桌面不支持透明色键, 会退化为白底卡片, 功能不受影响。

## 🔗 与其它套件的关系

与 WPH666-py 的其它皮肤套件**完全独立**: 包名 `genshen-skin-cp23`、
命令前缀 `genshen-cp23`、运行时目录 `~/.genshen-cp23`、
vscode 扩展 ID `wp666.genshen-skin-cp23`、
DeepKing 皮肤 id `genshen-cp23-lumine-noelle`
互不冲突, 各套件可同时安装。引擎与其它套件共用同一套实现。

## 🙏 素材说明

1 张荧 × 诺艾尔同人插画。**仅用于个人桌面美化, 请勿二次商用。**
版权归原作者所有。

## 📄 许可

代码以 MIT 许可发布(见 [LICENSE](LICENSE)); 插画素材不在 MIT 授权范围内。
