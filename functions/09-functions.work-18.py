# lambda函数
def lambda_function(args):
    try:
        if args=="+":
            return lambda x,y:x+y
        elif args=="-":
            return lambda x,y:x-y
        elif args=="*":
            return lambda x,y:x*y
        elif args=="%":
            try:
                return lambda x,y:x%y
            except ZeroDivisionError:
                return "除数不能为0"
    except ValueError:
        print("value error")
result=lambda_function("%")
print(result(3,1))