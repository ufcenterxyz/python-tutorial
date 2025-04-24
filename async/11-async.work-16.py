# 异步流水线操作
import asyncio
import math


async def fun_generate(queue):
    for i in range(1,11):
        await queue.put(i)
        print(i)
        await asyncio.sleep(0.1)
    await queue.put(None)


async def fun_handle_sqrt(inter_queue,outer_queue):
    while True:
        n=await inter_queue.get()
        if n is None:
            await outer_queue.put(None)
            break
        item=n*n
        await outer_queue.put(item)
        
        
async def saver(outer_queue):
    while True:
        o=await outer_queue.get()
        if o is None:
            break
        print(o)
    


async def main():
    queue=asyncio.Queue()
    outer_queue=asyncio.Queue()
    await asyncio.gather(fun_generate(queue),fun_handle_sqrt(queue,outer_queue),saver(outer_queue))

asyncio.run(main())
