score=input("score: ")
score=int(score)
if 90<=score<=100:
    print("A")
elif 80<=score<=89:
    print("B")
elif 70<=score<=79:
    print("C")
elif 60<=score<=69:
    print("D")
elif score<0 or score>100:
    print("please input score again")
else:
    print("F")