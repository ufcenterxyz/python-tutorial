def mysql():
    try:
        return "连接数据库"
    except LookupError:
        print("连接错误")
    finally:
        print("关闭连接")
mysql()
    