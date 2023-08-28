'''
Demo program to see how to read and write NFC tag
For the demo to run successfully you need to add lib file into Pico W :
https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/examples/nfc.py

'''
from machine import UART,Pin,SPI,PWM, I2C
import time,utime
from nfc import NFC
import os

    
data = '1B233A49' # must be 4 byte, for write
baudrate = 9600	 # communication buadrate between pico W and NFC module
page_no = '15'    # memory location divided into pages NTAG213/215/216 -> 4bytes per page
nfc = NFC(baudrate) #create object
time.sleep(1) #wait for 1 second

while 1:
        status = nfc.Data_write(data,page_no) # Write data to Tag
        
        if status == "Card write sucessfully":
            dataRec = nfc.data_read(page_no) # Read Tag data written initially
            print("Received data = ",dataRec)
            time.sleep(0.5)
        else :
            print("Scan Card Please!")
        
        time.sleep(0.5)
