# 可变参数
def sum_all(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
sum_all(1)