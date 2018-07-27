import serial
import time

ser = serial.Serial("/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0",9600)

line = ser.readline()
while line:
    print(line.strip())
    line = ser.readline()
    ser.write("hello, I'm Raspberry Pi.\n")      # write a string
ser.close()
