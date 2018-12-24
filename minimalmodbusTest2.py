import minimalmodbus
import serial

usbDevice = '/dev/ttyUSB0'

modbusSlaveID = 1

# can be 'ascii' or 'rtu'
modbusFormat = 'rtu'

#in hexadecimal its 0x3100
registerToRead = 12544

# 3 is for Holding Registers, 4 is for Input Registers
functionCode = 3

# initialize the device
device = minimalmodbus.Instrument(usbDevice, modbusSlaveID, modbusFormat)

# set the various options, which will depend on the device you are communicating with
device.debug = True
device.serial.baudrate = 115200
device.serial.bytesize = 8
device.serial.parity = serial.PARITY_NONE
device.serial.stopbits = 1
device.serial.timeout = 2   # seconds

print device.read_register(registerToRead, functioncode=functionCode)