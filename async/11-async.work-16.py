# 异步流水线操作
import asyncio
import math


async def fun_generate(queue):
    for i in range(1,11):
        await queue.put(i)
        print(i)
        await asyncio.sleep(0.1)
    await queue.put(None)


async def fun_handle_sqrt(queue):
    while True:
        n=await queue.get()
        if n is None:
            break
        item=n*n
        print(item)


async def main():
    queue=asyncio.Queue()
    await asyncio.gather(fun_generate(queue),fun_handle_sqrt(queue))

asyncio.run(main())
