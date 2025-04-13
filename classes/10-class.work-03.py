# 方法重载
class Calculator(object):
    def __init__(self):
        pass
    def add(self,num1,num2):
        
        return num1+num2
    
    def add(self,num_list):
        return 1

result=Calculator()
print(result.add(1,2))
print(result.add([1,2,3]))