# JetBrains 系 IDE (PyCharm / WebStorm / IntelliJ / GoLand) — 原神CP6 背景图

JetBrains 的背景图是官方 UI 功能, 脚本负责生成高清素材, 之后只需 2 次点击。

## 步骤(可让 AI 自动执行)

1. 生成全部素材:

   ```bash
   genshen-cp6 all --out "%USERPROFILE%\GenshenCP6-Backgrounds"   # Windows
   genshen-cp6 all --out ~/GenshenCP6-Backgrounds                 # macOS / Linux
   ```

   源码形态: `python -m genshen_skin_cp6.engine.cli all --out 目录`

   输出 6 张: 两张素材各有卡片式(`single1..2`)、满屏(`cover1..2`)、完整不裁(`showall1..2`)

2. 打开 IDE:
   **Settings / Preferences → Appearance & Behavior → Appearance → Background Image**

3. 点 `+` 添加图片 → 选择刚生成的任意一张。

   - **编辑器区推荐 `single2-*.jpg`**: 夕照那张是 16:9, 留白舒服、代码可读性好
   - **欢迎页 / 工具窗口推荐 `cover2-*.jpg`**: 满屏夕阳渐变, 视觉冲击强
   - **不想裁掉任何画面用 `showall*-.jpg`**: 两侧留同色边
   - 想让代码更清晰: 把下方的 **Opacity** 调到 10%~20%

4. 可对 **Editor / Welcome screen / Menus and tool windows** 分别设置不同图片。
