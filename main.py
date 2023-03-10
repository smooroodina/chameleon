import numpy as np
import cv2
import rainbow

if __name__ == '__main__':
    src = cv2.imread('./img/image.png', cv2.IMREAD_COLOR, )
    src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    src_hsv = rainbow.change_saturation(src_hsv, 1)
    rainbow.dynamic_hue_video('./img//dynamicHue_low.mp4', src_hsv, 45, 1)
