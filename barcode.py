import cv2
import numpy as np


def to_barcode(video):
    if isinstance(video, str):
        video = cv2.VideoCapture(video)
    columns = []
    while True:
        ret, frame = video.read()
        if not ret:
            break
        columns.append(frame.mean(axis=1, keepdims=True))
    columns = np.hstack(columns)
    return columns


if __name__ == '__main__':
    im = to_barcode('video.ts')
    cv2.imwrite('im.jpg', im)
