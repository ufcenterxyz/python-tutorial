# 函数返回多个值
def min_max_avg(lists):
    sum=0
    try:
        for i in lists:
            sum+=i
        return max(lists),min(lists),sum/len(lists)
    except ValueError:
        return "值错误"
result=min_max_avg([1,2,3])
print(result)
