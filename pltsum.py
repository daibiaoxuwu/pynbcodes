from matplotlib import pyplot as plt
import numpy as np
from scipy import ndimage
import os
import cv2


PATH = '05wan11/0'
filelist = os.listdir(PATH)
sums = []
size=11
for index,filename in enumerate(filelist[:100]):
    if 'git' in filename:continue
    ans = np.array(cv2.imread(os.path.join(PATH, filename)))
    ans = np.clip((ans-np.percentile(ans,10))/(np.percentile(ans,90)-np.percentile(ans,10)),0,1)
    for i in range(0,22-size):
        for j in range(0,52-size):
            sums.append(np.sum(ans[i:i+size,j:j+size]))
    if index%1000==0:
        print(index)
        
plt.hist(sums)
plt.show()
