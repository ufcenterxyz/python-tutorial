students_system={
    "jack":{
        "score":90
        },
    "bob":{
        "score":90
        },
}

# 1.添加学生
# 2.删除学生
# 3.查看所有学生
# 4.查找特定学生
# 5.退出系统

students_system['student3']={
        "name":"I",
        "score":100
        }
print(students_system)

del students_system["student3"]
print(students_system)

for i in students_system:
    print(students_system[i])
    print(students_system.keys())