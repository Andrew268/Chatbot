from serial import *
port = Serial("/dev/cu.usbmodem1422",115200,timeout=2)
port.readall()
message = "Hello there Microbit\n"
port.write(message.encode())
print("You just said: Hello there Microbit")
input = port.readline()
print("Microbit replied: " + input)
port.close()