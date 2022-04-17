import cv2
import numpy as np
import serial
import time

arduino = serial.Serial(port='COM4' , baudrate = 9600 , timeout = .1)
#Arduino and Python is connected by Serial Communication

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    
def matchimage(frame1):
    for i in range(1, 16):
        img = cv2.imread((str(i) + '.jpeg'), 0)
        imgnew = cv2.resize(src=img, dsize=(40, 40), interpolation=cv2.INTER_AREA)
        if cv2.matchTemplate(frame1, imgnew, cv2.TM_CCOEFF_NORMED) >= 0.9:
            return i
        
def disp(j):
    print(j, file=f)
    
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('video2.mp4', fourcc, 1, (600, 600))
for j in range(90):
    i = np.random.randint(1, 16)
    imgwrite = cv2.imread(str(i) + '.jpeg', 1)
    video.write(imgwrite)
    img1 = cv2.resize(src=imgwrite, dsize=(40, 40), interpolation=cv2.INTER_AREA)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    i1 = matchimage(img1)
    disp(i1)
    write_read(f.readline())
    time.sleep(1.01)
    if i == 1:
        imgwrite = cv2.imread('2.jpeg', 1)
        video.write(imgwrite)
        disp(2)
        j += 1

f.close()
video.release()
