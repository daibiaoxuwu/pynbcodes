from matplotlib import pyplot as plt
import numpy as np
from scipy import ndimage
import os
import cv2


PATH = '05wan13b/0'
filelist = os.listdir(PATH)
sums = []
pics = []
for index,filename in enumerate(filelist[:100]):
    if 'git' in filename:continue
    ans = np.array(cv2.imread(os.path.join(PATH, filename)))[1130:1230,429:649]
    pics.append(ans)
pics = np.stack(pics)
print(np.percentile(pics,10))
print(np.percentile(pics,90))
