# 生成随机数 random.randint(1,100)
import random
i=random.randint(1,100)
while True:
    try:
        user_input=int(input("number:"))
        print(f"i:{i}")
        if user_input>i:
            print("过大")
        elif user_input<i:
            print("过小")
        elif user_input==i:
            print("猜对了")
            break
        else:
            print("请重新输入")
    except ValueError:
        print("请重新输入")