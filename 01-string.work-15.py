txt="abracadabra"
output=""
new_txt={}
for i in txt:
    if new_txt.get(i) is None:
        
        output+=i
        new_txt[i]=1
print(output)