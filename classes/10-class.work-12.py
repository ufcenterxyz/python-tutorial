# 类组合    
class Engine(object):
        def __init__(self,name):
                self.name=name
        def start(self):
            return f"{self.name} can start ."
        
        def end(self):
            return f"{self.name} can end ."   
        
class Car():
    engine=None
    
    def __init__(self, engin):
        self.engine = engin
        
    def start_car(self):
        return  self.start()
    
    def end_car(self):
        return self.end()
    
# esg = Engine("esg")
result_car=Car(Engine("esg"))

print(result_car)

