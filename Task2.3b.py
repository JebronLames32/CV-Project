import serial
import time
f=open('directionOutputsBonus.txt', 'r')

arduino = serial.Serial(port='COM4' , baudrate = 9600 , timeout = .1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
for i in range(93):
    str = f.readline()
    print(str)
    #sp=int(str)
    write_read(str)
    time.sleep(1.01)
f.close()