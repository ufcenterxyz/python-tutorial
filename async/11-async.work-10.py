import asyncio
count=0

lock=asyncio.Lock()
async def count_fun():
    global count
    async with lock:
        temp=count
        await asyncio.sleep(0.01)
        count=temp+1
    
async def main():
    result=[count_fun() for _ in range(1000)]
    await asyncio.gather(*result)
    # print(count) 输出1000
    

asyncio.run(main())


