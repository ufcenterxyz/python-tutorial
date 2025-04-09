# 模块别名
import datetime as dt
time=dt.datetime.now().year
month=dt.datetime.now().month
date=dt.datetime.now().day
hour=dt.datetime.now().hour
minute=dt.datetime.now().minute
second=dt.datetime.now().second
print(f"当前时间：{time}-{month}-{date} {hour}:{minute}:{second}")
print(f"过一段时间：{time}-{month}-{date+5} {hour}:{minute}:{second}")





