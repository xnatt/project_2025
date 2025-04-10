# reaction.py (基础版)
from gpiozero import LED, Button
from time import sleep, time
from random import uniform

led = LED(4)
left_button = Button(14)
right_button = Button(15)

left_name = input("Left player name: ")
right_name = input("Right player name: ")

def game_loop():
    led.on()
    sleep(uniform(5, 10))
    led.off()
    
    while True:
        if left_button.is_pressed or right_button.is_pressed:
            return

def pressed(button):
    if button.pin.number == 14:
        print(f"{left_name} wins!")
    else:
        print(f"{right_name} wins!")
    exit()

left_button.when_pressed = pressed
right_button.when_pressed = pressed

while True:
    game_loop()
    sleep(1)
