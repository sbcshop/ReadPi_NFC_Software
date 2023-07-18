 # Demo code for 1.3" Display and Joystick
from machine import Pin,SPI
import time
import st7789 #library module import of ST7789 display controller 
import vga1_bold_16x32 as font


joyRight = Pin(14,Pin.IN, Pin.PULL_UP)
joyLeft  = Pin(21,Pin.IN, Pin.PULL_UP)
joyUp   = Pin(22,Pin.IN, Pin.PULL_UP)
joyDown  = Pin(26,Pin.IN, Pin.PULL_UP)  
joySel    = Pin(27,Pin.IN, Pin.PULL_UP)  

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)#SPI interface for tft screen

def displayTest():
    tft.init()
    time.sleep(0.5)#time delay
    tft.text(font,"1.3\" Display", 10,40,st7789.YELLOW)# print on tft screen
    tft.fill_rect(0, 70, 240,5, st7789.RED)#display red line on tft screen
    
    tft.text(font,"SB Components", 10,120,st7789.WHITE)
    tft.fill_rect(0, 150, 240,5, st7789.CYAN)
    
time.sleep(1)

displayTest()

while True:
    #get current value of buttons, 0 - when pressed and 1 - when released 
    val1 =  joyUp.value()
    val2 = joyDown.value()
    val3 = joyLeft.value()
    val4 = joyRight.value()
    val5 = joySel.value()

    if val1 == 0:
        print("JY-RIGHT, val1 = ",val1)
        tft.text(font,"JY-RIGHT", 10,180,st7789.WHITE)
    elif val2 == 0:
        print("JY-DOWN, val2 = ",val2)
        tft.text(font,"JY-DOWN", 10,180,st7789.WHITE)
    elif val3 == 0:
        print("JY-LEFT, val3 = ",val3)
        tft.text(font,"JY-LEFT", 10,180,st7789.WHITE)
    elif val4 == 0:
        print("JY-UP, val4 = ",val4)
        tft.text(font,"JY-UP", 10,180,st7789.WHITE)
    elif val5 == 0:
        print("JY-Sel, val5 = ",val5)
        tft.text(font,"JY-Sel", 10,180,st7789.WHITE)
    else :
        tft.text(font,"             ", 10,180,st7789.WHITE)
        
    time.sleep(0.2)
        
