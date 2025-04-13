# 类组合    
class Engine(object):
        def __init__(self,name):
                self.name=name
        def start(self):
            return f"{self.name} can start ."
        
        def end(self):
            return f"{self.name} can end ."   
        
class Car(Engine):
    
    def start_car(self):
        return  self.start()
    
    def end_car(self):
        return self.end()
    
result_car=Car("TSL").end_car()

print(result_car)

