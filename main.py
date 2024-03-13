from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

# 加载TTF字体文件
font = TTFont('font.ttf')

# 获取字体中的所有字符
chars = [chr(c) for c in font.getBestCmap()]

# 逐个字符生成图片
for char in chars:
    img = Image.new('RGBA', (100, 100), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('font.ttf', 100)  # 调整字体大小
    draw.text((0, 0), char, fill=(0, 0, 0), font=font)  # 调整字符位置和颜色
    img.save(f'{ord(char)}.png')
