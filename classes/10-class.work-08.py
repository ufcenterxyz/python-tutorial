class Vector(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self):
        return self.x+self.y
    
    def __sub__(self):
        return self.x-self.y
    
    def __str__(self):
        return f"{self.x},{self.y}"

result=Vector(1,2)
print(result.__add__(),result.__sub__())