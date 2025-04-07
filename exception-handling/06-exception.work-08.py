def fun(my_dict,my_key):
    try:
        my_key=my_dict[my_key]
    except KeyError:
        print("KeyError")
    else:
        return my_key[my_key]
my_dict={"a":1,"b":2}
fun(my_dict,"a")