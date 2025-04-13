# 属性装饰器
class Temperature(object):

    temperature=10
    
    
    @property
    def C(self):
        return self.temperature
    
    @property
    def T(self):
        return  self.temperature* 9/5 + 32
    
result=Temperature()
print(result.T)
