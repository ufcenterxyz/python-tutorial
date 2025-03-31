str1=input("input1: ")
str2=input("input2: ")
if len(str1)>len(str2):
    print(str1)
elif len(str1)<len(str2):
    print(str2)
else:
    print("两个字符串长度相同")