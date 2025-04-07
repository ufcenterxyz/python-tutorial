# 字符串转化为整数    
def change_int(a):
    try:
        if type(int(a))==int:
            return int(a)
        else:
            return "valueError"
    except ValueError:
        print("valueError")
change_int("123")
print(change_int("123"))