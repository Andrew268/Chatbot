#from microbit import *
import microbit
from microbit import uart
# Write your code here :-)
#display.scroll('Welcome to HELL', wait=False, loop=True)

while(True):
    if(uart.any()):
        input = uart.read(1)
        print("Got " + str(input))
        
        
        if(chr(input[0]) == '1'): light = 0
        else: light = 0
        microbit.display.on()
        microbit.display.set_pixel(0,0,light)
        microbit.display.set_pixel(0,1,light)
        microbit.display.set_pixel(0,2,light)
        microbit.display.set_pixel(0,3,light)
        microbit.display.set_pixel(0,4,light)
