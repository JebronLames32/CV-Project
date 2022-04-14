import cv2
import numpy as np
  
  
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('video1.mp4', fourcc,1, (600, 600))
for j in range(90):
    i=np.random.randint(1,16)
    img = cv2.imread(str(i) + '.jpeg',1)
    video.write(img)
    if i==1:
        img = cv2.imread('2.jpeg',1)
        video.write(img)
        j+=1
cv2.destroyAllWindows()
video.release()