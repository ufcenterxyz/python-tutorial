# 1.start
# 2.输入主程序

# 3.用户选择
student_list={}
while True:
    info=print(f'''用户信息如下，请选择
1.添加学生
2.删除学生
3.查看所有学生
4.查看特定学生
5.退出程序           
''')
    try:
        user_input=int(input("请输入1-5之间的数字： "))
        if user_input==1:
            student_name=input("student name: ").strip().lower()
            if student_name in student_list:
                print("该学生已存在")
            else:
                while True:
                    try:
                        score=int(input("score:"))
                        if 0<=score<=100:
                            student_list[student_name]={
                                "score":score
                            }
                            print(f"student信息如下：{student_list}")
                        else:
                            print("请输入1-100之间的数字")    
                        break
                    except ValueError:
                        print("请输入1-100之间的数字")
        elif user_input==2:
            while True:
                try:
                    delete_name=input("要删除哪位学生，请输入学生姓名: ").strip().lower()
                    if delete_name in student_list:
                        del student_list[delete_name]
                        print(f"学生列表：{student_list}")
                    else:
                        print("请输入列表中的学生姓名")
                except ValueError:
                    print("请输入正确的学生姓名")
                break 
        elif user_input==3:
            while True:
                print(f"所有的学生： {student_list}")
                break
        elif user_input==4:
            while True:
                try:
                    student_name=input("要查找的学生姓名: ").strip()
                    print(student_list)
                    if student_name in student_list: 
                        print(f"当前查找的该学生分数：{student_name} 的分数是{student_list[student_name]}")
                        break
                    else:
                        print("该学生不存在") 
                except ValueError:
                    print("输入正确的姓名")
        elif user_input==5:
            print("退出程序")
            break
        else:
            print("请输入1-5之间的数字，请重新输入") 
            break  
    except ValueError:
        print("请输入1-5之间的数字，请重新输入")