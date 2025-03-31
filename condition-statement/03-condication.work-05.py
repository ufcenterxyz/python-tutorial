year=input("year:")
year=int(year)
if year%4==0 or year%400==0 and year%100!=0:
    print("这是闰年")
else:
    print("这不是闰年")