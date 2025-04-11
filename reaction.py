from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)

led.on()
sleep(uniform(5, 10))  # Random delay between 5-10 seconds
led.off()
