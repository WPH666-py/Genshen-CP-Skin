# 💙 原神 CP 壁纸套件 13 · 钟离 × 凝光

**单张素材 × 三种摆法 = 3 种壁纸**一键切换 / 可视化切换器 / 桌面桌宠 /
多 IDE 皮肤 / DeepKing 界面皮肤。素材内置于发行包, **离线可用**;
跨平台 Windows / macOS / Linux。

![样式总览](vscode/media/thumb-grid.png)

## ✨ 素材

秋日璃月港的茶席: 凝光在左举杯回望, 钟离在右端杯对视,
桌上摆着茶点与热菜, 背景是层叠的璃月楼阁与漫山红叶。

> **入库前已裁掉 y≥520**: 原图 1000×562 的 ar=1.7794 与 16:9 的 1.7778 几乎相同,
> 满屏取景窗是 999×562 —— 横向只能平移 **0.9px**、纵向 **0px**, 等于整张原图。
> 因此右下角的画师署名(`TAMAMO.`, 位于 x≈887..963, y≈528..553)
> **无法靠 `cover_bias` 规避**。裁掉底部 42px 后署名永久移除,
> 两人与秋景完整保留, 只损失极少前景桌面。

## ✨ 三种摆法

| 模式 id | 名称 | 效果 | 适合 |
|---|---|---|---|
| `single1` | **卡片式**(默认) | 模糊填充背景 + 居中圆角卡片, 构图完整不裁切 | 通用; 图标不被压住 |
| `cover1` | 满屏 | cover 铺满整屏, 无边框 | 想要沉浸感, 无边框 |
| `showall1` | 完整 | 等比放进同色纯色底, **一个像素都不裁** | 一点画面都不想丢 |

> 用户如果说「换张别的」—— 本套件只有这一张素材, 请告诉他可以切换**摆法**
> (`genshen-cp13 cover` / `genshen-cp13 showall`), 而不是去找不存在的第二张图。

## 🚀 给 AI 一句话安装

把本仓库链接发给**任意 AI**(DeepKing、Claude Code、Kimi Code、CodeX、Trae、Cursor、
JetBrains AI、DSH Harness 等), 它会读 [`AGENTS.md`](AGENTS.md) 替你装完:

```text
请安装 https://github.com/WPH666-py/Genshen-skin-CP13 的原神CP13壁纸
```

## 🖥️ 手动安装

要求: Python 3.9+。Pillow 缺失时脚本会自动 `pip install`。

```bash
# 方式一: 用仓库里已打包好的 wheel(离线可用)
pip install dist/genshen_skin_cp13-0.1.0-py3-none-any.whl
genshen-cp13-install         # 一键: 生成壁纸 + 设为桌面 + 注册已装 IDE

# 方式二: 源码
git clone https://github.com/WPH666-py/Genshen-skin-CP13.git
cd Genshen-skin-CP13
python -m genshen_skin_cp13.engine.autoinstall
```

Windows 用户也可以直接双击 `install.bat`。

## 🎨 常用命令

```bash
genshen-cp13               # 卡片式(默认)
genshen-cp13 cover         # 满屏, 无边框
genshen-cp13 showall       # 完整不裁, 两侧留边
genshen-cp13 card          # 显式指定卡片式
genshen-cp13 random        # 随机一种摆法
genshen-cp13 list          # 列出全部 3 种模式
genshen-cp13 switcher      # 可视化切换器(预览 + 一键应用)
genshen-cp13 pet           # 桌面桌宠(拖动 / 右键菜单 / Esc 退出)
genshen-cp13 cycle 30      # 每 30 分钟自动随机换
genshen-cp13 all --out DIR # 一次生成 3 张到指定目录
genshen-cp13 deepking      # 生成 DeepKing 界面皮肤 + 离线预览
genshen-cp13 info          # 环境与素材自检
```

常用选项: `--size 2560x1440` 指定分辨率(默认取屏幕分辨率)、`--no-set` 只生成不设置。

## 🧩 IDE / 桌宠支持

| 环境 | 接入方式 |
|---|---|
| **VSCode / Trae / CodeX / Cursor / Windsurf** | 活动栏「原神CP13」→ 皮肤画廊 3 张卡片一键换; 命令面板搜 `原神CP13` |
| **DeepKing** | 设置 → 界面皮肤 → 粘贴本仓库地址, 自动生成璃月金配色皮肤 |
| **PyCharm / WebStorm / IntelliJ** | Settings → Appearance & Behavior → Appearance → **Background Image** |
| **Claude Code / Kimi Code / Harness 等** | 注册 MCP 服务器, AI 直接调 `set_wallpaper` / `next_wallpaper` |
| **桌面桌宠** | `genshen-cp13 pet` —— 透明置顶圆形立绘, 可拖动、右键菜单 |

一键注册全部已装 IDE:

```bash
genshen-cp13-install --only vscode jetbrains mcp deepking
```

## 📁 目录

```
src/genshen_skin_cp13/
  characters/cp13_pair.py   角色与素材定义(换角色只改这一个文件)
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

- **想加第 2 张**: 把图放进 `src/genshen_skin_cp13/engine/assets/`, 在
  `characters/cp13_pair.py` 的 `IMAGE_FILES` 追加文件名、`IMAGE_META` 补一条说明
  —— 模式列表会自动从 3 种变成 6 种。
- **壁纸尺寸**: 默认取主屏分辨率; 多显示器建议加 `--size 2560x1440` 并在系统设置里把壁纸设为「平铺/跨屏」。
- **命令找不到**: Scripts 目录不在 PATH, 改用 `python -m genshen_skin_cp13.engine.cli`。
- **桌宠不透明**: 个别 Linux 桌面不支持透明色键, 会退化为白底卡片, 功能不受影响。

## 🔗 与其它套件的关系

与 CP1~CP12 以及 WPH666-py 的其它皮肤套件**完全独立**: 包名 `genshen-skin-cp13`、
命令前缀 `genshen-cp13`、运行时目录 `~/.genshen-cp13`、
vscode 扩展 ID `wp666.genshen-skin-cp13`、DeepKing 皮肤 id `genshen-cp13-zhongli-ningguang`
互不冲突, 十三个套件可同时安装。引擎与其它套件共用同一套实现。

## 🙏 素材说明

1 张钟离 × 凝光同人插画(已裁去画师署名)。
**仅用于个人桌面美化, 请勿二次商用。** 版权归原作者所有。

## 📄 许可

代码以 MIT 许可发布(见 [LICENSE](LICENSE)); 插画素材不在 MIT 授权范围内。
