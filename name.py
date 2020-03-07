import os
import cv2
import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt


path1 = '05wan3/0'
path2 = '05wan3b/0'

clocks = dict()
x_train0 = []
y_train0 = []
for filename in os.listdir(path2):
    if 'git' in filename: continue
    #print(path1)
    #ftimestr,number = path1.split('_')
    clocks[int(filename.split('_')[0])]=int(filename.split('_')[1][:-4])
    #clocks[int(ftimestr)]=int(number)
keys = clocks.keys()
for filename in os.listdir(path1)[0:]:
   # filename = '1582553079436_0.jpg'
    if 'git' in filename: continue
    ftime = int(filename.split('_')[0])
    value = max(filter(lambda t:t<ftime,keys))
#    x_train0.append(cv2.imread(os.path.join(path1,filename), cv2.IMREAD_GRAYSCALE)[:,:,np.newaxis]/255.0)
    y_train0.append(clocks[value])

    #image = cv2.imread(os.path.join('05wan3/0', '1582553079436_0.jpg'),cv2.IMREAD_GRAYSCALE)
    t=0
    image = cv2.imread(os.path.join('05wan3/0', filename),cv2.IMREAD_GRAYSCALE)[49-t:61+t,46-t:58+t]
    gam1= exposure.adjust_gamma(image, 0.5)
    plt.imshow(gam1,cmap=plt.cm.gray)
    #plt.imshow(gam1)
    plt.show()
    break

print(len(x_train0),len(y_train0))
print(y_train0[:10])
