import numpy as np
from scipy import ndimage
from skimage.measure import block_reduce, compare_mse
import os
import cv2

PATH = r'05wan14/0'
OUTPATH = r'05wan14/1'
#os.rmdir(OUTPATH)
os.mkdir(OUTPATH)
filelist = os.listdir(PATH)

for index, file in enumerate(filelist):
    if 'git'  in file:continue
    im1 = np.array(cv2.imread(os.path.join(PATH, file)))
    im1 = im1[52:66,39:70]#[50:64,40:71]
    cv2.imwrite(os.path.join(OUTPATH, file),im1)
    if(index%1000==0):print(str(index) + " : " + file + " complete")

