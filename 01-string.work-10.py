# 10str.format()
new_str="Python is as simple as {0},{1},{2}".format("a","b","c")
print(new_str)

# 10.2
xy={"x":5,"y":10}
new_str_format="The point is x={x},y={y} ".format(**xy)
print(new_str_format)