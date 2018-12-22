#!/usr/bin/env python
import minimalmodbus
import time

minimalmodbus.BAUDRATE = 115200

# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('COM3', 1)

while True:
    # Register number (in decimals), number of decimals, function code
    temperature = instrument.read_register(12545, 2,4)
    print temperature
    time.sleep(1)