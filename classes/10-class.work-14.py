# 单例模式
# 使用__new方法在创造实例时，达到实现单例模式
class Logger():
    _instance=None
    def __new__(cls):
        return cls._instance
    
    def __init__(self,name):
        self.name=name
        
    def log(self):
        return self


log_result=Logger().log()
print(log_result)    