import cv2
import numpy as np
from collections import deque
import time
import sys

sys.setrecursionlimit(1700)

img=cv2.imread('map1.2.png',0)
b=880
a=145
d=359
c=563
x,y=img.shape
img[a][b] = 128
img[c][d] = 200
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)


stack1=deque()
stack2=deque()

def check(i,j):
    if(img[i,j]==128):
        print("complete")
        dfs(i,j)
    elif(img[i,j]==255):
        dfs(i,j)
        
ct=0
def dfs(i,j):
    global ct
    if img[i,j]!=128:
            ct+=1
            img[i,j]=127
            stack1.append(i)
            stack2.append(j)
            cv2.imshow('Image', img)
            cv2.waitKey(2)
            if(j+1<y):
                if(img[i,j+1]==128):
                    print("complete")
                    dfs(i,j+1)
                elif(img[i,j+1]==255):
                    dfs(i,j+1)
                        
            if(i-1)>=0:
                if(img[i-1,j]==128):
                    print("complete")
                    dfs(i-1,j)
                elif(img[i-1,j]==255):
                    dfs(i-1,j)


            if(j-1)>=0:
                if(img[i,j-1]==128):
                    print("complete")
                    dfs(i,j-1)
                elif(img[i,j-1]==255):
                    dfs(i,j-1)

            if(i+1<x):
                if(img[i+1,j]==128):
                    print("complete")
                    dfs(i+1,j)
                elif(img[i+1,j]==255):
                    dfs(i+1,j)
            
            stack1.pop()
            stack2.pop()

    
    else:
        print("complete")
        l1=len(stack1)
       
        print("distance=", l1)
        end=time.time()
        print("time=",end-begin)
        img1=cv2.imread('map1.2.png')
        cv2.namedWindow('Image1', cv2.WINDOW_NORMAL)
        for k in range(l1):
            img1[stack1.pop(),stack2.pop()]=(0,0,255)
            cv2.imshow('Image1', img1)
            cv2.waitKey(2)
        cv2.waitKey(0)
        exit()
            
begin=time.time()
dfs(c,d)
cv2.destroyAllWindows()
