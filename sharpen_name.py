from matplotlib import pyplot as plt
import cv2
import os
from skimage import exposure

filename = '1583081562071_14413.jpg'

image = cv2.imread(os.path.join('05wan8/2',filename),cv2.IMREAD_GRAYSCALE)
gam1= exposure.adjust_gamma(image, 0.5)
#plt.imshow(gam1)

filename = '1583081562510_14414.jpg'
image = cv2.imread(os.path.join('05wan8/2',filename),cv2.IMREAD_GRAYSCALE)
gam2= exposure.adjust_gamma(image, 0.5)

y_train0 = dict()
path2='05wan8b/1'
for fname in os.listdir(path2):
  if 'git' in fname: continue
  y_train0[int(fname[:-4])]=cv2.imread(os.path.join(path2,fname), cv2.IMREAD_GRAYSCALE)/255.0      
  
keys = list(y_train0.keys())
ftime = int(filename.split('_')[0])
value = max(filter(lambda t:t<ftime,keys))
print(abs(ftime-value))
yimg = y_train0[value]

plt.subplot(131)
plt.imshow(gam1,cmap=plt.cm.gray)
plt.subplot(132)
plt.imshow(gam2,cmap=plt.cm.gray)
plt.subplot(133)
plt.imshow(yimg,cmap=plt.cm.gray)
#plt.imshow(gam1)
plt.show()
