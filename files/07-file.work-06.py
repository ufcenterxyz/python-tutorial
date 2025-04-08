# 错误处理
try:
    with open("nonexistent.txt","r") as file_handler:
        file_handler.read()
except IOError :
    print("IOError")
finally:
    print("文件找不到")