import copy

import numpy as np
import cv2
import random

def change_hue_image(img_hsv, hue_change):
    def set_new_hue(row):
        new_row = copy.deepcopy(row)
        new_row[:, 0] = (row[:, 0] + hue_change) % 360
        return new_row
    result_hsv = np.array(list(map(set_new_hue, img_hsv)))
    return result_hsv

def random_hue_image(img_hsv):
    return change_hue_image(img_hsv, random.randrange(0, 360));

def change_saturation(img_hsv, rate:float):
    def low_saturation(row):
        row[:,1] = row[:,1]*rate
        return row
    result_hsv = np.array(list(map(low_saturation, img_hsv)))
    return result_hsv

def dynamic_hue_video(img_hsv, fps:int=30, degree:int=1):
    codec = 'avc1'
    h, w, c = img_hsv.shape
    size = (w, h)
    out = cv2.VideoWriter('./dynamicHue.mp4', cv2.VideoWriter_fourcc(*codec), fps, size)
    for hue_change in range(degree, 360):
        img_new = cv2.cvtColor(change_hue_image(img_hsv, hue_change), cv2.COLOR_HSV2BGR)
        out.write(img_new)
    out.release()
