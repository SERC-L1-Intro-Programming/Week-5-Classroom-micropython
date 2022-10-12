# micropython script that outputs temperature and humidity readings from a DHT11 sensor.
import time
import dht
import machine

# create sensor object
sensor = dht.DHT11(machine.Pin(5))
# sensor = dht.DHT22(machine.Pin(5))

# make console-like app
print("* DHT11 Temperature & Humidity *")
print("Press Ctrl-C to stop")

#TODO: add a try/except block to catch the Ctrl-C keyboard interrupt
#TODO: add a while loop to read the sensor every 2 seconds
#TODO: output the temperature and humidity readings to the console
