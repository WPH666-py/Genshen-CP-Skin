# -*- coding: utf-8 -*-
"""
生成 VSCode 扩展画廊所需的缩略图与图标。

  python vscode/gen_media.py

优先从仓库源码(src/)导入本套件; 若已 pip 安装则直接用已安装的包。
输出到 vscode/media/:
  thumb-single1..3.png / thumb-cover1..3.png  画廊卡片缩略图 (640x360)
  thumb-grid.png                              所有样式拼版 (文档用)
  icon.png                                    扩展市场图标 (256x256)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
MEDIA = os.path.join(HERE, "media")
THUMB = (640, 360)

# 优先仓库源码, 回退已安装包
sys.path.insert(0, os.path.join(REPO, "src"))
try:
    from genshin_skin_cp1 import skin_core as sc
except ImportError:  # 已 pip 安装的情况
    import genshin_skin_cp1.skin_core as sc


def ensure_media():
    os.makedirs(MEDIA, exist_ok=True)


def make_thumbs():
    from PIL import Image, ImageDraw
    modes = [m[0] for m in sc.MODES]
    made = []
    for mode in modes:
        img = sc.compose(mode, THUMB)
        out = os.path.join(MEDIA, "thumb-%s.png" % mode)
        img.save(out, optimize=True)
        made.append(out)
        print("  OK  %-9s -> %s" % (mode, os.path.basename(out)))

    # 拼版总览图
    cols, rows = 3, 2
    tw, th = THUMB
    gap = 12
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * gap,
                              rows * th + (rows + 1) * gap), (16, 22, 31))
    for i, mode in enumerate(modes[:cols * rows]):
        r, c = divmod(i, cols)
        sheet.paste(sc.compose(mode, THUMB),
                    (gap + c * (tw + gap), gap + r * (th + gap)))
    sheet_out = os.path.join(MEDIA, "thumb-grid.png")
    sheet.save(sheet_out, optimize=True)
    print("  OK  grid      -> %s" % os.path.basename(sheet_out))
    return made


def make_icon():
    """扩展图标: 蓝紫渐变圆角底 + 白色爱心(比心手势的意象)。"""
    from PIL import Image, ImageDraw
    S = 256
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # 渐变底
    for y in range(S):
        t = y / (S - 1)
        r = int(58 + (126 - 58) * t)
        g = int(140 + (96 - 140) * t)
        b = int(233 + (214 - 233) * t)
        d.line([(0, y), (S, y)], fill=(r, g, b, 255))
    # 圆角遮罩
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, S - 1, S - 1], radius=56, fill=255)
    img.putalpha(mask)

    # 爱心: 四倍超采样后缩小, 消除圆弧与三角之间的接缝
    SS = 4
    big = Image.new("RGBA", (S * SS, S * SS), (0, 0, 0, 0))
    bd = ImageDraw.Draw(big)
    cx, cy = S // 2, int(S * 0.44)
    R = int(S * 0.21)
    bx, by, bR = cx * SS, cy * SS, R * SS
    white = (255, 255, 255, 255)
    bd.ellipse([bx - 2 * bR, by - bR, bx, by + bR], fill=white)
    bd.ellipse([bx, by - bR, bx + 2 * bR, by + bR], fill=white)
    # 三角底边上移并与两圆重叠, 避免出现尖角接缝
    bd.polygon([(bx - 2 * bR + bR // 5, by + bR // 3),
                (bx + 2 * bR - bR // 5, by + bR // 3),
                (bx, by + 3 * bR)], fill=white)
    img = Image.alpha_composite(img, big.resize((S, S), Image.LANCZOS))

    # 底部一颗小青绿点(呼应少女发色)
    dot = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    dr = 15
    ImageDraw.Draw(dot).ellipse(
        [cx - dr, int(S * 0.795), cx + dr, int(S * 0.795) + 2 * dr],
        fill=(94, 226, 214, 255))
    img = Image.alpha_composite(img, dot)

    out = os.path.join(MEDIA, "icon.png")
    img.save(out)
    print("  OK  icon      -> %s" % os.path.basename(out))
    return out


def main():
    ensure_media()
    sc.ensure_pillow()
    print("[gen_media] 生成缩略图 %s" % MEDIA)
    make_thumbs()
    make_icon()
    print("[gen_media] 完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
