names = ["Alice", "Bob", "Charlie"] 
scores = [85, 55, 65]

# def level(value):
#     return "及格" if value >= 60 else "不及格"
    
result={ i:"及格" if value >= 60 else "不及格" for i,value in zip(names,scores)}
print(result)