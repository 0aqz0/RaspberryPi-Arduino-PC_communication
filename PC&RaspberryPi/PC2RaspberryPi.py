#coding:utf-8
import serial
import time

ser = serial.Serial("COM6",9600)

while True:
    ser.write("Hello, I'm PC.\n")      # write a string
    print("I receive：")
    line = ser.readline()
    print(line.strip())
    time.sleep(2)
ser.close()
