# 编写一个程序，从 random 模块导入 randint 和 choice 函数，然后创建一个简单的猜数游戏。
# 程序随机选择 1-10 之间的一个数字，用户有三次机会猜测。每次猜测后，程序应告知用户猜测是否正确，或者给出"太高"或"太低"的提示。
from random import randint,choice
x=randint(1,10)
i=0
try:
    for i in range(0,3):
        i+=1
        user_input=int(input("请输入数字: "))
        if user_input>x:
            print("太高")
        elif user_input<x :
            print(f"太低,正确的答案是:{x}")
        elif i==3:
            print(f"已结束,正确的答案是:{x}")
        elif user_input==x:
            print(f"答对了")
            break
except ValueError:
    print("请输入正确的数字")
