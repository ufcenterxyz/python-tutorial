string_one=input("请输入正确的字符: ").lower()
result_dia={}
try:
    for i in string_one:
        n=string_one.count(i)
        print(i,n)
        result_dia[i]=n
    print(result_dia)
except ValueError:
    print("请输入正确的字符")