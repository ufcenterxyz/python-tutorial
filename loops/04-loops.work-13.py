import math

# for i in range(0,100):
#     print( math.sqrt(i))
#     new_number=int(math.sqrt(i))
#     print(new_number)
for n in range(0,100):
        if n==2 or n%n==0:
            print(f"{n} {True}")
            break
        elif n==1:
            print(False)
        else:
            print(False)