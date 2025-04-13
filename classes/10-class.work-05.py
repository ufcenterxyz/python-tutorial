# 多级继承
class Vehicle(object):
    def __init__(self,name):
        self.name=name

class Car(Vehicle):
    def __init__(self, name, color):
        self.color = color
        
    def run(self):
        return f"{self.name} can run"

class SportsCar(Car):
    def __init__(self, name, color):
        self.name=name
        self.color=color
    def runQ(self):
        return f"{self.name}{self.color} can run quickly"


result=SportsCar("xiaomi","RED")
print(result.runQ())
print(result.run())
