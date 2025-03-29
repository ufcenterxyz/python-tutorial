one_dict={"name":"li"}
two_dict={"age":40}
final_dict={}
final_dict.update(one_dict)
final_dict.update(two_dict)
print(final_dict)

#methods 2
final_dict={**one_dict,**two_dict}
print(f"methods2:{final_dict}")