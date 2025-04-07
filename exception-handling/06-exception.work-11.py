# 嵌套异常处理
def my_dict_fun(my_dict,my_key):
    try:
        if my_key in my_dict:
            try:
                return my_dict[my_key]
            except ValueError:
                print("valueError")
    except KeyError:
        print("keyError")
my_dict={"a":1,"b":2,"c":3}
my_dict_fun(my_dict,"a")
print(my_dict_fun(my_dict,"de"))
