# EPSolar_Tracer
This repo has a few different implementations and tools for communicating with EP Solar Tracer charge controllers.
This has been tested with model 3210A, but should work with any EP Solar Tracer model that uses Modbus RS485 and MT50 displays

## Raspberry Pi Mobel 3 B+
I do not have a successful standalone Raspberry Pi 3 B+ version yet, but am continueing to work on it. There are a few examples of people who have realized this project in the past, but I haven't seen anyone specifically succeed with this specific Pi using Raspian Stretch... You can easily connected the Pi to an Arduino via a USB cable.

### install steps
* sudo apt-get install git
* sudo apt-get install python-pip
* pip install pymodbus
* pip install serial

## Arduino Uno + Max485
This works well. It's a pretty easy implementation. I'm using software serial to free up the USB port for serial communication with a computer or whatever you want. In the future I may build it out as a library.

You can monitor the serial port from the Arduino IDE or serialTest.py

## Win 10 PC
This is the simplest implementation. Uses a RS485 to USB cable. In the 

## Resources & Prior Work
https://github.com/kasbert/epsolar-tracer <br>
http://www.solarpoweredhome.co.uk/

## Links
Tracer charge controller
https://www.epsolarpv.com/product/3.html

Tracer Modbus Protocol
http://www.solar-elektro.cz/data/dokumenty/1733_modbus_protocol.pdf

