'''
Demo program to see how to read and write NFC tag
For the demo to run successfully you need to add lib file into Pico W :
https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/examples/nfc.py

'''
from machine import UART,Pin,SPI,PWM, I2C
from nfc import NFC
import utime,time
import st7789 #library of TFT display controller uses SPI interface
import vga1_bold_16x32 as font
import os

buzzer = PWM(Pin(15)) # buzzer pin connected to GPIO15

def playtone(frequency):
    buzzer.duty_u16(5000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)
    
data = '1B233A49' # must be 4 byte, for write
baudrate = 9600	 # communication buadrate between pico W and NFC module
page_no = '15'    # memory location divided into pages NTAG213/215/216 -> 4bytes per page
nfc = NFC(baudrate) #create object

#define and configure SPI for Display
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)#SPI interface for tft screen

tft.init() #initialize display
tft.fill(0) # clear display
tft.text(font,"Hello!", 70,100,st7789.CYAN)# print on tft screen
time.sleep(1) #wait for 1 second

while 1:
        status = nfc.Data_write(data,page_no) # Write data to Tag
        
        if status == "Card write sucessfully":
            tft.fill(0)
            playtone(1865)
            dataRec = nfc.data_read(page_no) # Read Tag data written initially
            print("Received data = ",dataRec)
            tft.text(font,str(dataRec), 50,120,st7789.WHITE)# print on tft screen
            time.sleep(0.5)
            bequiet()
        else :
            tft.fill(0)
            tft.text(font,"SCAN CARD", 40,60,st7789.YELLOW)# print on tft screen
            tft.text(font,"Please!", 60,120,st7789.YELLOW)# print on tft screen
        
        time.sleep(0.5)
        



