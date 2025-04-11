from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
left_button = Button(14)  # Button on GPIO14
right_button = Button(15)  # Button on GPIO15

left_name = input("Enter left player name: ")
right_name = input("Enter right player name: ")

def pressed(button):
    if button.pin.number == 14:
        print(f"{left_name} won!")
    else:
        print(f"{right_name} won!")
    exit()  # Exit after a button is pressed

led.on()
sleep(uniform(5, 10))
led.off()

left_button.when_pressed = pressed
right_button.when_pressed = pressed
