import cv2
# import numpy as np

vi = cv2.VideoCapture('video1.mp4')
cv2.namedWindow('Frame' , cv2.WINDOW_NORMAL)
ct =0
f=open('directionOutputs.txt', 'w')
def matchimage(frame1):
    for i in range(1,16):
        img = cv2.imread((str(i) + '.jpeg'), 0)
        imgnew = cv2.resize(src=img, dsize=(40, 40), interpolation=cv2.INTER_AREA)
        if cv2.matchTemplate(frame1, imgnew, cv2.TM_CCOEFF_NORMED) >= 0.9:
            return i
            break
def disp(j):
    if j==1:
        print("stop motors", file=f)
    elif j==2:
        print("move forward. Speed=40", file=f)
    elif j==3:
        print("right turn", file=f)
    elif j==4:
        print("left turn", file=f)
    elif j==5:
        print("U turn", file=f)
    elif j==6 :
        print("Hospital zone. Speed=25", file=f)
    elif j==7 :
        print("Hump ahead. Decelerate", file=f)
    elif j == 8 :
        print("Speed=30", file=f)
    elif j==9:
        print("Speed=20", file=f)
    elif j==10:
        print("School ahead. Speed=20", file=f)
    elif j==11:
        print("Stop motors", file=f)
    elif j==12:
        print("keep moving", file=f)
    elif j==13:
        print("Animal crossing zone. Speed=15", file=f)
    elif j==14 :
        print("Right curve. RightSpeed=30 Leftspeed=20", file=f)
    elif j==15 :
        print("Left curve. LeftSpeed=30 Rightspeed=20", file=f)

while(True) :
    ret,frame = vi.read()
    if ret :
        ct+=1
        frame11 = cv2.resize(src=frame, dsize=(40,40), interpolation=cv2.INTER_AREA)
        frame1=cv2.cvtColor(frame11 , cv2.COLOR_BGR2GRAY)
        i1 = matchimage(frame1)
        disp(i1)
        cv2.imshow('Frame' , frame)
        cv2.waitKey(100)
    else :
        break
print(ct)
f.close()
cv2.destroyAllWindows()