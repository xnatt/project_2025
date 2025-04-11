from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
left_button = Button(14)  # Button on GPIO14
right_button = Button(15)  # Button on GPIO15
def pressed(button):
    print(f"Button {button.pin.number} pressed!")

led.on()
sleep(uniform(5, 10))  # Random delay between 5-10 seconds
led.off()
left_button.when_pressed = pressed
right_button.when_pressed = pressed
