#coding:utf-8
import time 
import serial

ser = serial.Serial("COM5",9600)
line = ser.readline() 
while line: 
    print(line.strip()) 
    line = ser.readline()
    sep  = int(time.strftime("%S")) % 10
    if sep == 0:
        ser.write("hello, the time is : " + time.strftime("%Y-%m-%d %X\n"))      # write a string
ser.close()