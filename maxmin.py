import cv2
import os
import numpy as np

image = cv2.imread(os.path.join('', '1583322722474.jpg'))
print(np.max(image),np.min(image))
