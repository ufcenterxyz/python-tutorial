name=input("admin:")
password=input("password:")

if name=="admin" and password=="password":
    print("登录成功")
if name!="admin" or password!="password":
    print("用户名或者密码错误")
