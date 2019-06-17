# based on the example from http://www.solarpoweredhome.co.uk/

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from time import sleep
import datetime
import numpy as np
import pandas as pd
import csv
import os

client = ModbusClient(method = 'rtu', port = '/dev/ttyUSB0', baudrate = 115200)
client.connect()

fileName = 'data/tracerData'+str(datetime.date.today)+'.csv'

while True:
	result = client.read_input_registers(0x3100,16,unit=1)

	solarVoltage = float(result.registers[0] / 100.0)
	solarCurrent = float(result.registers[1] / 100.0)
	batteryVoltage = float(result.registers[4] / 100.0)
	chargeCurrent = float(result.registers[5] / 100.0)
	loadCurrent= float(result.registers[9] / 100.0)
	loadPower= float(result.registers[10] / 100.0)
 	
	# Do something with the data

	print("PV Voltage: " + str(solarVoltage))

	print("PV Current" + str(solarCurrent))

	print("Battery Voltage: " + str(batteryVoltage))

	print("Charge Current: " + str(chargeCurrent))
	print("Load Current" + str(loadCurrent))
	print("Load Power: " + str(loadPower))
	currentDate = datetime.datetime.now()
	print("Local time: " + str(currentDate))

	s = pd.Series([solarVoltage, solarCurrent, batteryVoltage, chargeCurrent, loadCurrent, loadPower, currentDate])


	# check if the file already exists
 	try:
		with open(fileName, mode='w') as csvfile:
	    	readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				print(row)
				print(row[0])
		        print(row[0],row[1],row[2],)
	except:
		print("first file of the day!")

		df = pandas.DataFrame(data={"PV voltage": solarVoltage, "PV current": solarCurrent})
		df.to_csv("./file.csv", sep=',',index=False)

	sleep(20)

client.close()