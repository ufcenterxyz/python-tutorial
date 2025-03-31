students_system={
    "jack":{
        "score":100
        },
    "bob":{
        "score":90
        },
}

# 1.添加学生
# 2.删除学生
# 3.查看所有学生
# 4.查找特定学生
# 5.退出系统)

print('''学生管理系统
1.添加学生
2.删除学生
3.查看所有学生
4.查找特定学生
5.退出系统''')

name=input("添加学生name: ")
while True:
    students_system[name]={
        "score":70
    }
    print(students_system)
    break

delete=input("想要删除哪位学生的信息： ")
while True:
    students_system.pop(delete)
    print(students_system)
    break


look=input(f"是否查看所有学生nameY/N: ")
try:
                if look=="Y" or look=="y":
                    print(students_system)
                elif look=="N" or look=="n":
                    print("你想查看哪位学生的分数？请输入你想要查看的学生姓名：")
                    print(students_system)
                    student_name=input("student name:")
                    for i in students_system:
                        if i==student_name:
                            print(students_system[i])
                    if student_name!=i:
                        print("请根据student_system中提供的学生姓名，重新输入")
                        print("你想查看哪位学生的分数？请输入你想要查看的学生姓名：")
                        print(students_system)
                        student_name=input("student name:")
                        for i in students_system:
                            if i==student_name:
                                print(students_system[i])
                else:
                    print("请检查您的输入，只能输入Y/N")
except:
    print("请检查您的输入")
    
while True:
    exit=input("要退出系统吗？Y/N ")
    if exit=="Y" or exit=="y":
        print("你已退出程序")
    break

