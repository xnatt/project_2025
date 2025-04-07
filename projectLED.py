from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
led.on()
sleep(5)  # 初始固定时间，后续改为随机
led.off()



sleep(uniform(5, 10))  # 随机5-10秒

left_button = Button(14)
right_button = Button(15)

def pressed(button):
    if button.pin.number == 14:
        print(f"{left_name} won!")
    else:
        print(f"{right_name} won!")

left_button.when_pressed = pressed
right_button.when_pressed = pressed

left_name = input("Left player name: ")
right_name = input("Right player name: ")


left_score = 0
right_score = 0

while True:
    led.on()
    sleep(uniform(5, 10))
    led.off()
    # 等待按钮按下，触发pressed函数
    # 在pressed函数中更新得分：
    if button.pin.number == 14:
        left_score += 1
        print(f"{left_name} won! Score: {left_score} vs {right_score}")
    else:
        right_score += 1
        print(f"{right_name} won! Score: {left_score} vs {right_score}")