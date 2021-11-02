# 发呆用工具
import random

import cv2
import numpy as np


def show(gs=4, w=512):
    im = np.zeros((w, w, 4), dtype='uint8')
    im[:] = 255

    path = []
    x, y = w // 2, w // 2
    while True:
        if len(path) > 200:
            i, j = path.pop(0)
            im[i:i + gs, j:j + gs] = im[i, j, 3]
        # x += random.choice([-gs, gs])
        # y += random.choice([-gs, gs])
        dx, dy = random.choice([(0, gs), (0, -gs), (gs, 0), (-gs, 0)])
        x += dx
        y += dy
        x = max(min(x, w - gs), 0)
        y = max(min(y, w - gs), 0)
        path.append((x, y))
        im[x, y, 3] = max(im[x, y, 3] - 125, 0)
        for p, (i, j) in enumerate(path, 100 + 200 - len(path)):
            im[i:i + gs, j:j + gs, :3] = 0, 0, max(min(p * 255 // (200 + 100), 255), 0)
        cv2.imshow('Random Walk', im)
        if cv2.waitKey(1) == ord(' '):
            break


if __name__ == '__main__':
    show()
