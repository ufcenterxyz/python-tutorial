# 类装饰器
import time

@timer
class Time():
    print(time.time())