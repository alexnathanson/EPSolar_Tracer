# pymodbus code based on the example from http://www.solarpoweredhome.co.uk/

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from time import sleep
import datetime
import numpy as np
import pandas as pd
import csv
import os

fileName = 'data/tracerData'+str(datetime.date.today())+'.csv' 

client = ModbusClient(method = 'rtu', port = '/dev/ttyUSB0', baudrate = 115200)
client.connect()


while True:
	result = client.read_input_registers(0x3100,16,unit=1)

	solarVoltage = float(result.registers[0] / 100.0)
	solarCurrent = float(result.registers[1] / 100.0)
	batteryVoltage = float(result.registers[4] / 100.0)
	chargeCurrent = float(result.registers[5] / 100.0)
	loadCurrent= float(result.registers[9] / 100.0)
	loadPower= float(result.registers[10] / 100.0)
 	
	# Do something with the data
'''
	print("PV Voltage: " + str(solarVoltage))

	print("PV Current" + str(solarCurrent))

	print("Battery Voltage: " + str(batteryVoltage))

	print("Charge Current: " + str(chargeCurrent))
	print("Load Current" + str(loadCurrent))
	print("Load Power: " + str(loadPower))
	currentDate = datetime.datetime.now()
	print("Local time: " + str(currentDate))
'''
	#s = pd.Series([solarVoltage, solarCurrent, batteryVoltage, chargeCurrent, loadCurrent, loadPower, currentDate])


	newDF = pd.DataFrame(data={"PV voltage": [solarVoltage],
		"PV current": [solarCurrent],
		"battery voltage":[batteryVoltage],
		"charge current":[chargeCurrent],
		"load current": [loadCurrent],
		"load power": [loadPower],
		"time": [currentDate]})

	# check if the file already exists
 	try:
		with open(fileName) as csvfile:
			df = pd.read_csv(fileName)
			print(df)
			df = df.append(newDF, ignore_index = True)
			df.to_csv(fileName, sep=',',index=False)
			#print("It exists!")
	except:
		print("first file of the day!")
		newDF.to_csv(fileName, sep=',',index=False)

	#runs every minute
	sleep(60)

client.close()