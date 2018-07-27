import serial
import time

ser = serial.Serial("/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0",9600)

while True:
    ser.write("Hello, I'm Raspberry Pi.\n")
    print("I receive: ")
    line = ser.readline()
    print(line.strip())
    time.sleep(2)
ser.close()