password_input=input("password")
if len(password_input)<8:
    print("弱密码")
elif len(password_input)>=8:
    print("中密码")
elif len(password_input)>=8 and password_input.__contains__(int):
    print("强密码")