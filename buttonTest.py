from gpiozero import Button
from signal import pause

# 定义左右按钮的 GPIO 引脚
left_button = Button(14)
right_button = Button(15)

# 定义按钮按下时的回调函数
def left_button_pressed():
    print("左边按钮被按下！")

def right_button_pressed():
    print("右边按钮被按下！")

# 绑定按钮按下事件
left_button.when_pressed = left_button_pressed
right_button.when_pressed = right_button_pressed

# 保持程序运行，等待按钮事件
pause()
    