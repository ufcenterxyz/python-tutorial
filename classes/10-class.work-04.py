# 简单继承
class Animal(object):
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        return f"{self.name} can speak"
    
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} 汪汪" 
    
    
result=Dog("dog")
print(result.speak())
    
        
        
