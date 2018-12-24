import sys
import glob
import serial
import os
import subprocess

ports=glob.glob('/dev/tty[A-Za-z]*')

result=[]

for port in ports:
	try:
		s = serial.Serial(port)
		s.close()
		result.append(port)
	except (OSError, serial.SerialException):
		pass

print('List system ports')
print(result)

try:
	serial_port = serial.Serial('/dev/ttyXRUSB0',115200)
	print('Port is open')
	serial_port.close()
	print('Port is now closed')
except serial.SerialException:
	serial.Serial('/dev/ttyXRUSB0',115200).close()
	print('Port is closed')
	ser = serial.Serial('/dev/ttyXRUSB0',115200)
	print('port is open, again?')


subprocess.call(['python', '-m', 'serial.tools.list_ports'])