# coding: utf-8
import sys
import cv2


def imcut(im):
    if isinstance(im, str):
        im = cv2.imread(im)
    h, w, _ = im.shape
    im = im[:w * 320 // 240]
    im = cv2.resize(im, (240, 320))
    return im


def _clip(im, width=1366, height=768):
    h, w, _ = im.shape
    y = (h - w * height // width) // 2
    y = max(y, 0)
    x = (w - h * width // height) // 2
    x = max(x, 0)
    im = im[y:h - y, x:w - x]
    return im


def clip(im, width=1366, height=768):
    if isinstance(im, str):
        im = cv2.imread(im)
    im = _clip(im, width, height)
    return cv2.resize(im, (width, height))


if __name__ == '__main__':
    assert len(sys.argv) >= 2
    fn = sys.argv[1]
    im = clip(fn, 750, 500)
    cv2.imshow('a', im)
    cv2.waitKey()
