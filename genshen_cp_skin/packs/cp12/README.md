# 💙 原神 CP 壁纸套件 12 · 行秋 × 重云

**三张素材 × 三种摆法 = 9 种壁纸**一键切换 / 可视化切换器 / 桌面桌宠 /
多 IDE 皮肤 / DeepKing 界面皮肤。素材内置于发行包, **离线可用**;
跨平台 Windows / macOS / Linux。

![样式总览](vscode/media/thumb-grid.png)

## ✨ 三张素材

冰与水的双人, 三种场景:

| 序号 | 名称 | 画面 | 原始比例 |
|---|---|---|---|
| 1 | 月下 | 满月前对坐: 重云持冰蓝长剑与雪花, 行秋托腮含笑, 左下嫩芽黄花丛 | 1.333 横图 |
| 2 | 蓝伞 | 蓝伞与花枝下: 重云着白底蓝纹外袍, 行秋执折扇比耶, 水蓝史莱姆环绕 | 1.365 横图 |
| 3 | 晴空 | 晴空天台: 重云穿连帽衫吃冰棍, 行秋着校服读着书, 左侧趴着一只猫 | 1.412 横图 |

> **第 2 张已做无损预裁**: 原图 688×600 的右下角带画师水印。
> 这张窄于 16:9, 满屏取景窗**横向会用满整张源图、只能上下裁**,
> 所以 `cover_bias` 无论如何都移不掉那个水印 —— 与 CP11 是同一类问题。
> 入库前裁掉 y≥504(水印在 y≈570..600), 水印永久移除, 两人与伞面完整保留。

## ✨ 三种摆法

每张素材都能在三种摆放方式之间切换, 所以共 **9 种壁纸**:

| 模式 id | 名称 | 效果 | 适合 |
|---|---|---|---|
| `single1..3` | **卡片式**(默认) | 模糊填充背景 + 居中圆角卡片, 构图完整不裁切 | 通用; 图标不被压住 |
| `cover1..3` | 满屏 | cover 铺满整屏, 无边框 | 想要沉浸感, 无边框 |
| `showall1..3` | 完整 | 等比放进同色纯色底, **一个像素都不裁** | 一点画面都不想丢 |

> 三张都窄于 16:9(1.333 / 1.365 / 1.412), 满屏时**左右零裁切**、只裁上下,
> 因此横向构图完全不会丢, 只需校准纵向取景窗。

## 🚀 给 AI 一句话安装

把本仓库链接发给**任意 AI**(DeepKing、Claude Code、Kimi Code、CodeX、Trae、Cursor、
JetBrains AI、DSH Harness 等), 它会读 [`AGENTS.md`](AGENTS.md) 替你装完:

```text
请安装 https://github.com/WPH666-py/Genshen-skin-CP12 的原神CP12壁纸
```

## 🖥️ 手动安装

要求: Python 3.9+。Pillow 缺失时脚本会自动 `pip install`。

```bash
# 方式一: 用仓库里已打包好的 wheel(离线可用)
pip install dist/genshen_skin_cp12-0.1.0-py3-none-any.whl
genshen-cp12-install         # 一键: 生成壁纸 + 设为桌面 + 注册已装 IDE

# 方式二: 源码
git clone https://github.com/WPH666-py/Genshen-skin-CP12.git
cd Genshen-skin-CP12
python -m genshen_skin_cp12.engine.autoinstall
```

Windows 用户也可以直接双击 `install.bat`。

## 🎨 常用命令

```bash
genshen-cp12               # 第 1 张 · 卡片式(默认)
genshen-cp12 2             # 第 2 张(蓝伞)
genshen-cp12 3             # 第 3 张(晴空)
genshen-cp12 cover         # 第 1 张满屏
genshen-cp12 cover2        # 第 2 张满屏
genshen-cp12 showall3      # 第 3 张完整不裁
genshen-cp12 random        # 随机一张(9 种里随机)
genshen-cp12 list          # 列出全部 9 种模式
genshen-cp12 switcher      # 可视化切换器(预览 + 一键应用 + 自动随机)
genshen-cp12 pet           # 桌面桌宠(拖动 / 右键换立绘 / Esc 退出)
genshen-cp12 cycle 30      # 每 30 分钟自动随机换
genshen-cp12 all --out DIR # 一次生成 9 张到指定目录
genshen-cp12 deepking      # 生成 DeepKing 界面皮肤 + 离线预览
genshen-cp12 info          # 环境与素材自检
```

常用选项: `--size 2560x1440` 指定分辨率(默认取屏幕分辨率)、`--no-set` 只生成不设置。

## 🧩 IDE / 桌宠支持

| 环境 | 接入方式 |
|---|---|
| **VSCode / Trae / CodeX / Cursor / Windsurf** | 活动栏「原神CP12」→ 皮肤画廊 9 张卡片一键换; 命令面板搜 `原神CP12` |
| **DeepKing** | 设置 → 界面皮肤 → 粘贴本仓库地址, 自动生成靛蓝配色皮肤 |
| **PyCharm / WebStorm / IntelliJ** | Settings → Appearance & Behavior → Appearance → **Background Image** |
| **Claude Code / Kimi Code / Harness 等** | 注册 MCP 服务器, AI 直接调 `set_wallpaper` / `next_wallpaper` |
| **桌面桌宠** | `genshen-cp12 pet` —— 透明置顶圆形立绘, 可拖动、右键菜单 |

一键注册全部已装 IDE:

```bash
genshen-cp12-install --only vscode jetbrains mcp deepking
```

## 📁 目录

```
src/genshen_skin_cp12/
  characters/cp12_pair.py   角色与素材定义(换角色只改这一个文件)
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

- **想加第 4 张**: 把图放进 `src/genshen_skin_cp12/engine/assets/`, 在
  `characters/cp12_pair.py` 的 `IMAGE_FILES` 追加文件名、`IMAGE_META` 补一条说明
  —— 模式列表会自动从 9 种变成 12 种。
- **壁纸尺寸**: 默认取主屏分辨率; 多显示器建议加 `--size 2560x1440` 并在系统设置里把壁纸设为「平铺/跨屏」。
- **命令找不到**: Scripts 目录不在 PATH, 改用 `python -m genshen_skin_cp12.engine.cli`。
- **桌宠不透明**: 个别 Linux 桌面不支持透明色键, 会退化为白底卡片, 功能不受影响。

## 🔗 与其它套件的关系

与 CP1~CP11 以及 WPH666-py 的其它皮肤套件**完全独立**: 包名 `genshen-skin-cp12`、
命令前缀 `genshen-cp12`、运行时目录 `~/.genshen-cp12`、
vscode 扩展 ID `wp666.genshen-skin-cp12`、DeepKing 皮肤 id `genshen-cp12-xingqiu-chongyun`
互不冲突, 十二个套件可同时安装。引擎与其它套件共用同一套实现。

## 🙏 素材说明

3 张行秋 × 重云同人插画(第二张已裁去画师水印)。
**仅用于个人桌面美化, 请勿二次商用。** 版权归原作者所有。

## 📄 许可

代码以 MIT 许可发布(见 [LICENSE](LICENSE)); 插画素材不在 MIT 授权范围内。
