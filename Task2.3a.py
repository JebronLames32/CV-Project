import cv2
import numpy as np
f=open('directionOutputsBonus.txt', 'w')
def matchimage(frame1):
    for i in range(1,16):
        img = cv2.imread((str(i) + '.jpeg'), 0)
        imgnew = cv2.resize(src=img, dsize=(40, 40), interpolation=cv2.INTER_AREA)
        if cv2.matchTemplate(frame1, imgnew, cv2.TM_CCOEFF_NORMED) >= 0.9:
            return i

def disp(j):
    print(j, file=f)
  
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('video2.mp4', fourcc,1, (600, 600))
for j in range(90):
    i=np.random.randint(1,16)
    imgwrite = cv2.imread(str(i) + '.jpeg',1)
    video.write(imgwrite)
    img1 = cv2.resize(src=imgwrite, dsize=(40,40), interpolation=cv2.INTER_AREA)
    img1=cv2.cvtColor(img1 , cv2.COLOR_BGR2GRAY)
    i1=matchimage(img1)
    disp(i1)
    if i==1:
        imgwrite = cv2.imread('2.jpeg',1)
        video.write(imgwrite)
        disp(2)
        j+=1

f.close()
video.release()
