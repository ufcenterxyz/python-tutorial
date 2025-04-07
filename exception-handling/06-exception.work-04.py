def file_read(file_path):
    try:
        if file_path:
            f = open(file_path, "r")
            print(f.read())
    except FileNotFoundError:
        print("FileNotFoundError")
result=file_read("loops/hello.txt")
print(result)
