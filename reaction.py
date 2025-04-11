from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
left_button = Button(14)  # Button on GPIO14
right_button = Button(15)  # Button on GPIO15

left_name = input("Enter left player name: ")
right_name = input("Enter right player name: ")

game_active = False

def pressed(button):
    global game_active
    if game_active:
        winner = left_name if button.pin.number == 14 else right_name
        print(f"{winner} wins this round!")
        game_active = False  # Reset for next round

left_button.when_pressed = pressed
right_button.when_pressed = pressed

while True:
    game_active = True
    led.on()
    sleep(uniform(5, 10))
    led.off()
    
    # Wait for a button press to start the next round
    while game_active:
        sleep(0.1)
