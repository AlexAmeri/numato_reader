from pynput.keyboard import Listener, Key
import time
import sys
import serial

def on_press(key):
    if (key.char == '1'):
        ser.write("gpio writeall 01\r")
        time.sleep(0.1)
        ser.write("gpio writeall 00\r")
    elif (key.char == '2'):
        ser.write("gpio writeall 02\r")
        time.sleep(0.1)
        ser.write("gpio writeall 00\r")
    if (key.char == '3'):
        ser.write("gpio writeall 04\r")
        time.sleep(0.1)
        ser.write("gpio writeall 00\r")
    if (key.char == '4'):
        ser.write("gpio writeall 08\r")
        time.sleep(0.1)
        ser.write("gpio writeall 00\r")

#Start the COM port
print ('Starting COM port')
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    xonxoff=True,
    dsrdtr=True
)

try:
    ser.isOpen()
    ser.write("\r")
    ser.write("\r")
    ser.write("gpio iodir 00\r")
    ser.write("gpio iodir 00\r")
    print ('Started COM port')
    with Listener(on_press=on_press) as listener:  # Setup the listener
        listener.join()  # Join the thread to the main thread

except serial.SerialException:
    print ("Failed to open COM port")