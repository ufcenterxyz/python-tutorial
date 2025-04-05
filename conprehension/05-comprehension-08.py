input1={"a": 5, "b": 15, "c": 10, "d": 20}
input2={i:value for i,value in input1.items() if value>10}
print(input2)