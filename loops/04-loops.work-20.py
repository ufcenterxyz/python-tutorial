f=open("/home/mavis/python-tutorial/loops/hello.txt","r")
# print(f.read())

# 读取每一行

# 计算总行数
count_line=0
count_long=0
for i in f:
    print(f"i:{i}")
    count_line+=1    
    count_long+=len(i)
print(f"总行数：{count_line},总字符串：{count_long}")

# 关闭文件
f.close()

