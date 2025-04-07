def file(path):
    try:
        f=open(path,"r")
        return f.read()
    except FileNotFoundError:
        print("FileNotFoundError")
file("exception-handling/06-exception.work-11.py")
print(file("exception-handling/06-exception.work-111.py"))    