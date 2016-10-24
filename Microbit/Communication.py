from microbit import *

while(True):
    if(uart.any()):
        input = uart.readline()
        display.show(Image.HAPPY)
        uart.write("I am happy !\n")