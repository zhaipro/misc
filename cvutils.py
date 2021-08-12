import os

import cv2
import numpy as np
from mutagen.mp3 import MP3
from mutagen.wave import WAVE
from PIL import Image, ImageDraw, ImageFont


def put_text(img, text, xy, fill=(255, 255, 255), size=20, font='SourceHanSansCN-Bold.otf'):
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, size, encoding='utf-8')
    draw.text(xy, text, fill, font=font)
    return np.asarray(img)


def to_frame(cap):
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        yield frame


def get_time_secs(fn):
    assert os.path.isfile(fn), f'get_time_secs({fn})?'
    if fn.endswith('.mp4'):
        cap = cv2.VideoCapture(fn)
        time_secs = cap.get(7) / cap.get(5)
        cap.release()
        return time_secs
    elif fn.endswith('.mp3'):
        return MP3(fn).info.length
    elif fn.endswith('.wav'):
        return WAVE(fn).info.length
    else:
        assert False, f'get_time_secs({fn})?'


if __name__ == '__main__':
    for fn in ['r.mp4', 'r.wav']:
        r = get_time_secs(fn)
        print(fn, r)
    im = np.zeros((100, 200, 3), dtype='uint8')
    im = put_text(im, "你好 World!!!", (5, 5))
    cv2.imshow('a', im)
    cv2.waitKey()
