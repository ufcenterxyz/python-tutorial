def my_function(list):
    try:
        if len(list)!=0:
            return list[0]
    except IndexError:
        raise Exception("")
result=my_function([1,2,3,4])  
print(result) 