import datetime
file_time=str(datetime.datetime.now())
x=""
def log_message(message):
    with open("files/07-file.work-log.log","w") as file_handler:
        file_handler.write("  %s\n" % file_time+message)
log_message("aaaa")
print(log_message("aaaa"))


def read_log(last_ten):
    with open("files/07-file.work-log.log") as file:
        file.readlines()   
    read_log(last_ten)


