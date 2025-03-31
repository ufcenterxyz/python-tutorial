weather=input("weather:")
tempture=input("tempture:")
tempture=int(tempture)
if weather=="晴天":
    if tempture>=20:
        print("穿少点")
    elif 20>tempture>=10:
        print("要穿外套")
    else:
        print("穿棉衣")

if weather=="雨天":
    if tempture>=20:
        print("穿少点")
    elif 20>tempture>=10:
        print("要穿外套")
    else:
        print("穿棉衣")

if weather=="雪天":
    if 20>=tempture>=10:
        print("要穿外套")
    else:
        print("穿棉衣")