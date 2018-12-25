/*tracerRegisters
  This program is based off of RS485_HalfDuplex.ino found at
  https://github.com/4-20ma/ModbusMaster/blob/master/examples/RS485_HalfDuplex/RS485_HalfDuplex.ino
  
  RS485_HalfDuplex.pde - example using ModbusMaster library to communicate
  with EPSolar LS2024B controller using a half-duplex RS485 transceiver.

  This example is tested against an EPSolar LS2024B solar charge controller.
  See here for protocol specs:
  http://www.solar-elektro.cz/data/dokumenty/1733_modbus_protocol.pdf

  Library:: ModbusMaster
  Author:: Marius Kintel <marius at kintel dot net>

  Copyright:: 2009-2016 Doc Walker

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

*/


/*
    We're using a MAX485-compatible RS485 Transceiver.

  In order to allow for Modbus communication and serial communication with the Arduino Uno,
  we're using software serial.Rx/Tx is hooked up to the software serial port at RX=10 & TX=11.
  The Data Enable and Receiver Enable pins are hooked up at DE = 3 & RE = 2.

  Wiring
  MAX485=>Arduino Uno
  GND => GND
  VCC => 5V
  DI => 11
  DE => 3
  RE => 2
  RO => 10

  TRACER => MAX485
  blue => B
  green => A
*/
#include <TracerRegisters.h> // empty library for potential future use

#include <ModbusMaster.h>
#include <SoftwareSerial.h>

SoftwareSerial myserial(10, 11); // RX, TX


#define MAX485_DE      3
#define MAX485_RE_NEG  2

// instantiate ModbusMaster object
ModbusMaster node;

// not needed...
float batVolt;
float batPercentage = 0.0;

int outputValue1 = 0;
int countIt = 0;

void preTransmission()
{
  digitalWrite(MAX485_RE_NEG, 1);
  digitalWrite(MAX485_DE, 1);
}

void postTransmission()
{
  digitalWrite(MAX485_RE_NEG, 0);
  digitalWrite(MAX485_DE, 0);
}

void setup()
{
  pinMode(MAX485_RE_NEG, OUTPUT);
  pinMode(MAX485_DE, OUTPUT);
  // Init in receive mode
  digitalWrite(MAX485_RE_NEG, 0);
  digitalWrite(MAX485_DE, 0);

  // Modbus communication runs at 115200 baud

  //Tracer connection
  myserial.begin(115200); 

  //USB Serial connection
  Serial.begin(115200);

  // Modbus slave ID 1
  node.begin(1, myserial);
  
  // Callbacks allow us to configure the RS485 transceiver correctly
  node.preTransmission(preTransmission);
  node.postTransmission(postTransmission);

}

//was true
bool state = true;

void loop()
{
  // uint8_t is short hand for a byte or an integer of length 8 bits
  uint8_t result;
  uint16_t data[6];

  // Read 16 registers starting at 0x3100)
  result = node.readInputRegisters(0x3100, 16);
  if (result == node.ku8MBSuccess)
  {

   
//check battery voltage and turn off output as needed
    batVolt = node.getResponseBuffer(0x04)/100.0f;
    if (batVolt >= 12)
    {
      state = true;
        // Toggle the coil at address 0x0002 (Manual Load Control)
      result = node.writeSingleCoil(0x0002, state);
     } else {
        state = false;
       result = node.writeSingleCoil(0x0002, state);
     }

      // print data
    Serial.println("Tracer CC Data:");
    
    //PV array voltage
     Serial.print("PV Voltage: ");
    Serial.println(node.getResponseBuffer(0x0)/100.0f);

     //PV array current
     Serial.print("PV Current: ");
    Serial.println(node.getResponseBuffer(0x01)/100.0f);

    
     //PV array rated power
     Serial.print("PV Power L: ");
    Serial.println(node.getResponseBuffer(0x02)/100.0f);

     //PV array power
     Serial.print("PV Power H: ");
    Serial.println(node.getResponseBuffer(0x03)/100.0f);

    //battery voltage
    Serial.print("Vbatt: ");
    Serial.println(batVolt);

     //Charging current to battery
     Serial.print("Battery charging current: ");
    Serial.println(node.getResponseBuffer(0x05)/100.0f);

  //Charging current to battery
     Serial.print("Battery charging power L: ");
    Serial.println(node.getResponseBuffer(0x06)/100.0f);

    
  //Charging current to battery
     Serial.print("Battery charging power H: ");
    Serial.println(node.getResponseBuffer(0x07)/100.0f);
    
    // load voltage
    Serial.print("load voltage: ");
    Serial.println(node.getResponseBuffer(0x0C)/100.0f);

    // load current
    Serial.print("load current: ");
    Serial.println(node.getResponseBuffer(0x0D)/100.0f);

    // instantaneous Watts (power) of load
    Serial.print("load power: ");
    Serial.println(node.getResponseBuffer(0x0E)/100.0f);
  }

 // Read 16 registers starting at 0x3110)
  result = node.readInputRegisters(0x3110, 16);
  if (result == node.ku8MBSuccess)
  {
   Serial.print("Bat temp: ");
        Serial.println(node.getResponseBuffer(0x00)/100.0f);

    Serial.print("Battery Percentage: ");
    Serial.println(node.getResponseBuffer(0x0A)/100.0f);
  }

   result = node.readInputRegisters(0x3300, 16);
  if (result == node.ku8MBSuccess)
  {
   Serial.print("Max PV input voltage today: ");
        Serial.println(node.getResponseBuffer(0x00)/100.0f);

    Serial.print("Min PV input voltage today: ");
        Serial.println(node.getResponseBuffer(0x01)/100.0f);

     Serial.print("Max battery voltage today: ");
        Serial.println(node.getResponseBuffer(0x02)/100.0f);

    Serial.print("Min battery input voltage today: ");
        Serial.println(node.getResponseBuffer(0x03)/100.0f);
 
  }


  
  delay(1000);
}

