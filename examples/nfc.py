import machine
import time
import binascii
import array
import ustruct
import urandom


STARTBYTE     ='A8'  
ENDBYTE       ='A9'
HARD_VERSION  ='0007000100'
GET_ADDRESS   ='0001000100'
READ_DATA     ='0037000200'         
NTAG_VERSION  ='0036000100'
ECC_SIG       ='003C000100'
WRITE_DATA    ='0039000600'
CARD_UID      ='0026000100' 

class NFC():
    def __init__(self,baudrate):
        self.serial = machine.UART(1, baudrate=baudrate, bits=8, parity=None, stop=1, tx=machine.Pin(4), rx=machine.Pin(5))
        self.serial.init(baudrate=baudrate, bits=8, parity=None, stop=1)
        time.sleep(0.2)

    def calculate_checksum(self,data):
        checksum = 0
        for byte in data:
            checksum ^= byte
        return checksum

    def calculation(self,address_r):
        address_r = str(hex(int(address_r))[2:])
        if len(address_r) < 2:
            address_r = '0' + address_r            
        rand_hex = self.random_hex()
        chksm_data = rand_hex+READ_DATA+address_r
        bin_data1 = binascii.unhexlify(chksm_data)
        chk_1 = (hex(self.calculate_checksum(bin_data1)))
        chk = chk_1[2:]
        dat = STARTBYTE+rand_hex+READ_DATA+address_r+chk+ENDBYTE
        return dat
    
    def calculation_1(self,da):           
        rand_hex_1  = self.random_hex()
        chksm_data_1  = rand_hex_1 +da
        bin_data1_1  = binascii.unhexlify(chksm_data_1 )
        chk_2 = (hex(self.calculate_checksum(bin_data1_1 )))
        chk_1  = chk_2[2:]
        dat_1  = STARTBYTE+rand_hex_1 +da+chk_1 +ENDBYTE
        return dat_1 

    def write_calculation(self,data,address_r,s):
        address_r = str(hex(int(address_r))[2:])
        if len(address_r) < 2:
            address_r = '0' + address_r            
        rand_hex = self.random_hex()
        chksm_data = rand_hex+s+address_r+data
        bin_data1 = binascii.unhexlify(chksm_data)
        chk_1 = (hex(self.calculate_checksum(bin_data1)))
        chk = chk_1[2:]
        dat = STARTBYTE+rand_hex+s+address_r+data+chk+ENDBYTE
        return dat
    
        
    def random_hex(self):
        length = 2
        random_bytes = bytearray(urandom.getrandbits(8) for _ in range((length + 1) // 2))
        random_hex = ''.join('{:02x}'.format(byte) for byte in random_bytes)
        return random_hex[:length]
           
    def send_command(self, Data):
        bin_data = binascii.unhexlify(Data)
        response = self.serial.write(bin_data)
        #print("bin_data = ",bin_data)

    def hardware_version(self):
        dat_1  = self.calculation_1(HARD_VERSION)
        self.send_command(dat_1 )
        time.sleep(0.2)
        d = self.serial.read(19)
        s = []
        if d is not  None: 
            def split_bytes_data(data, packet_size):
                # Split the bytes object into packets of the specified size
                packets = [data[i:i+packet_size] for i in range(0, len(data), packet_size)]
                return packets
            ds = split_bytes_data(d,7)
            for i in range(1,len(ds)):
                   s.append(str(ds[i],'latin-1'))
            return "".join(s)

########################## read operations ############################################
    def data_read(self,address_r):
        dat = self.calculation(address_r)
        if len(dat) == 20:
            data = self.send_command(dat)
            time.sleep(0.2)
            rec_data = self.serial.read()
            if rec_data is not None:
                a = ['{:02x}'.format(x) for x in rec_data]
                if "".join(a)[6:14] != "37000101":
                    if  len("".join(a)[14:22]) > 7:
                        return "".join(a)[14:22]
                    else:
                        return "Card not detect"
        
    def Ntag_version(self):
        dat = self.calculation_1(NTAG_VERSION)
        data = self.send_command(dat)
        time.sleep(0.5)
        rec_data = self.serial.read()
        #print("rec_data = ",rec_data)
        if rec_data is not None:
            a = ['{:02x}'.format(x) for x in rec_data]
            return "".join(a)
        #read_data.flush()
        
    def ECC_signature(self):
        dat = self.calculation_1(ECC_SIG)
        if len(dat) == 18:
            data = self.send_command(dat)
            time.sleep(0.5)
            rec_data = self.serial.read()
            #print("rec_data = ",rec_data)
            if rec_data is not None:
                a = ['{:02x}'.format(x) for x in rec_data]
                f =  "".join(a)[-5:-4]
                
                if  "".join(a)[-5:-4] == '1':
                    return "Card not detect"
                else:
                    return  "".join(a)
        
    def Card_UID(self):
        dat = self.calculation_1(CARD_UID)
        print(dat)
        print(len(dat))
        if len(dat) == 18:
            data = self.send_command(dat)
            time.sleep(0.5)
            rec_data = self.serial.read()
            if rec_data is not None and len(rec_data) > 18:
                a = ['{:02x}'.format(x) for x in rec_data]
                s = "".join(a)
                return s#s[-36:-1]
        
########################## write operations ############################################
        
    def Data_write(self,data,address_r):
        dat = self.write_calculation(data,address_r,WRITE_DATA)
        if len(dat) == 28:
            data = self.send_command(dat)
            time.sleep(0.5)
            rec_data = self.serial.read()
            if rec_data is not None:
                a = ['{:02x}'.format(x) for x in rec_data]
                f =  "".join(a)[-5:-4]
                
                if  "".join(a)[-5:-4] == '0':
                    return "Card write sucessfully"
                else:
                    return "Card not detect"
        

