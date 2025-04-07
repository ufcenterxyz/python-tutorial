def change_int(my_list,index1):
    try:
        for index in my_list:
            print(index)
            if index1==index:
                return index1  
    except IndexError:
        print("IndexError")
    except ValueError:
        print("ValueError")
my_list=[1,2,3,"a"]        
change_int(my_list,1)