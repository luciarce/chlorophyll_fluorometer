#!/usr/bin/env python3.8

#code is used to obtain the port at which the Arduino is plugged

import serial
import serial.tools.list_ports

def get_ports(): #obtains the existing port locations
	ports = serial.tools.list_ports.comports()
	return ports

def findArduino (portsFound): #makes a function that turns ports into a string, and then searches for the keyword that indicates an Arduino connection (CDC) on the port list
	commPort = 'None'
	numConnection = len(portsFound)
	for i in range(0, numConnection): 
		port = foundPorts[i]
		strPort = str(port)
		
		if ('CDC' in strPort): 
			splitPort = strPort.split(' ')
			commPort = (splitPort[0])
			
	return commPort
		
foundPorts = get_ports() 
connectPort = findArduino (foundPorts) #runs the existing ports on the findArduino function above

if(connectPort != 'None'): #if a port with the CDC Arduino name is found, will write 'connected to ____', if not will give 'connection issue'
	ser = serial.Serial(connectPort,baudrate = 9600, timeout=1)
	print('Connected to ' + connectPort)
else:
	print('Connection Issue!')

print ('DONE.')






