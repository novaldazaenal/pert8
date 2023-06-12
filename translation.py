import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("gambar2.jpeg")
h,w = image.shape[:2]

half_height,half_width = h//4, w//8

transition_matrix =np.float32([[1,0,half_width],[0,1,half_height]])

image_transition = cv.warpAffine(image,transition_matrix,(w,h))

plt.imshow(cv.cvtColor(image_transition,cv.COLOR_BGR2GRAY))
plt.title("Translation")
plt.show()