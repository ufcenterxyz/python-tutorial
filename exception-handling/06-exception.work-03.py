def list_find(my_list,index):
    try:
        if index in my_list:
            return index
        else:
            return "indexError"
    except IndexError:
        print("indexError")
my_list=[1,2,3,4,5]
list_find(my_list,5)
print(list_find(my_list,6))