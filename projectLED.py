from gpiozero import LED, Button
from time import sleep, time
from random import uniform


led = LED(4)
left_button = Button(14)
right_button = Button(15)


def pressed(button):
    global left_score, right_score, start_time
    end_time = time()
    elapsed_time = end_time - start_time
    if button.pin.number == 14:
        left_score += 1
        print(f"{left_name} won! Score: {left_score} vs {right_score}")
        print(f"{left_name} used time: {elapsed_time:.2f} seconds")
    else:
        right_score += 1
        print(f"{right_name} won! Score: {left_score} vs {right_score}")
        print(f"{right_name} used time: {elapsed_time:.2f} seconds")


left_name = input("Left player name: ")
right_name = input("Right player name: ")

left_score = 0
right_score = 0

while True:
    led.on()
    start_time = time()
    sleep(uniform(5, 10))
    led.off()
    left_button.when_pressed = pressed
    right_button.when_pressed = pressed
