# 抽象基类
from abc import ABC, abstractclassmethod
# @abstractclassmethod(已弃用)


class Shape(ABC):
    @classmethod
    def __init__(self,name):
        self.name=name
    def area(self):
        return f"{self.name}"
    def perimeter(self):
        pass
    
result=Shape("O").area()
print(result)