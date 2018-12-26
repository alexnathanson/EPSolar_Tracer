#!/usr/bin/env python
import minimalmodbus
import time

minimalmodbus.BAUDRATE = 115200

# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('COM6', 1)

while True:
    # Register number (in decimals), number of decimals, function code
    # the first Tracer register is 0x3100 (12544 in decimal)
    batVoltage = instrument.read_register(12548, 2,4)
    print batVoltage
    time.sleep(1)