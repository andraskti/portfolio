from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1200, 630
im = Image.new("RGB", (W, H), (8, 8, 12))

# orb warna (diblur seperti di web)
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(layer)
d.ellipse((-260, -220, 420, 420), fill=(106, 77, 255, 200))
d.ellipse((W-380, 120, W+180, 620), fill=(47, 107, 255, 170))
d.ellipse((180, H-260, 700, H+160), fill=(224, 79, 176, 130))
layer = layer.filter(ImageFilter.GaussianBlur(120))
im = Image.alpha_composite(im.convert("RGBA"), layer).convert("RGB")

dr = ImageDraw.Draw(im)
# grid samar
for x in range(0, W, 64):
    dr.line((x, 0, x, H), fill=(255, 255, 255, 6), width=1)
for y in range(0, H, 64):
    dr.line((0, y, W, y), fill=(255, 255, 255, 6), width=1)

def font(size, bold=True):
    for f in ([r"C:\Windows\Fonts\seguibl.ttf"] if bold else []) + \
             [r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf",
              r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf"]:
        try:
            return ImageFont.truetype(f, size)
        except Exception:
            pass
    return ImageFont.load_default()

def mono(size):
    for f in [r"C:\Windows\Fonts\consolab.ttf", r"C:\Windows\Fonts\consola.ttf"]:
        try:
            return ImageFont.truetype(f, size)
        except Exception:
            pass
    return font(size, False)

AC = (179, 166, 255)
# label atas
dr.text((80, 92), "PORTFOLIO  /  SEMARANG, ID", font=mono(26), fill=(160, 160, 172))
# nama besar
dr.text((76, 170), "ANDRA SAKTI", font=font(110), fill=(242, 241, 238))
dr.text((76, 300), "PRAGATA", font=font(110), fill=(242, 241, 238),
        stroke_width=2, stroke_fill=(242, 241, 238))
# garis aksen + peran
dr.rectangle((82, 448, 292, 454), fill=AC)
dr.text((80, 476), "SOCIAL MEDIA SPECIALIST · SEO WRITER", font=mono(30), fill=(242, 241, 238))
dr.text((80, 524), "CREATIVE DIRECTOR · WEDDING & EVENT CREW", font=mono(30), fill=(179, 166, 255))
# asterisk kanan bawah
cx, cy, r = W - 140, H - 150, 52
for ang in range(0, 180, 45):
    import math
    a = math.radians(ang)
    dr.line((cx - r*math.cos(a), cy - r*math.sin(a), cx + r*math.cos(a), cy + r*math.sin(a)),
            fill=AC, width=7)

im.save("og-cover.jpg", "JPEG", quality=88, optimize=True)
import os
print("og-cover.jpg:", os.path.getsize("og-cover.jpg") // 1024, "KB")
