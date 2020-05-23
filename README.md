# chlorophyll_fluorometer
scripts for extracting data from chlorophyll fluorometer PAM101-102-103, and live plotting results

findArduino.py is used to locate the serial port to which the Arduino is connected.
The port name is necessary for extracting data from the fluorometer.

bare_read_fluorometer.py reads the serial output from the fluorometer via the Arduino and saves the data as a text file.
Careful with overwriting - change name of text file every time
Check port name is the same as findArduino.py

rollplot.py produces a plot of the data as collected thus far, and a 50 datapoints rolling average
Indicate from which text file the data is plotted
