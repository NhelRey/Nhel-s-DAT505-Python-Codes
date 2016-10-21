from microbit import *


port.readall()

while(True):
    if(uart.any()):
        input = uart.readline()
        uart.write(" Good day to you sir !\n")
        
        input = port.readline()
	print("Microbit replied: " + input)
	port.close()