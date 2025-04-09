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


    left_name = input("请输入左边玩家的名字: ")
    right_name = input("请输入右边玩家的名字: ")
    rounds = int(input("请输入游戏总轮数: "))

    for round_num in range(1, rounds + 1):
        print(f"第{round_num}轮游戏开始！")
        led.on()
        start_time = time()
        sleep(uniform(5, 10))
        led.off()
        left_button.when_pressed = pressed
        right_button.when_pressed = pressed

        # 等待按钮按下
        while True:
            if left_button.is_pressed or right_button.is_pressed:
                break
            sleep(0.1)

        if round_num < rounds:
            next_round = input("是否进行下一轮游戏？(y/n): ")
            if next_round.lower() != 'y':
                break


if __name__ == "__main__":
    play_game()
