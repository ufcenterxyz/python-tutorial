# 工厂模式
class ShapeFactory():
    def __init__(self,name):
        self.name=name
        
    def create_shape(self):
        return self.name

class Circle(ShapeFactory):
    def draw(self):
        return "circle"

class Rectangle(ShapeFactory):
    def draw(self):
        return "rectangle"
    
shape_result=ShapeFactory("circle").create_shape()
print(shape_result)
