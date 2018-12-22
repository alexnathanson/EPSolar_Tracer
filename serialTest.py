import serial

ser = serial.Serial('/dev/ttyAMA0',115200)
s = [0]
while True:
	read_serial=ser.readline()
	s[0] = str(ser.readline())
	print s[0]
	print (read_serial)