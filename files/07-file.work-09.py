# 大文件处理
count=0
words=0
line_byte=0
with open("files/file.work-09.txt") as file_handler:
    # 行数
    lines=file_handler.readlines()
    for i in lines:
        count+=1
        for n in i.split():
            words+=len(i)
            for b in n:
                line_byte+=1
    print(f"字符数：{line_byte}")
    print(f"单词数：{words}")
    print(f"行数：{count}")

    