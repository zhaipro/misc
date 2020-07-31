import os
import sys

import cv2


def to_video(ipath, ofn):
    writer = None
    ifns = os.listdir(ipath)
    ifns.sort()
    for ifn in ifns:
        ifn = os.path.join(ipath, ifn)
        frame = cv2.imread(ifn)
        if not writer:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            h, w, _ = frame.shape
            writer = cv2.VideoWriter(ofn, fourcc, 25, (w, h))
        writer.write(frame)
    writer.release()


if __name__ == '__main__':
    ipath, ofn = sys.argv[1], sys.argv[2]
    to_video(ipath, ofn)
