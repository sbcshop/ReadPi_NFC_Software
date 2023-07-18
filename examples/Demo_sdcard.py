'''
Demo to test sdcard read and write operation
To run this code successfully you will have to add library sdcard.py 
#https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/examples/sdcard.py
'''

from machine import Pin, SPI
import time,utime
import sdcard
import os

#function performs detection, write and read operation on micro SDcard
def sdtest(data):
    spi=SPI(0,sck=Pin(18),mosi=Pin(19),miso=Pin(16)) #define and configure sdcard SPI interfacing
    sd=sdcard.SDCard(spi,Pin(17))
    vfs = os.VfsFat(sd) 
    os.mount(vfs, "/fc")   # mount SD card
    print("Filesystem check")
    
    print(os.listdir("/fc")) # list directories present in sdcard

    fn = "/fc/File.txt"		#create file with suitable name
    print()
    print("Single block read/write")
    with open(fn, "a") as f:
        n = f.write(data)		#write data to file
        print(n, "bytes written") 

    with open(fn, "r") as f:
        result2 = f.read()		#read data from file
        print(len(result2), "bytes read\n")
        print("Data written on File:")
        print(result2)

    os.umount("/fc")
    
sdtest('Hello World!!\n')
print("Done operation on SD Card")

while 1:
    time.sleep(1)
  
