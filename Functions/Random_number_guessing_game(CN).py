#### 猜猜我是什么数字 ####

import random

# 不变值
again = 'y'

# 主要功能
def main():
    # 显示标题
    display_title()

    # 开始游戏
    game_star()

# 显示标题及指南给用家
def display_title():

    print("*** 猜猜我是什么数字 ***")
    print("系统将会随机产生一个数字 1 - 100")
    print("假如你猜得比答案高")
    print("系统将会显示 \"太高, 再尝试.\"")
    print("假如你猜得比答案低")
    print("系统将会显示 \"太低, 再尝试.\"")

def game_star():

    print("游戏开始!!!")
    number = random.randint(1, 100)

    answer = int(input("请输入你的答案: "))

    count = 1

    while answer != number:
        
        if answer >= number:
            print("太高, 再尝试.")
            answer = int(input("请输入你的答案: "))
        elif answer <= number:
            print("太低, 再尝试.")
            answer = int(input("请输入你的答案: "))
        else:
            print("错误, 不正确的输入.")
            answer = int(input("请输入你的答案: "))

        count += 1

    # Loop ended
    print("恭喜你 !!! 你猜了", count, "次")
    
# Call the main function
while again == 'y' or again == 'Y':
    main()

    # Run again?
    again = input("想再玩一次吗? (y = yes): ")
