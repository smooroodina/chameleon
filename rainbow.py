import copy

import numpy as np
import cv2
import random

def change_hue_image(img_hsv, hue_change):
    img_hsv[:, :, 0] = (img_hsv[:, :, 0]+hue_change)%180
    if hue_change % 10 == 0:
        print(img_hsv[:, :, 0])
    return img_hsv

def random_hue_image(img_hsv):
    return change_hue_image(img_hsv, random.randrange(0, 360));

def change_saturation(img_hsv, rate:float):
    result_hsv = copy.deepcopy(img_hsv)
    result_hsv[:, :, 1] = np.clip((result_hsv[:, :, 1].astype(np.float32)*rate), 0, 255)
    return result_hsv

def dynamic_hue_video(img_hsv, fps:int=30, degree:int=1):
    codec = 'avc1'
    h, w, c = img_hsv.shape
    size = (w, h)
    out = cv2.VideoWriter('./dynamicHue.mp4', cv2.VideoWriter_fourcc(*codec), fps, size)
    for i in range(180//degree):
        img_new = cv2.cvtColor(change_hue_image(img_hsv, degree), cv2.COLOR_HSV2BGR)
        out.write(img_new)
    out.release()
