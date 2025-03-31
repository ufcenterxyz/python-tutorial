age=input("age: ")
age=int(age)
if 0<=age<=12:
    print("儿童")
elif 13<=age<=19:
    print("青少年")
elif 20<=age<=64:
    print("成年人")
else:
    print("老年人")