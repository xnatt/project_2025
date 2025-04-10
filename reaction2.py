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
        print("Button pressed!")
        nonlocal left_score, right_score, start_time, left_time, right_time
        end_time = time()
        elapsed_time = end_time - start_time
        if button.pin.number == 14:
            left_time = elapsed_time
        else:
            right_time = elapsed_time

        if left_time is not None and right_time is not None:
            if left_time < right_time:
                left_score += 1
                print(f"{left_name} won! Score: {left_score} vs {right_score}")
            elif right_time < left_time:
                right_score += 1
                print(f"{right_name} won! Score: {left_score} vs {right_score}")
            else:
                print("It's a tie!")
            print(f"{left_name} used time: {left_time:.2f} seconds")
            print(f"{right_name} used time: {right_time:.2f} seconds")

    left_name = input("input left name: ")
    right_name = input("input right name: ")
    rounds = int(input("total number of rounds: "))

    for round_num in range(1, rounds + 1):
        print(f"the {round_num} round of the game begins！")
        led.on()
        sleep(uniform(5, 10))
        led.off()
        start_time = time()
        left_time = None
        right_time = None
        left_button.when_pressed = pressed
        right_button.when_pressed = pressed

        timeout = 10  
        end_time = start_time + timeout
        while time() < end_time:
            if left_time is not None and right_time is not None:
                break
            sleep(0.1)

        
        if left_time is None:
            right_score += 1
            print(f"{right_name} won by default! Score: {left_score} vs {right_score}")
            left_time = timeout
            right_time = right_time if right_time is not None else timeout
        elif right_time is None:
            left_score += 1
            print(f"{left_name} won by default! Score: {left_score} vs {right_score}")
            right_time = timeout
            left_time = left_time if left_time is not None else timeout

        

        if round_num < rounds:
            next_round = input("Do you want to proceed to the next round of the game?(y/n): ")
            if next_round.lower() != 'y':
                break

if __name__ == "__main__":
    play_game()