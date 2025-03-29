# new_list=[]
# for i in range(1,21):
#     if i%2==0:
#         new_list.append(i)  #append()将元素添加到元组
# print(new_list)


new_list = [item for item in range(1, 21) if item % 2 == 0]
print(new_list)


