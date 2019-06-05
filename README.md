# EPSolar_Tracer
This repo has a few different implementations and tools for communicating with EP Solar Tracer charge controllers.
This has been tested with Tracer model 3210A, but should work with any EP Solar Tracer model that uses Modbus RS485 and MT50 displays.

There are 2 different Modbus libraries for Python that work well, pymodbus and minimalmodbus. Pymodbus is better to use because it has more options. libmodbus is a library for C that others have used with Raspberry Pis.

Because the rs485 converter to USB port implementation for the Raspberry Pi relies on version specific drivers, the Arduino implementation might be more future proof.

## Raspberry Pi Mobel 3 B+

### Via USB port
This works with a USB to RS485 converter (ch340T chip model).

I was not able to get this to work with the manufacturer's recommended cable (Model: CC-USB-RS485-150U) because the EXAR USB drivers would not work with this version of the Raspberry Pi. A number of other people have successfullly used that cable and EXAR drivers with earlier Raspberry Pi models. (EXAR drivers: https://www.exar.com/design-tools/software-drivers)

#### wiring
RJ45 blue => b <br>
RJ45 green => a

#### ch340T specs
* https://hackaday.com/tag/ch340/
* http://fobit.blogspot.com/2014/11/ch340g-in-eagle.html

#### install steps
* sudo apt-get update
* sudo apt-get dist-upgrade
* sudo apt-get install git
* sudo apt-get install python-pip
* pip install pymodbus 
* pip install serial
* git clone  https://github.com/alexnathanson/EPSolar_Tracer.git


#### Misc. Linux port identification commands
* Lsusb
* dmesg
* ls /dev/* | grep XRUSB
* python -m serial.tools.list_ports
* dmesg /dev/ | grep tty
* sudo cat /proc/tty/driver/serial

#### Troubleshooting
If you're trying to use the EXAR driver set the port to the right permissions.
* sudo chmod 777 /dev/ttyXRUSB0

### Via GPIO
This method uses a Max485 and a 5v to 3.3v level shifter. I have not realized this version, but it should be doable if you need to free up USB ports for whatever reason.

Some GPIO resources
* https://learn.sparkfun.com/tutorials/txb0104-level-shifter-hookup-guide?_ga=2.223672476.663927220.1545672234-707983221.1543353897
* https://spellfoundry.com/2016/05/29/configuring-gpio-serial-port-raspbian-jessie-including-pi-3/
* https://www.instructables.com/id/How-to-Use-Modbus-With-Raspberry-Pi/
* https://doc.homegear.eu/data/homegear-homematicwired/configuration.html#config-rs485-serial
* https://www.raspberrypi-spy.co.uk/2018/09/using-a-level-shifter-with-the-raspberry-pi-gpio/
* https://www.raspberrypi.org/documentation/configuration/uart.md

## Arduino Uno & Max485
This works well. It's a pretty easy implementation. I'm using software serial to free up the USB port for serial communication with a computer or whatever you want. In the future I may build it out as a library.

![arduino max485](https://github.com/alexnathanson/EPSolar_Tracer/blob/master/images/arduino_Max485_wiring.jpg)

You can monitor the serial port from the Arduino IDE or serialTest.py (serialTest.py is a simple alternative if you can't get the Tracer to communicate directly with the Raspberry Pi)

This uses the Modbus Master library. https://github.com/4-20ma/ModbusMaster

## Win 10 PC
This is the simplest implementation. It uses the manufacturer recommended RS485 to USB cable (Model: CC-USB-RS485-150U). This also worked with ch340T model.

In device manager right-click on the port and select properties. In the port settings tab make sure RS-485 is checked and the BPS is set to 115200. The other settings I used were databits = 8, parity= None, stopbits = 1

Both minimalmodbus and pymodbus libraries work well with my PC.

## Addition Resources & Prior Work
https://github.com/kasbert/epsolar-tracer <br>
http://www.solarpoweredhome.co.uk/ <br>
https://medium.com/@jcrbcn/installing-the-exar-usb-driver-on-the-raspberrypi-for-teknic-sc-hub-39de533f0502

## Links
Tracer charge controller
https://www.epsolarpv.com/product/3.html

Tracer Modbus Protocol
http://www.solar-elektro.cz/data/dokumenty/1733_modbus_protocol.pdf

