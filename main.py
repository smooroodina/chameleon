import numpy as np
import cv2
import rainbow

if __name__ == '__main__':
    src = cv2.imread('image.png', cv2.IMREAD_COLOR, )
    src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    src_hsv = rainbow.change_saturation(src_hsv, 5)
    rainbow.dynamic_hue_video(src_hsv, 45, 1)
