import numpy as np
import cv2
import time

img=cv2.imread('map1.2.png',0)
q=880
p=145
d=851
c=229
b=359
a=563
n, m = img.shape

cv2.namedWindow('Image1', cv2.WINDOW_NORMAL)
cv2.imshow('Image1', img)
img[a][b] = 255
print(b,a)
print(d,c)

path1=[]
path2=[]
count=0
z=n*n
value=[z,z,z,z,z,z,z,z]
end=0
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
def astar(i,j,c,d):
    global end, count
    if end==0:
        while(i,j!=c,d):
            img[i,j]=127
            value=[z,z,z,z,z,z,z,z]
            path1.append(i)
            path2.append(j)
            cv2.imshow('Image', img)
            cv2.waitKey(10)
            if(i-1>=0):
                if((i-1,j)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d,c,d)
                elif(img[i-1,j]==255):
                    g=2
                    h=(c-i+1)**2+(d-j)**2
                    f=g+h
                    value[0]=f

            if(j-1>=0):
                if((i,j-1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d,c,d)
                elif(img[i,j-1]==255):
                    g=2
                    h=(c-i)**2+(d-j+1)**2
                    f=g+h
                    value[1]=f
                    
            if(i+1<n):
                if((i+1,j)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d,c,d)
                elif(img[i+1,j]==255):
                    g=2
                    h=(c-i-1)**2+(d-j)**2
                    f=g+h
                    value[2]=f
                    
            if(j+1<m):
                if((i,j+1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d,c,d)
                elif(img[i,j+1]==255):
                    g=2
                    h=(c-i)**2+(d-j-1)**2
                    f=g+h
                    value[3]=f
                    

            if(j+1<m and i+1<n):
                if((i+1,j+1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d,c,d)
                elif(img[i+1,j+1]==255):
                    g=1
                    h=(c-i-1)**2+(d-j-1)**2
                    f=g+h
                    value[4]=f

            if(j+1<m and i-1>=0):
                if((i-1,j+1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d,c,d)
                elif(img[i-1,j+1]==255):
                    g=1
                    h=(c-i+1)**2+(d-j-1)**2
                    f=g+h
                    value[5]=f

            if(i+1<n and j-1>=0):
                if((i+1,j-1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d,c,d)
                elif(img[i+1,j-1]==255):
                    g=1
                    h=(c-i-1)**2+(d-j+1)**2
                    f=g+h
                    value[6]=f

            if(j-1>=0 and i-1>=0):
                if((i-1,j-1)==(c,d)):
                    print("complete")
                    end=1
                    astar(c,d,c,d)
                elif(img[i-1,j-1]==255):
                    g=1
                    h=(c-i+1)**2+(d-j+1)**2
                    f=g+h
                    value[7]=f  
            
            
            

            minpos=value.index(min(value)) 
            if minpos==0:
                astar(i-1,j,c,d)
            elif minpos==1:
                astar(i,j-1,c,d)
            elif minpos==2:
                astar(i+1,j,c,d)
            elif minpos==3:
                astar(i,j+1,c,d)
            elif minpos==4:
                img[i+1,j+1]=127
                astar(i+1,j+1,c,d)
            elif minpos==5:
                img[i-1,j+1]=127
                astar(i-1,j+1,c,d)
            elif minpos==6:
                img[i+1,j-1]=127
                astar(i+1,j-1,c,d)
            elif minpos==7:
                img[i-1,j-1]=127
                astar(i-1,j-1,c,d)
            break
    
    else:
        print("final complete")
begin=time.time()       
astar(a,b,c,d)
end=0
astar(c,d,p,q)
end=time.time()
l=len(path1)
print("distance=", l)
print("time=",end-begin)
img1=cv2.imread('map1.2.png')
cv2.namedWindow('Image1', cv2.WINDOW_NORMAL)
for k in range(l):
    img1[path1.pop(),path2.pop()]=(0,255,0)
    cv2.imshow('Image1', img1)
    cv2.waitKey(20)

cv2.waitKey(0)
cv2.destroyAllWindows
                        
