def handle_number(val1,val2):
    try: 
        return str(val1/val2)
    except ZeroDivisionError:
        print("zerodivisionError")
    except TypeError:
        print("typeError")
handle_number(1,10)
print(handle_number(1,10))
    