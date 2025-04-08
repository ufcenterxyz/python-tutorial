try:
    with open("files/name.txt","w") as file_handler:
        for i in range(0,5):
            user_input=input("input name: ")
            file_handler.write("  %s\n" % user_input)
except IOError:
    print("IO has an error")
