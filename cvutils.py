import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont


def put_text(img, text, xy, fill=(255, 255, 255), size=20, font='SourceHanSansCN-Bold.otf'):
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, size, encoding='utf-8')
    draw.text(xy, text, fill, font=font)
    return np.asarray(img)


if __name__ == '__main__':
	im = np.zeros((100, 200, 3), dtype='uint8')
	im = put_text(im, "你好 World!!!", (5, 5))
	cv2.imshow('a', im)
	cv2.waitKey()
