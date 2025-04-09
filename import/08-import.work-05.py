import calculator
import random
user_input1=input("数字1: ")
user_input2=input("数字2: ")
operator=random.choice("+-*%")
print(operator)
if operator=="*":
    calculator.multiply(int(user_input1),int(user_input2))
elif operator=="+":
    calculator.add(int(user_input1),int(user_input2))
elif operator=="-":
    calculator.subtract(int(user_input1),int(user_input2))
elif operator=="%":
    calculator.divide(int(user_input1),int(user_input2))
else:
    print("please input right words")








