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


if __name__ == '__main__':
    assert len(sys.argv) >= 2
    ifn = sys.argv[1]
    ofn = sys.argv[2] if len(sys.argv) >= 3 else 'a.jpg'
    im = imcut(ifn)
    cv2.imwrite(ofn, im)
