list1=["Hello world", "Python is awesome", "I am learning"]
list_sentence=[sentence.split() for sentence in list1 ]
new_list=[]
for word in list_sentence:
    count=0
    for i in word:
        if len(i)>3:
            count+=1
    new_list.append(count)
print(new_list)    