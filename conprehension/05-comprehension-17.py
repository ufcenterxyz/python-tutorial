# 输入 list1 = [1, 2, 3, 4] 和 list2 = [3, 4, 5, 6]
# 输出应为包含 {3, 4} 的集合
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list=[i for i in list1 for n in list2 if n==i]
print(set(list))
