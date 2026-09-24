# 💙 原神 CP 壁纸套件 24 · 甘雨 × 绫华

**单张素材 × 三种摆法 = 3 种壁纸**一键切换 / 可视化切换器 / 桌面桌宠 /
多 IDE 皮肤 / DeepKing 界面皮肤。素材内置于发行包, **离线可用**;
跨平台 Windows / macOS / Linux。

![样式总览](vscode/media/thumb-grid.png)

## ✨ 素材

**「和服」** —— 樱花雪景中的和服合影: 甘雨与绫华并肩而立,
一人着白底粉樱和服、一人着绯红金饰旗袍式外衣; 绫华撑着朱红油纸伞,
背景是飘落的樱花、红色缎带与覆雪的屋檐。

原图 1728×1080(ar 1.6)。

> 两人的脸位于**画面上部**, 因此满屏取景窗是**贴顶**的(源 y 0..972)——
> 这样才保住头部, 只裁掉画面下方 108px。实测两人面部、红伞与樱花都完整。

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
请安装 https://github.com/WPH666-py/Genshen-skin-CP24 的原神CP24壁纸
```

## 🖥️ 手动安装

要求: Python 3.9+。Pillow 缺失时脚本会自动 `pip install`。

```bash
# 方式一: 用仓库里已打包好的 wheel(离线可用)
pip install dist/genshen_skin_cp24-0.1.0-py3-none-any.whl
genshen-cp24-install         # 一键: 生成壁纸 + 设为桌面 + 注册已装 IDE

# 方式二: 源码
git clone https://github.com/WPH666-py/Genshen-skin-CP24.git
cd Genshen-skin-CP24
python -m genshen_skin_cp24.engine.autoinstall
```

Windows 用户也可以直接双击 `install.bat`。

## 🎨 常用命令

```bash
genshen-cp24               # 卡片式(默认)
genshen-cp24 card          # 同上, 显式指定
genshen-cp24 cover         # 满屏
genshen-cp24 showall       # 完整不裁
genshen-cp24 random        # 随机一种摆法
genshen-cp24 list          # 列出全部 3 种模式
genshen-cp24 switcher      # 可视化切换器(预览 + 一键应用 + 自动随机)
genshen-cp24 pet           # 桌面桌宠(拖动 / 右键菜单 / Esc 退出)
genshen-cp24 cycle 30      # 每 30 分钟自动随机换
genshen-cp24 all --out DIR # 一次生成 3 张到指定目录
genshen-cp24 deepking      # 生成 DeepKing 界面皮肤 + 离线预览
genshen-cp24 info          # 环境与素材自检
```

常用选项: `--size 2560x1440` 指定分辨率(默认取屏幕分辨率)、`--no-set` 只生成不设置。

## 🧩 IDE / 桌宠支持

| 环境 | 接入方式 |
|---|---|
| **VSCode / Trae / CodeX / Cursor / Windsurf** | 活动栏「原神CP24」→ 皮肤画廊 3 张卡片一键换; 命令面板搜 `原神CP24` |
| **DeepKing** | 设置 → 界面皮肤 → 粘贴本仓库地址, 自动生成深绯配色皮肤 |
| **PyCharm / WebStorm / IntelliJ** | Settings → Appearance & Behavior → Appearance → **Background Image** |
| **Claude Code / Kimi Code / Harness 等** | 注册 MCP 服务器, AI 直接调 `set_wallpaper` / `next_wallpaper` |
| **桌面桌宠** | `genshen-cp24 pet` —— 透明置顶圆形立绘, 可拖动、右键菜单 |

一键注册全部已装 IDE:

```bash
genshen-cp24-install --only vscode jetbrains mcp deepking
```

## 📁 目录

```
src/genshen_skin_cp24/
  characters/cp24_pair.py   角色与素材定义(换角色只改这一个文件)
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

- **想换图**: 把图放进 `src/genshen_skin_cp24/engine/assets/`, 在
  `characters/cp24_pair.py` 的 `IMAGE_FILES` / `IMAGE_NAMES` / `IMAGE_META` 里改一处
  —— 模式列表会自动跟着变(单张是 3 种, 三张就是 9 种)。
- **壁纸尺寸**: 默认取主屏分辨率; 多显示器建议加 `--size 2560x1440`。
- **命令找不到**: Scripts 目录不在 PATH, 改用 `python -m genshen_skin_cp24.engine.cli`。
- **桌宠不透明**: 个别 Linux 桌面不支持透明色键, 会退化为白底卡片, 功能不受影响。

## 🔗 与其它套件的关系

与 WPH666-py 的其它皮肤套件**完全独立**: 包名 `genshen-skin-cp24`、
命令前缀 `genshen-cp24`、运行时目录 `~/.genshen-cp24`、
vscode 扩展 ID `wp666.genshen-skin-cp24`、
DeepKing 皮肤 id `genshen-cp24-ganyu-ayaka`
互不冲突, 各套件可同时安装。引擎与其它套件共用同一套实现。

## 🙏 素材说明

1 张甘雨 × 绫华同人插画(和服主题)。**仅用于个人桌面美化, 请勿二次商用。**
版权归原作者所有。

## 📄 许可

代码以 MIT 许可发布(见 [LICENSE](LICENSE)); 插画素材不在 MIT 授权范围内。
