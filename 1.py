# reaction.py
from gpiozero import LED, Button
from time import sleep, time
from random import uniform

# Hardware initialization
led = LED(4)
left_button = Button(14)
right_button = Button(15)

# Player information
left_name = input("Left player's name: ")
right_name = input("Right player's name: ")

# Game variables
left_score = 0
right_score = 0
rounds = 3  # Configurable number of rounds


def game_loop():
    global left_score, right_score
    led.on()
    delay = uniform(5, 10)
    sleep(delay)
    led.off()
    start_time = time()

    # Detect button press
    while True:
        if left_button.is_pressed:
            reaction_time = time() - start_time
            print(f"{left_name} wins! Reaction time: {reaction_time:.2f} seconds")
            left_score += 1
            break
        if right_button.is_pressed:
            reaction_time = time() - start_time
            print(f"{right_name} wins! Reaction time: {reaction_time:.2f} seconds")
            right_score += 1
            break


def main():
    print("==== Quick Reaction Game ====")
    for i in range(rounds):
        print(f"\nRound {i + 1}/{rounds}")
        game_loop()
        sleep(1)  # Interval between rounds

    print("\n=== Final Score ===")
    print(f"{left_name}: {left_score} points")
    print(f"{right_name}: {right_score} points")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame terminated")
    finally:
        led.off()