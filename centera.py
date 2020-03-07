import numpy as np
from scipy import ndimage
from skimage.measure import block_reduce, compare_mse
import matplotlib.pyplot as plt
import os
import cv2
import random
PATH = r'05wan14/0'
filelist = os.listdir(PATH)
random.shuffle(filelist)
pics=[]
for index, file in enumerate(filelist[:200]):
    if 'git'  in file:continue
    pics.append(np.array(cv2.imread(os.path.join(PATH, file)))[52:66,39:70,0])
pic = np.sum(pics,axis=0)
plt.imshow(pic)
plt.colorbar()
plt.show()
