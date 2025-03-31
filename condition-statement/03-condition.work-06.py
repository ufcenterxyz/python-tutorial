input1=input("一边： ")
input2=input("第二边: ")
input3=input("第三边：")

input1=int(input1)
input2=int(input2)
input3=int(input3)

if input1+input2>input3 or input1+input3>input2 or input2+input3>input1:
    print("这三个数字可以构成三角形")
else:
    print("这三个数字不能构成三角形")
