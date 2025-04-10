from gpiozero import LED, Button
from time import sleep, time
from random import uniform


def play_game():
    led = LED(4)
    left_button = Button(14)
    right_button = Button(15)
    left_score = 0
    right_score = 0

    def pressed(button):
        nonlocal left_score, right_score, start_time
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


    left_name = input("left name: ")
    right_name = input("right name: ")
    rounds = int(input("Please enter the total number of rounds in the game: "))

    for round_num in range(1, rounds + 1):
        print(f"the {round_num} round of the game begins！")
        led.on()
        start_time = time()
        sleep(uniform(5, 10))
        led.off()
        left_button.when_pressed = pressed
        right_button.when_pressed = pressed

        
        while True:
            if left_button.is_pressed or right_button.is_pressed:
                break
            sleep(0.1)

        if round_num < rounds:
            next_round = input("Do you want to proceed to the next round of the game?(y/n): ")
            if next_round.lower() != 'y':
                break


if __name__ == "__main__":
    play_game()
