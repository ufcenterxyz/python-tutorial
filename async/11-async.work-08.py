# 实现异步生成器
# 实现异步生成器，每隔一秒数字递增，总共5个数字
import asyncio

async def generator():
    count=0
    for i in range(1,6):
        count+=1
        await asyncio.sleep(1)
        yield i

async def main():
        async for i in generator():
            print(i)
asyncio.run(main())
    