# while循环与用户输入
sum=0
while True:
    try:
        user_input=input("请输入数字:")
        user_input=int(user_input)
        sum+=user_input
        print(f"总和: {sum}")
        if input("请输入数字:")=="done":
            print(f"总和: {sum}")
            break
    except ValueError:
        print("请输入正确的数字类型")