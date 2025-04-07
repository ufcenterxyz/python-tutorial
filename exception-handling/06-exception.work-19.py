def result():
    user_input=input("输入数字")
    try:
        return int(user_input)
    except ValueError:
        print("请重新输入")
r = result()
print(r)
