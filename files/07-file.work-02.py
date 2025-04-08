sum=0
try:
    with open("files/linetxt.txt","r") as file_lines:
        for line in file_lines:
            sum+=int(line)
        print(sum)
except IOError:
    print("IOError has occurred!")