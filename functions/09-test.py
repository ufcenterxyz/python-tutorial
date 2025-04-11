def total(money):
    increase_total=0
    decrease_total=0
    for i in range(1,13):
        money*=i
        increase_total+=money
        print(increase_total)
    
    for i in range(1,13):
        money*=(i-1)*0.2
        
        decrease_total+=money
        print(decrease_total)
    
    return increase_total-decrease_total
result=total(10000)
print(result)