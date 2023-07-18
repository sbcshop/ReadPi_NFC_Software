 # Demo code for 1.3" Display test of ReadPi
from machine import Pin,SPI
import time
import st7789 #library module import of ST7789 display controller 
import vga1_bold_16x32 as font

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)#SPI interface for tft screen

tft.init()
time.sleep(0.5) #wait for half second

while True:
    tft.text(font,"HELLO WORLD!!", 10,40,st7789.YELLOW) # print text on tft screen
    tft.fill_rect(0, 72, 240,5, st7789.RED) #display red line on tft screen

    tft.text(font,"LCD 1.3 SCREEN", 10,120,st7789.CYAN)
    tft.fill_rect(0, 152, 240,5, st7789.GREEN)
    time.sleep(3)
    tft.fill(0)
    time.sleep(1)
