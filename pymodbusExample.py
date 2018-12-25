# based on the example from http://www.solarpoweredhome.co.uk/

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
 
client = ModbusClient(method = 'rtu', port = 'COM3', baudrate = 115200)
client.connect()
 
result = client.read_input_registers(0x3100,16,unit=1)
solarVoltage = float(result.registers[0] / 100.0)
solarCurrent = float(result.registers[1] / 100.0)
batteryVoltage = float(result.registers[4] / 100.0)
chargeCurrent = float(result.registers[5] / 100.0)
loadCurrent= float(result.registers[9] / 100.0)
loadPower= float(result.registers[10] / 100.0)
 
# Do something with the data

print("Solar Voltage: " + str(solarVoltage))

print("Solar Current" + str(solarCurrent))

print("Battery Voltage: " + str(batteryVoltage))

print("Charge Current: " + str(chargeCurrent))
print("Load Current" + str(loadCurrent))
print("Load Power: " + str(loadPower))

client.close()