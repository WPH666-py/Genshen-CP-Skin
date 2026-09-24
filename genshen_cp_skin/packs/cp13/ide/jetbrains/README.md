# JetBrains 系 IDE (PyCharm / WebStorm / IntelliJ / GoLand) — 原神CP13 背景图

JetBrains 的背景图是官方 UI 功能, 脚本负责生成高清素材, 之后只需 2 次点击。

## 步骤(可让 AI 自动执行)

1. 生成全部素材:

   ```bash
   genshen-cp13 all --out "%USERPROFILE%\GenshenCP13-Backgrounds"   # Windows
   genshen-cp13 all --out ~/GenshenCP13-Backgrounds                 # macOS / Linux
   ```

   源码形态: `python -m genshen_skin_cp13.engine.cli all --out 目录`

   输出 3 张: 卡片式(`single1`)、满屏(`cover1`)、完整不裁(`showall1`)

2. 打开 IDE:
   **Settings / Preferences → Appearance & Behavior → Appearance → Background Image**

3. 点 `+` 添加图片 → 选择刚生成的任意一张。

   - **编辑器区推荐 `single1-*.jpg`**: 中间留白多, 代码可读性最好
   - **欢迎页 / 工具窗口推荐 `cover1-*.jpg`**: 满屏秋景, 视觉冲击强
   - **不想裁掉任何画面用 `showall1-*.jpg`**: 两侧留同色边
   - 想让代码更清晰: 把下方的 **Opacity** 调到 10%~20%

4. 可对 **Editor / Welcome screen / Menus and tool windows** 分别设置不同图片。
