# coding: utf-8
import sys
import cv2


def imcut(im, width, height, x=0.5, y=0.5, r=1.0, resize=False):
    if isinstance(im, str):
        im = cv2.imread(im)
    h, w, _ = im.shape
    ch = int(max(h - w * height / width * r, 0))
    cw = int(max(w - h * width / height * r, 0))
    x, y = int(cw * x), int(ch * y)
    im = im[y:h - ch + y, x:w - cw + x]
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
