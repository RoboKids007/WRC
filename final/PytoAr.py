
import serial
import time
arduino = serial.Serial(port='/dev/ttyACM1', baudrate=9600, timeout=.1)
#while True:
#	x='f'
#	arduino.write(bytes(x, 'utf-8'))


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
def startSerialCmd():
    while True:
        num = 'f' # Taking input from user
        value = write_read(num)
        s1 = value.decode("utf-8") 
        print(value)
        print(s1)
        if "nice" in s1:
            print(s1) # printing the value
            break
startSerialCmd()
