# 方法重载
class Calculator(object):

    def __init__(self):
        pass
        
    def add(self,*args):
        print(args)
        if len(args)==2:
            return args[0]+args[1]
        elif len(args)==1:
            return sum(args[0])
        else:
            return "valueError"
        
    


result=Calculator()
print(result.add(1,2))
print(result.add([1,2,3]))