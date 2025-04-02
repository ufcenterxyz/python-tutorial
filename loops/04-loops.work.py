# for  i in list(range(0,10,2)):
#     print(i)
    
a_dict={1:"one",2:"two",3:"three"}
sorted_dict=sorted(a_dict.keys())

# for i in sorted_dict:
#     print(i)
    
# i=0
# while i<10:
#     print(i)
#     if i==5:
#         break
#     i+=1

i=0
while i<10:
    if i==3:
        i+=1
        continue
    print(i)    
    if i==5:
        break
    i+=1
        