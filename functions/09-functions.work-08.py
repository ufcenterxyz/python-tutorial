# 函数组合
def celsius_to_fahrenheit(C):
    print(32+C*1.8)

def fahrenheit_to_celsius(F):
    print((F- 32) % 1.8)

def convert_temperature(*args):
    fahrenheit_to_celsius(32)
    celsius_to_fahrenheit(tem)
    print(fahrenheit_to_celsius(32))

convert_temperature(tem," °F","°C")