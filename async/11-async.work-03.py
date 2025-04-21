# 实现异步计数器
import asyncio
async def count_add(name,limit):
    for i in range(limit):
        print(f"""{i}.{name}""")
        await asyncio.sleep(i)

asyncio.run(count_add("count",3))

