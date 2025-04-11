# 函数作为参数
def apply_function(fun,lists):
    apply_list=[]
    for i in lists:
        print(i)
        apply_list.append(fun(i))
    return apply_list
result=apply_function(str,[1,2,3])
print(result)
