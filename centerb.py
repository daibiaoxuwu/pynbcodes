import numpy as np
from scipy import ndimage
from skimage.measure import block_reduce, compare_mse
import matplotlib.pyplot as plt
import os
import cv2
import random
PATH2 = r'05wan14b/0'
filelist = os.listdir(PATH2)
random.shuffle(filelist)
pics=[]
for index, file in enumerate(filelist[:200]):
    if 'git'  in file:continue
    pics.append(np.array(cv2.imread(os.path.join(PATH2, file)))[1134:1226,437:641,0])
pic = np.sum(pics,axis=0)
plt.imshow(pic)
plt.colorbar()
plt.show()
