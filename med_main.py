from VGG_classification import VGG_classification as VGGCla

from InputFile import inpuCreate as inpInit


import easygui
import cv2
path1 = easygui.fileopenbox()
iputImg = cv2.imread(path1)
cv2.imshow('Input image ', iputImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
inpInit.InputMain()
