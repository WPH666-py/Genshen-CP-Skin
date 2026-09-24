# AGENTS.md — 原神 CP 壁纸套件合集 · AI 自动安装指引（AI 助手必读）

用户把 **https://github.com/WPH666-py/Genshen-CP-Skin** 交给你，并说
「装原神CP壁纸 / 换个壁纸 / 装 CP24 / 甘雨绫华壁纸 / 装个桌宠」时，按本文件执行。

> **给 AI 的话**：当用户点名某套 CP 时，**你就是安装器**，直接替用户执行，
> 不要让用户自己敲命令。所有命令都是幂等的。

---

## 这套东西是什么

**24 套原神 CP 壁纸，一个安装包全部带走。**

与原先把「一套一个仓库」的做法不同，本包把每一套的**源图与自带引擎都打进包里**，
所以：

- **装壁纸全程不需要联网**，不需要 git，也不依赖 GitHub 是否可访问
- 装完即可用，不需要先拉仓库

壁纸由**各套自带引擎按用户屏幕分辨率实时合成**，不是预生成的固定尺寸图。

### 三种摆法

| 摆法 id | 名称 | 说明 |
|---|---|---|
| `single1` | 卡片式 | **默认**。模糊填充背景 + 居中圆角卡片，构图完整不裁切 |
| `cover1` | 满屏 | cover 铺满整屏，无边框 |
| `showall1` | 完整 | 等比放进同色纯色底，一个像素都不裁 |

编号对应素材张数（`single1/2/3` …）。

> ⚠️ **摆法数量各套不同，不要替用户假设**。以实测为准：
> `cp1` 只有 `single` + `cover` 两族（6 种，**没有 showall**）；
> 单图套件多为 3 种；三图套件为 9 种。
> 用 `gc wallpaper <套件> --list` 看该套的真实清单。

---

## 第 0 步：先确认用户想要哪一套

- 用户点名了 → 用 `gc show <关键词>` 确认后再装。
- 不确定是哪一套 → 读 `genshen_cp_skin/catalog.json` 的 `packs[].char` / `name` / `aliases`
  匹配；匹配不到就列几个候选问用户。
- **不要**在没有确认的情况下给 24 套全部换壁纸（那是 24 次系统壁纸切换）。

找某套有四种写法，都能命中：

```bash
gc show cp24      # 编号
gc show 24        # 序号
gc show 甘雨       # 角色名
gc show ganyu     # 拼音
```

角色关键词对照：cp1=米提亚×沃雅妮莎、cp2=奥黛塔×沃雅妮莎、cp3=米提亚×奥黛塔×沃雅妮莎、
cp4=柯莱×安柏、cp5=桑多涅×哥伦比娅、cp6=玛拉妮×基尼奇×卡其娜、cp7=娜维娅×克洛琳德、
cp8=胡桃×芙宁娜、cp9=神里绫华×宵宫、cp10=雷电影×八重神子、cp11=胡桃×香菱、
cp12=行秋×重云、cp13=钟离×凝光、cp14=神里绫华×优菈×甘雨、cp15=甘雨×刻晴、
cp16=温迪×芭芭拉、cp17=奥黛塔×沃雅妮莎×米提亚×阿罗夏、cp18=散兵×万叶、
cp19=空×荧、cp20=散兵×荧、cp21=魈×荧、cp22=荧×达达利亚、cp23=荧×诺艾尔、
cp24=甘雨×绫华

---

## 第 1 步：装安装器

```bash
py -3 -m pip install genshen-cp-skin          # Windows
python3 -m pip install genshen-cp-skin        # macOS / Linux
```

**国内网络装不上时**（pypi.org 连不上 / TLS 被中断）改用镜像，三个都试一下：

```bash
py -3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple genshen-cp-skin   # 清华
py -3 -m pip install -i https://mirrors.ustc.edu.cn/pypi/simple genshen-cp-skin    # 中科大
py -3 -m pip install -i https://mirrors.aliyun.com/pypi/simple genshen-cp-skin     # 阿里云
```

**没有 Python 时**先装（3.8 及以上任意版本都可以）：

```bash
winget install Python.Python.3.12     # Windows
brew install python                   # macOS
sudo apt install python3 python3-pil  # Ubuntu / Debian
```

> `gc` 命令不在 `PATH` 里时，用 `py -3 -m genshen_cp_skin <命令>`（Windows）
> 或 `python3 -m genshen_cp_skin <命令>`（macOS / Linux），**不要去改 PATH**。

---

## 第 2 步：装某一套

```bash
gc install cp24              # 一键：壁纸 + IDE 扩展 + 桌宠
gc install cp24 --mode 2     # 指定满屏
gc install cp24 --no-ide --no-pet    # 只换壁纸
```

`install` 会依次做三件事，并**跳过本机不支持的部分**：

1. 用该套自带引擎按屏幕分辨率合成壁纸并设为桌面背景
2. 给检测到的编辑器装 VSIX 扩展（VSCode / Trae / CodeX / Cursor / Windsurf / VSCodium）
3. 启动 Windows 桌面置顶桌宠（悬浮于**所有**窗口之上，覆盖 PyCharm、claude-code、
   kimi-code、CodeX 等一切编辑器）

---

## 第 3 步：按用户环境补做

### A. 换壁纸（用户说「换一张」）

```bash
gc wallpaper cp24                # 随机换一种
gc wallpaper cp24 cover1         # 指定摆法
gc wallpaper cp24 all            # 一次生成全部摆法
gc wallpaper cp24 --list         # 看这套有哪些摆法
```

简写也认：`1`=卡片式 `2`=满屏 `3`=完整 `card`/`cover`/`showall` 同义。

### B. VSCode / Trae / CodeX / Cursor / Windsurf

```bash
gc ide cp24
```

> **这一步需要联网**：VSIX 不随包（24 套共 44 MB），会按需取一次并缓存。
> 取不到时如实告诉用户「扩展需要联网下载」，**不要说整个安装失败** —— 壁纸已经装好了。

没有 CLI 时手动装：把 VSIX 当 zip 解压，`extension/` 目录放到
`%USERPROFILE%\.vscode\extensions\<扩展ID>\`（Trae 用 `.trae\extensions`、
Cursor 用 `.cursor\extensions`、Windsurf 用 `.windsurf\extensions`），重启编辑器。

### C. PyCharm / WebStorm / IntelliJ（背景图）

JetBrains 不支持 VSIX，走背景图：

```bash
gc export cp24 --out D:\CPBackgrounds
```

生成各种摆法的整屏壁纸。再引导用户：
Settings → Appearance & Behavior → **Background Image** → 选一张
（编辑器区推荐 `single1-*.jpg`，浅色留白多、代码可读性更好）。

### D. DeepKing 界面皮肤

```bash
gc deepking cp24            # 生成皮肤 JSON + 离线预览
gc deepking cp24 --check    # 校验源仓库是否满足 DeepKing 契约
gc deepking cp24 --what     # 显示会提取到什么
```

给用户两句话：打开 DeepKing → 设置 → 界面皮肤 → 粘贴该套的源仓库地址。

### E. claude-code / kimi-code / Harness 等（MCP）

CP 各套源仓库自带 MCP 服务器（暴露 `list_wallpapers` / `set_wallpaper` /
`next_wallpaper` / `generate_all` / `wallpaper_info` 五个工具）。
用户需要「用聊天直接换壁纸」时，可引导其注册，命令形如：

```json
{
  "mcpServers": {
    "genshen-cp24": {
      "command": "python",
      "args": ["-m", "genshen_skin_cp24.engine.mcp_server"]
    }
  }
}
```

> 需先 `gc install cp24` 铺开素材，模块才可导入
> （位置 `~/.genshen-cp-skin/Genshen-skin-CP24/src`）。

### F. 桌面桌宠 / 可视化切换器（需要图形桌面）

```bash
gc pet cp24              # 桌宠：左键拖动，右键菜单，Esc 退出
gc pet cp24 --stop       # 停
gc pet cp24 --autostart  # 开机自启
gc pet cp24 --uninstall  # 卸桌宠
```

> 需要本地图形会话。远程/无桌面环境执行失败时，告诉用户在自己电脑上运行，
> **不要说「安装失败」**。

---

## 关于素材：包内自带，离线可用

安装包**自带每套的源图与引擎代码**（约 23 MB），所以：

- `gc install` / `gc wallpaper` **全程不需要联网**，不依赖 GitHub 是否被墙
- 不需要 git
- 壁纸是**按用户屏幕分辨率现算**的，不是固定尺寸的预生成图

边界（如实告知，不要含糊）：

- **换壁纸要 Pillow**：首次用到时脚本会自动 `pip install pillow`
  （venv / conda 下也走对分支，不会因 `--user` 失败）。
  真离线环境需要用户先自行装好 Pillow。
- **VSIX 扩展与吉祥物要联网取一次**：包内不带，取到后缓存，之后离线可用。

---

## 本地文件与目录

| 内容 | 位置 |
|---|---|
| 铺开的套件（含引擎） | `~/.genshen-cp-skin/<源仓库名>/` |
| 合成的壁纸 | `~/.genshen-cp<NN>/wallpapers/` |
| 包内素材（只读） | `<site-packages>/genshen_cp_skin/packs/` |

`GENSHEN_CP_HOME` 可改本地根目录。生成物都不写进用户项目目录，也不改动用户已有文件。

> **运行时目录名不统一是历史遗留，别"顺手统一"**：
> `cp1` 用 `~/.genshin-cp1`（genshin），其余用 `~/.genshen-cp24`（genshen）。
> 改名会让老用户的缓存与已设壁纸路径失效。

---

## 约定与失败处理

- **只读原则**：不改动用户已有文件；素材取自包内，可选件才联网。
- **网络**：`raw.githubusercontent.com` 国内经常不通。本包会自动依次尝试
  直连 → jsDelivr → ghfast → gitmirror → gh-proxy，第一个成功的会被记住。
- **代理**：桌面代理软件通常只设 Windows 系统代理 —— git 能读、pip 读不到。
  本工具会把探测到的代理显式传给 pip；`GENSHEN_NO_PROXY=1` 关闭，
  `GENSHEN_PROXY=http://host:port` 指定。
- **Windows 控制台中文乱码**：先 `chcp 65001`；本工具内置 UTF-8 兜底。
- **桌宠启动后立刻消失**：宿主（AI Agent 的一次命令执行、部分 IDE 终端）会给子进程建
  Job 对象并在结束时回收整棵进程树。让用户双击或在自己终端里启动。
- **非 Windows 环境**：桌宠仅支持 Windows；壁纸合成与设置、VSIX、DeepKing 跨平台可用。
- **卸载**：`gc uninstall cp24`（清本地副本，`--keep-files` 保留素材）。

---

## 一键复述（可直接念给用户）

> 已为你装好「原神 CP 壁纸套件 24 · 甘雨 × 绫华」。
> 换摆法：`gc wallpaper cp24 cover1`（满屏）/ `gc wallpaper cp24 showall1`（完整不裁）
> / `gc wallpaper cp24 single1`（卡片式）；
> 看全部摆法：`gc wallpaper cp24 --list`；生成全部：`gc wallpaper cp24 all`；
> 要别的 CP：`gc list` 看 24 套，然后 `gc install cp7` 这样装。

---

## 素材版权

立绘、壁纸等素材版权归 **米哈游（miHoYo / HoYoverse）**。
本包的**代码**是 MIT，但素材**不在** MIT 授权范围内，仅供个人学习与娱乐，
**不得商用**。用户问及商用时要如实说明。

部分素材带作者水印，各源仓库（`Genshen-skin-CPN`）的 `README.md` 里写明了
保留原因（水印压在结构复杂处，覆盖会留补丁，因此原样保留并如实披露）。
