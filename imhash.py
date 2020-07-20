# coding: utf-8
import cv2
import numpy as np
import scipy.fftpack


def humanize(hash_func):
    def wrapper(im):
        if isinstance(im, str):
            im = cv2.imread(im, cv2.IMREAD_GRAYSCALE)
        if im.ndim == 3:
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        im = hash_func(im)
        im = np.packbits(im)
        im.dtype = 'uint64'
        return im
    return wrapper


@humanize
def avhash(im):
    im = cv2.resize(im, (8, 8), interpolation=cv2.INTER_CUBIC)
    avg = im.mean()
    im = im > avg
    return im


@humanize
def phash(im):
    im = cv2.resize(im, (32, 32), interpolation=cv2.INTER_CUBIC)
    im = scipy.fftpack.dct(scipy.fftpack.dct(im, axis=0), axis=1)
    im = im[:8, :8]
    med = np.median(im)
    im = im > med
    return im


def distance(h0, h1):
    r = h0 ^ h1
    r.dtype = np.uint8
    r = np.unpackbits(r)
    r.shape = -1, 64
    r = r.sum(axis=1)
    return r


if __name__ == '__main__':
    import sys

    fn0, fn1 = sys.argv[1:3]
    im = cv2.imread(fn0)
    h0 = phash(im)
    im = cv2.imread(fn1)
    h1 = phash(im)
    r = distance(h0, h1)
    print(r)
