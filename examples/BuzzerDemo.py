#import library to access port, PWM and time function
from machine import Pin, PWM
import time

buzzer = PWM(Pin(15)) #define PWM output pin GP15

def playtone(frequency): # function to play tone on buzzer with define frequency
    buzzer.duty_u16(5000)  # HIGH will sound buzzer
    buzzer.freq(frequency)

def bequiet():	# Function to stop buzzer
    buzzer.duty_u16(0) # Low will stop buzzer

while True:
    playtone(1865)
    time.sleep(0.5)
    bequiet()
    time.sleep(0.5)
