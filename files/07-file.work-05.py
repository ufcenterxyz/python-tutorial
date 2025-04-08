# 文件追加
import datetime
x=datetime.datetime.now()
print(x)
with open("files/log.txt","a") as file_handler:
    file_handler.write(str(x))
