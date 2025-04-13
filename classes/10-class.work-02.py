# 属性访问与修改
class Person(object):
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def introduce(self):
        return f"我是{self.name},我是{self.age}岁"
    
    def have_birthday(self):
        return int(self.age)+1
    
result=Person("li","10")
print(result.introduce(),result.have_birthday())
    
    
    
