# 全局变量

counter=1
def increment_counter():
    global counter
    counter+=1

def get_counter():
    increment_counter()
    return counter

print(get_counter())