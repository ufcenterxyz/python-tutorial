# 参数验证

def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "被除数不能为0"
divide(10,5)
print(divide(10,1))

