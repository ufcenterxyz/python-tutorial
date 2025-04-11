# 函数的异常处理
def safe_divide(x,y):
    try:
        try:
            if type(x)!=int and type(y)!=int:
                return int(x)/int(y)
            else:
                return x/y
        except TypeError:
                print("类型不是数字类型")
    except ZeroDivisionError:
        print("被除数不能为0")
safe_divide("5","6")
print(safe_divide("5","6"))