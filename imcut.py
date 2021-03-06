# coding: utf-8
import sys
import cv2


def imcut(im, width, height, x=0.5, y=0.5, c=0.0, resize=False):
    if isinstance(im, str):
        im = cv2.imread(im)
    h, w, _ = im.shape
    ch = max(h - w * height / width, 0)
    cw = max(w - h * width / height, 0)
    ch = int(ch + (h - ch) * c)
    cw = int(cw + (w - cw) * c)
    x, y = int(cw * x), int(ch * y)
    im = im[y:h - ch + y, x:w - cw + x]
    if resize:
        im = cv2.resize(im, (width, height))
    return im


def imcut_ex(im, width, height, x=0.5, y=0.5, c=0.0, resize=False):
    if isinstance(im, str):
        im = cv2.imread(im)
    h, w, _ = im.shape
    ch = max(h - w * height / width, 0)
    cw = max(w - h * width / height, 0)
    ch = int(ch + (h - ch) * c)
    cw = int(cw + (w - cw) * c)
    x, y = int((w - cw) * x), int((h - ch) * y)
    if ch > 0:
        im[y:-ch] = im[y + ch:]
        im = im[:-ch]
    if cw > 0:
        im[:, x:-cw] = im[:, x + cw:]
        im = im[:, :-cw]
    if resize:
        im = cv2.resize(im, (width, height))
    return im


if __name__ == '__main__':
    assert len(sys.argv) >= 2
    ifn = sys.argv[1]
    flag = sys.argv[2] if len(sys.argv) >= 3 else 'center'
    ofn = sys.argv[3] if len(sys.argv) >= 4 else None
    if flag == 'left':
        x, y = 0, 0.5
    elif flag == 'right':
        x, y = 1, 0.5
    elif flag == 'top':
        x, y = 0.5, 0
    elif flag == 'down':
        x, y = 0.5, 1.0
    else:
        x, y = 0.5, 0.5
    im = imcut(ifn, 1920, 1080, x=x, y=y, resize=True)
    if ofn:
        cv2.imwrite(ofn, im)
    else:
        cv2.imshow('a', im)
        cv2.waitKey()
