# 7复杂切片/
record="20250326Alice   99   X"
Date=record[:8]
Name=record[8:15]
Score=record[16:20]
Flag=record[-1]
print({
     'Date':Date,
     'Name':Name.strip(),
     'Score':str(Score).strip(),
     'Flag':Flag
})

print(f'Date: {Date}')