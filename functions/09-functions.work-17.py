# 函数作为返回值
def create_adder(num):
    def create(num1):
        return num1
    return create(5)+num
result=create_adder(3)
print(result)

