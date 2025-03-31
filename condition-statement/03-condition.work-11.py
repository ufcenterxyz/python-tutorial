weather=input("weather:")
temperature=input("temperature:")
temperature=int( temperature)
if weather=="晴天":
    if  temperature>=20:
        print("穿少点")
    elif 20> temperature>=10:
        print("要穿外套")
    else:
        print("穿棉衣")

if weather=="雨天":
    if  temperature>=20:
        print("穿少点")
    elif 20> temperature>=10:
        print("要穿外套")
    else:
        print("穿棉衣")

if weather=="雪天":
    if 20>= temperature>=10:
        print("要穿外套")
    else:
        print("穿棉衣")