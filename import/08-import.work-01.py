# 编写一个程序，使用 math 模块计算圆的面积和周长。用户输入圆的半径，程序输出对应的面积和周长。
import math
r=int(input("圆的半径： "))
s=math.pi*r*r

l=2*math.pi*r
print(f"面积：{s},周长：{l}")