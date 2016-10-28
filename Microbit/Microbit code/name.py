from serial import *
from serial.tools.list_ports import comports
ports = comports()
print("\nAvailable serial ports:")
for port in ports:
    if (port.device.find("usbmodem") != -1):
        print("   " + port.device + " " + port.description)
print("\n")