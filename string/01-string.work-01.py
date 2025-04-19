# 一.str的不可变 immutable
# 因为str在内容里面，str定义的部分只是在内存中占了一个位置
# 如果修改字符串会报错,提示str object does not support item assignment
'''eg1'''
# test_string="abc"
# test_string[0]="e"
# print(test_string)

'''eg2'''
test_string='python'
test_string="python"
test_string='''python'''
test_string="I'm an engineer"
test_string='please study "python"'
test_string='''hello,string is useful,
      such as "python"
'''

print(test_string)