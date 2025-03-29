# 字符串格式化
template="The sum of %i and %i is %i"
# result=template % (1,"2",3)
# print(result),a real number is required ,not str


final_template="The sum of %(x)s + %(y)s =%(z)s " %{"x":1,"y":2,"z":3}
print(final_template[11:])