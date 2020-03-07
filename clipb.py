import numpy as np
from scipy import ndimage
from skimage.measure import block_reduce, compare_mse
import os
import cv2

PATH = r'05wan13b/0'
OUTPATH = r'05wan13b/4'
#os.rmdir(OUTPATH)
os.mkdir(OUTPATH)
filelist = os.listdir(PATH)

for index, file in enumerate(filelist):
#    if 'git'  in file:continue
    im1 = np.array(cv2.imread(os.path.join(PATH, file)))
    im1 = im1[1134:1226,437:641]
    im1 = np.clip((im1-115)/(250-115),0,1)*255
#    im1 = cv2.resize(im1,(102,46))
    im1 = cv2.resize(im1,(124,56))
    im1 = cv2.resize(im1,(62,28))
#    im1 = cv2.resize(im1,(31,14))
    cv2.imwrite(os.path.join(OUTPATH, file),im1)
    if(index%1000==0):print(str(index) + " : " + file + " complete")
