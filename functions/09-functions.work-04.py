def calculate(num1,num2,*args):
    try:
        print(args)
        for i in args:
            if i=="add":
                print(num1+num2)
            elif i=="subtract":
                print(num1-num2)
            elif i=="multiply":
                print(num1*num2)
            elif i=="divide":
                print(num1%num2)
            else:
                print("0不能被整除")
    except ValueError:
        print("valueError")
calculate(1,1,'add', 'subtract', 'multiply', 'divide')
