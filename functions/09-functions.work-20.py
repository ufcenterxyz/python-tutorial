def process_data(number_list,*args):
    for fun in args:
        for n in range(len(number_list)):
            number_list[n-1]=fun(number_list[n-1])
    return number_list

def double_values1(number):
    return number*2

def double_values1(number):
    return number*3
    
result=process_data([1,2,3,4],double_values1,double_values1)
print(result)