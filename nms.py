"""
目标检测必会NMS
"""
# Naive版本
from typing import AsyncIterable
import numpy as np

def nms(bboxes, thrd=0.5):
    if bboxes.shape[0] == 0:
        return bboxes
    x1 = bboxes[:, 0]
    y1 = bboxes[:, 1]
    x2 = bboxes[:, 2]
    y2 = bboxes[:, 3]
    score = bboxes[:, 4]
    area = (y2 - y1 + 1) * (x2 - x1 + 1)
    keep = []
    inds = score.argsort()[::-1]
    while len(inds) > 0:
        i = inds[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[inds[1:]])
        yy1 = np.maximum(y1[i], y1[inds[1:]])
        xx2 = np.minimum(x2[i], x2[inds[1:]])
        yy2 = np.minimum(y2[i], y2[inds[1:]])
        inter_area = np.maximum(0, yy2 - yy1 + 1) * np.maximum(0, xx2 - xx1 + 1)
        iou = inter_area / (area[i] + area[inds[1:]] - inter_area)
        print(iou)
        inds = inds[1:]
        inds = inds[iou < thrd]
    return bboxes[keep]

bboxes= np.array([[0, 0, 40, 40, 0.5], 
                  [1, 1, 50, 50, 0.7],
                  [4, 4, 70, 70, 0.9],
                  [20, 20, 40, 40, 0.3] ])
result = nms(bboxes)
print(result)
        
