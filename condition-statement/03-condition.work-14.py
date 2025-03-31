height=int(input("height: m"))
weight=int(input("weight: kg"))
BMI=weight/(height*height)
if BMI <18.5:
    print("体重过轻")
elif 18.5<=BMI <24.9:
    print("正常体重")
elif 25<=BMI<29.9:
    print("超重")
else:
    print("肥胖")