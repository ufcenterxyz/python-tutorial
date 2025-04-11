def create_multiply(n):
    x=2
    
    def new_fun():
        return x*n
    
    return new_fun
result=create_multiply(2)
print(result())

# def outer():
#     # 外层函数的变量
#     x = 10
    
#     def inner():
#         # 内层函数可以访问外层变量
#         return x + 5
    
#     return inner

# # 使用
# func = outer()
# print(func())  # 输出 15