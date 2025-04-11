# 作用域
def modify_list(*args):
    args=[*[1, 2, 3, 4],7]
    print(args)
modify_list([1,2,3,4])

        
def create_and_modify_list(*args):
    list1=[1,2,3,4]
    list1[3]=7
    print(list1)
create_and_modify_list([1,2,3,4])



