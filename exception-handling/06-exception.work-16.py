def file(file_path):
    try:
        with open(file_path,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print("filenotFoundError")
file("exception-handling/06-exception.work-15.py")
