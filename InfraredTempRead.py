from RPLCD.i2c import CharLCD
import smbus
import time

class IRTempSensor():
 
    MLX90614_TA    = 0x06
    MLX90614_TOBJ1 = 0x07
 
    def __init__(self, address = 0x5a, bus = 1):
        self.address = address
        self.bus = smbus.SMBus(bus)
 
    def readValue(self, registerAddress):
        error = None
        for i in range(3):
            try:
                return self.bus.read_word_data(self.address, registerAddress)
            except IOError as e:
                error = e
                time.sleep(0.1)
        raise error
 
    def valueToCelcius(self, value):
        return -273.15 + (value * 0.02)
 
    def readObjectTemperature(self):
        value = self.readValue(self.MLX90614_TOBJ1)
        return self.valueToCelcius(value)
 
    def readAmbientTemperature(self):
        value = self.readValue(self.MLX90614_TA)
        return self.valueToCelcius(value)


def Run():
    
    while True:

        lcd.clear()

        lcd.write_string("Temperatur:\r\n")# \r geht zum anfang / \n geht eine zeite tiefer
        #lcd.cursor_pos = (1, 12)# (Zeile, Charakter) Setze Curser in neue Zeile
        lcd.write_string(TempSensor.readObjectTemperature())
        time.sleep(5)

TempSensor = IRTempSensor(bus=1)
 
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=0, cols=16, rows=2, dotsize=8)

Run()