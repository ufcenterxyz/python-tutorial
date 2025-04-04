# 斐波拉数列
a1=0
a2=1
print(a1,a2)
i=0
while i<8:
    current=a1+a2
    a1=a2
    a2=current
    i+=1
    print(f"{i},{current}")


