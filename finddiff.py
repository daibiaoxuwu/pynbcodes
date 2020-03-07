from skimage.measure import block_reduce, compare_mse
import numpy as np
from scipy import ndimage
from skimage.measure import block_reduce, compare_mse
import os
import cv2


PATH = '05wan11/0'
filelist = os.listdir(PATH)
baseimg = np.array(cv2.imread(os.path.join(PATH, filelist[0])),dtype=np.uint8)
maxd = 0
maxpic = ''
for index,filename in enumerate( filelist):
    if 'git' in filename:continue
    imgnew = np.array(cv2.imread(os.path.join(PATH, filename)),dtype=np.uint8)
    diff = compare_mse(baseimg, imgnew)
    if diff>maxd:
        maxd = diff
        maxpic = filename
    if index%1000==0:
        print(index)
    del imgnew
imgnew = np.array(cv2.imread(os.path.join(PATH, maxpic)))
cv2.imwrite('diff_'+maxpic,imgnew)
print(maxpic)

