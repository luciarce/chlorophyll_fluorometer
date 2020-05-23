#!/usr/bin/env python3.8

#reads serial output from fluorometeter as translated by the Arduino and saves the data as a text file

import serial
import datetime
import numpy

#indicates port from which data should be extracted. CHANGE PORT NAME TO THE ONE IN find_Arduino.py
arduinoData = serial.Serial('/dev/cu.usbmodem141201', baudrate = 9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout = 1)

#creates a textfile where the data will be saved. CHANGE NAME OF SAVEFILE OR IT WILL OVERWRITE YOUR DATA
textFile = open('data/pringlei_20.03.20_infiltrationControl3.txt', 'w')

#creates a loop that will read and save the data on the text file
while True:

	arduinoString = arduinoData.readline().decode('utf8').strip('b\' \ r \ n') #reads serial data output, decodes it and removes unnecessary keys from the string
	print(arduinoString)	
	print(datetime.datetime.now()) #prints data and timestamp on terminal
	textFile.write (str(datetime.datetime.now())) #saves timestamp on textfile
	textFile.write (str(',')) #separates timestamp and data output with a comma
	textFile.write (str(arduinoString)) #prints serial data output from arduino
	textFile.flush()

ser.close()
	
