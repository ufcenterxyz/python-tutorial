import random

count=0
while True:
    count+=1
    if count>=7:
            print("game is over")
            break
    
    user_input=input("result: ")
    if type(user_input)!=int:
           print("请输入数字类型")
           continue
    
    user_input=int(user_input)
    new_random=random.randint(1,100)
    print(new_random)


    if user_input==new_random:
            print("猜对了")
    elif user_input>new_random:
            print("太大了，重新")
    elif user_input<new_random:
            print("太小了")
    



