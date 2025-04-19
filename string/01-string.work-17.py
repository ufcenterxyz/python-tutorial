log="INFO:2025-03-26 12:00:05:User 'admin' logged in successfully"
new_log=log.split()
print(new_log)
new_log_info=new_log[0][5:]
new_log_date=new_log[1][:-5]
new_add_info=new_log_info+ " " +new_log_date
print(new_log_date)
print(f'''
    level:{new_log[0][:4]},
    Datetime:{new_add_info}
    User:{new_log[2][1:6]}
''')