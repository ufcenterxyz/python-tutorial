num1=int(input("num1: "))
num2=int(input("num2: "))

operator=input("operator: ")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="/" and num2!=0:
    print(num1/num2)
elif operator=="/" and num2==0:
    print(f"{num2}不能为0")
elif operator=="*":
    print(num1*num2)
else:
    print("请输入有效字符")