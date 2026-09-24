# JetBrains 系 IDE (PyCharm / WebStorm / IntelliJ / GoLand) — 原神CP17 背景图

JetBrains 的背景图是官方 UI 功能, 脚本负责生成高清素材, 之后只需 2 次点击。

## 步骤(可让 AI 自动执行)

1. 生成全部素材:

   ```bash
   genshen-cp17 all --out "%USERPROFILE%\GenshenCP17-Backgrounds"   # Windows
   genshen-cp17 all --out ~/GenshenCP17-Backgrounds                 # macOS / Linux
   ```

   源码形态: `python -m genshen_skin_cp17.engine.cli all --out 目录`

   输出 3 张: 完整(`showall1`, 默认)、卡片式(`single1`)、满屏(`cover1`)

2. 打开 IDE:
   **Settings / Preferences → Appearance & Behavior → Appearance → Background Image**

3. 点 `+` 添加图片 → 选择刚生成的任意一张。

   - **编辑器区推荐 `showall1-*.jpg`**: 四格全见, 留白最多, 代码可读性最好
   - **欢迎页 / 工具窗口推荐 `single1-*.jpg`**: 居中卡片, 视觉更聚焦
   - **满屏(`cover1-*.jpg`)不建议**: 素材是竖图, 铺满 16:9 会上下裁掉大半
   - 想让代码更清晰: 把下方的 **Opacity** 调到 10%~20%

4. 可对 **Editor / Welcome screen / Menus and tool windows** 分别设置不同图片。
