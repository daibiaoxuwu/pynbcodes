from matplotlib import pyplot as plt
import cv2
import os
from skimage import exposure


image = cv2.imread(os.path.join('', '1583322722474.jpg'),cv2.IMREAD_GRAYSCALE)
gam1= exposure.adjust_gamma(image, 0.5)
plt.imshow(gam1,cmap=plt.cm.gray)
#plt.imshow(gam1)
plt.show()
