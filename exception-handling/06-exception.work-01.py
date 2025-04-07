def divide(val1,val2):
    try:
        print(val1/val2)
    except ZeroDivisionError:
        print("you cannot divide by zero")
divide(1,10)