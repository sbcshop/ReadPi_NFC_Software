# ReadPi_NPC_Software
<img src="https://cdn.shopify.com/s/files/1/1217/2104/files/readpi_1BANNER.jpg?v=1689673444">

ReadPi 13.56 MHz frequency based NFC Reader/Writer powered by Raspberry Pi Pico W unit. 
This github provides getting started guide and other working details for ReadPi NFC version.

### Features:
- Powered by Raspberry Pi Pico W microcontroller  board 
- Onboard 13.56MHz NFC read/write Module
- 1.3” Display for visual interaction
- TF card slot for storage and data transfer
- Drag- and- drop programming using mass storage over USB
- Multifunction GPIO breakout supporting general I/O, UART, I2C, SPI, ADC & PWM function.
- Multi- tune Buzzer to add audio alert into project
- Onboard 5-Way Joystick allows better control- related projects
- Status LED for board power, charging and Tag Scan indication 
- Battery supply and charging support for portable operation
- Multi- platform support like MicroPython, CircuitPython and Arduino IDE.
- Comes with HID support, so device can simulate a mouse or keyboard 

### Specifications:
- RP2040 microcontroller is dual-core Arm Cortex-M0+ processor, 2MB of onboard flash storage, 264kB of RAM
- On-board single-band 2.4GHz wireless interfaces (802.11n) for WiFi and Bluetooth® 5 (LE)
- WPA3 & Soft access point supporting up to four clients
- Operating voltage of pins 3.3V and board supply 5V
- 240x240 resolution, IPS display, and 65k RGB colors
- ST7789 display driver
- Operating Frequency: 13.56MHz
- Operating current: 50mA
- Reading Distance: >50mm(The effective distance is related to the IC card and the use environment)
- Integrated Antenna
- Support Protocols: ISO14443A, ISO14443B, Sony, ISO15693, ISO18092
- Contactless cards: NTAG213, Mifare one S50, Mifare one S70, ultralight, FM11RF08
- Operating Temperature: -15°C~+55°C

## Getting Started with ReadPi-NFC
### Hardware Overview
#### Pinout
<img src="https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/images/ReadPi_NFC%20PINOUT.jpg">

- (1) 1.3” Display
- (2) NFC Module
- (3) Joystick 
- (4) GPIOs breakout 
- (5) Battery Connector
- (6) TF card slot
- (7) Buzzer
- (8) Pico W

#### GPIO Pins Detail
<img src="https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/images/READPI%20GPIO%20PINS%20breakout.jpg">

### Interfacing Details
- Pico W and RFID module interfacing
  
  | Pico W | NFC Module Pin | Function |
  |---|---|---|
  |GP4 | RX | Serial UART connection |
  |GP5 | TX  | Serial UART connection |

  
- Pico W and Display interfacing
  
  | Pico W | Display Pin | Function |
  |---|---|---|
  |GP10 | SCLK | Clock pin of SPI interface for display|
  |GP11 | DIN  | MOSI (Master OUT Slave IN) data pin of SPI interface|
  |GP8 | DC | Data/Command pin of SPI interface|
  |GP9 | CS   | Chip Select pin of SPI interface for display|
  |GP12 | Reset | Display Reset Pin |
  
- Pico W and micro SD card interfacing

  | Pico W | microSD Card | Function |
  |---|---|---|
  |GP18 | SCLK |Clock pin of SPI interface for microSD card |
  |GP19 | DIN  | MOSI (Master OUT Slave IN) data pin of SPI interface|
  |GP16 | DOUT | MISO (Master IN Slave OUT) data pin of SPI interface|
  |GP17 | CS   | Chip Select pin of SPI interface for SDcard|

- Joystick, Buzzer and LED Interfacing with Pico W
  | Pico W | Buttons | Function |
  |---|---|---|
  |GP14 | JY_R |Programmable Joystick button|
  |GP21 | JY_L |Programmable Joystick button|
  |GP22 | JY_U |Programmable Joystick button|
  |GP26 | JY_D |Programmable Joystick button|
  |GP27 | JY_Sel |Programmable Joystick button|
  |GP15 | Buzzer | Buzzer positive |
  |GP25 | LED | OnBoard LED pin of Pico W  |
 
- Breakout GPIOs
  | Pico W |Physical Pin | Multi-Function |
  |---|---|---|
  |GP0 | 1  | General IO / SPI0 RX / I2C0 SDA / UART0 TX |
  |GP1 | 2 | General IO / SPI0 CSn / I2C0 SCL / UART0 RX |
  |GP2 | 4 | General IO / SPI0 SCK / I2C1 SDA |
  |GP3 | 5 | General IO / SPI0 TX / I2C1 SCL |
  |GP6 | 9 | General IO / SPI0 SCK / I2C1 SDA |
  |GP7 | 10 | General IO / SPI0 TX / I2C1 SCL |
  |GP28| 34 | General IO / ADC2 / SPI1 RX |


### 1. Step to install boot Firmware
   - Every ReadPi board will be provided with boot firmware already installed, so you can skip this step and directly go to step 2.
   - If in case you want to install firmware for your board, Push and hold the BOOTSEL button and plug your Pico W into the USB port of your computer. Release the BOOTSEL button after your Pico is connected.
   <img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/pico_bootmode.gif">
   
   - It will mount as a Mass Storage Device called RPI-RP2.
   - Drag and drop the MicroPython UF2 - [ReadPi_firmware](https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/ReadPi_Firmware.uf2) file provided in this github onto the RPI-RP2 volume. Your Pico will reboot. You are now running MicroPython on ArdiPi.

### 2. Onboard LED Blink 
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Once done start **Thonny IDE application**, Connect ReadPi to laptop/PC.
   - Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
     
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img1.jpg" />
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img2.jpg" />
      
   - Write simple onboard blink Python code or [Download Led blink code](https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/examples/onboard_ledBlink.py), then click on the green run button to make your script run on ReadPi.
     
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img3.jpg" />
     
     Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug Pico, it will stop running. To run your script without using an IDE, simply power up ArdiPi and it should run your script, go to step 3. Once you have transferred your code to the ArdiPi board, to see your script running, just plug in power either way using micro USB or via Vin, both will work.

### 3. How to move your script on Pico W of ReadPi
   - Click on File -> Save Copy -> select Raspberry Pi Pico , Then save file as main.py
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/transfer_script_pico.gif" />
   
      In similar way you can add various python code files to Pico. Also you can try out sample codes given here in [examples folder](https://github.com/sbcshop/ReadPi_NFC_Software/tree/main/examples). 
   
   - But in case if you want to move multiple files at one go, example suppose you are interested to save library files folder into Pico W, below image demonstrate that
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/images/multiple_file_transfer.gif" />
   
**NOTE: Don't rename _lib_ files** or and other files, only your main code script should be rename as main.py for standalone execution without Thonny.


### Example Codes
   Save whatever example code file you want to try as **main.py** in **Pico W** as shown in above [step 3](https://github.com/sbcshop/ReadPi_NFC_Software/tree/main#3-how-to-move-your-script-on-pico-w-of-readpi), also add related lib files with default name.
   In [example](https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/examples) folder you will find demo example script code to test onboard components of ReadPi like 
   - [Buzzer test](https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/examples/BuzzerDemo.py) : code to test onboard Buzzer
   - [SD card demo](https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/examples/Demo_sdcard.py) : code to test onboard micro SD card interfacing, [sdcard.py](https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/examples/sdcard.py) lib file is required for the code to run successfully.
   - [NFC module demo](https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/examples/NFCmodule_demo.py) : testing onboard NFC module , buzzer and display unit of shield. 
   
   Using this sample code as a guide, you can modify, build, and share codes!!  
   
## Resources
  * [Schematic](https://github.com/sbcshop/ReadPi_NFC_Hardware/blob/main/Design%20Data/Sch%20ReadPi.pdf)
  * [Hardware Files](https://github.com/sbcshop/ReadPi_NFC_Hardware)
  * [Step File](https://github.com/sbcshop/ReadPi_NFC_Hardware/blob/main/Mechanical%20Data/STEP.step)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)


## Related Products
   * [ReadPi RFID](https://shop.sb-components.co.uk/products/readpi-an-rfid-nfc-reader-powered-with-raspberry-pi-pico-w?variant=40478483054675) - ReadPi with 125KHz RFID powered by Raspberry Pi Pico W
   * [Raspberry Pi Pico RFID expansion](https://shop.sb-components.co.uk/products/raspberry-pi-pico-rfid-expansion) - RFID expansion board with support to incorporate Pico/Pico W 
   * [RFID_Breakout](https://shop.sb-components.co.uk/products/rfid-breakout?_pos=5&_sid=fac219786&_ss=r) - RFID breakout for standalone testing and freedom to choose microcontroller as per requirement.

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
