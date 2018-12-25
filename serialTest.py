# read from Arduino connection over USB

import serial

ser = serial.Serial('COM5',115200)
s = [0]
while True:
	read_serial=ser.readline()
	s[0] = str(ser.readline())
	print s[0]
	print (read_serial)