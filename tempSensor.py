import pycom
import machine
import time

print('Temperature readings:')
while True:
	celcius = (machine.ADC().channel(pin='P16').voltage() - 500.0) / 10.0
	print(celcius)
	pybytes.send_signal(1, celcius)
	time.sleep(5)