# 字典键查找
def find(my_dict,dict_key):
    try:
        if dict_key in my_dict.keys():
            return dict_key
        else:
            return "key is not exist"
    except IndexError:
        print("key is not exist") 
my_dict={"a":1,"b":2}
result=find(my_dict,"a")
print(result)