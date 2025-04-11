import math
def calculate_area(args,**kwargs):
    # 详细的文档字符串，描述用途、参数和返回值
    print(args)
    if args=="triangle":
        return 1/2 * kwargs["base"]*kwargs["height"]
    elif args=="rectangle":
        return kwargs["length"]*kwargs["width"]
    elif args=="circle":
        return kwargs["radius"]*kwargs["radius"]*math.pi
result=calculate_area('circle', radius=5)
print(result)

