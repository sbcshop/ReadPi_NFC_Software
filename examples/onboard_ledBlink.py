#import library to access port and time function
from machine import Pin
from time import sleep

# "LED" or GP25 to select onboard led of Pico W 
Led = Pin("LED", Pin.OUT) 

while True:
    Led.on()  #To switch on LED
    sleep(2)  # wait 2 second
    print("LED is ON")
    
    Led.off() #To switch off LED
    sleep(2)  #wait 2 second
    print("LED is OFF")
