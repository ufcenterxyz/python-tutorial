def a_function():
    pass
a_function()   

# pass *args to a function
def add(a,b):
    return a+b
add(1,2)

# pass the name of a function
def add(a=2,b=2):
    return a+b
print(add())
# total=add(a=6,b=0)
# print(total)

# keywords *args
def keyword_function(a=1,b=2):
    return a+b
keyword_function(a=7,b=9)
print(keyword_function())

def mixed_function(a,b=1,c=2):
    return a+b+c
print(mixed_function(0))   

# args and *args, **kwargs 
def many(*args,**kwargs):
    print(args)
    print(kwargs)
many(1,2,3,name="li",job="teacher")

# scope and globals
def function_a():
    global a
    a=1
    b=2
    return a+b
def function_b():
    c=3
    return c+a

print(function_a())
print(function_b())

# 函数递归
