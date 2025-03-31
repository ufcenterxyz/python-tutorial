choice1=f"choice:1.查看信息"
choice2=f"choice:2.添加信息"
choice3=f"choice:3.删除信息"
choice4=f"choice:4.退出"
print(f'''
      {choice1},
      {choice2},
      {choice3},
      {choice4}
''')

try:
        message=int(input("choice:"))

        if message>4:
                print("请重新检查输入")
        if message==1:
                print("查看信息")
        elif message==2:
                print("添加信息")
        elif message==3:
                print("删除信息")
        elif message==4:
                print("退出")
except:
        print('请重新检查输入')


