
import sys

import cv2
import numpy as np


def _capture_detect_0(im_hsv, threshold=35, q=0.1):
    last_hsv = im_hsv[0]
    im_h = im_hsv.shape[0]
    for w in range(int(im_h * q)):
        curr_hsv = im_hsv[w]
        delta_hsv = np.mean(np.abs(curr_hsv - last_hsv))
        if delta_hsv > threshold:
            break
        last_hsv = curr_hsv
    return w


def _capture_detect_1(im, threshold=35, q=0.2):
    hh, ww = im.shape[:2]
    im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    w = _capture_detect_0(im_hsv, threshold, q)
    im_hsv = np.rot90(im_hsv)
    d = _capture_detect_0(im_hsv, threshold, q)
    im_hsv = np.rot90(im_hsv)
    s = _capture_detect_0(im_hsv, threshold, q)
    im_hsv = np.rot90(im_hsv)
    a = _capture_detect_0(im_hsv, threshold, q)
    return w, hh - s, a, ww - d


def capture_detect(im, threshold=35, q=0.2):
    w, s, a, d = _capture_detect_1(im, threshold, q)
    return im[w:s, a:d]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('python cvutils.py <image filename> <output>')
        exit()
    fn = sys.argv[1]
    im = cv2.imread(fn)
    # im = cv2.resize(im, None, fx=4, fy=4)
    w, s, a, d = _capture_detect_1(im, 35, q=0.2)
    if len(sys.argv) > 2:
        cv2.imwrite(sys.argv[2], im[w:s, a:d])
    im = cv2.rectangle(im, (a - 1, w - 1), (d, s), (0, 0, 255), 2)
    cv2.imshow('result', im)
    cv2.waitKey()
