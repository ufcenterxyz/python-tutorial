# 多重继承
class  Flyable(object):
    def __init__(self,name):
        self.name=name
        
    def fly(self):
        return f"{self.name} can fly"

class Swimmable(Flyable):
    def swim(self):
        return f"{self.name} can swim"
    

class Duck(Swimmable):
    def describe(self):
        return self.fly()+self.swim()
    

result=Duck("duck")
print(result.describe())

    