import asyncio
async def task1():
    print(1)
    await asyncio.sleep(1)
async def task2():
    print(2)
    await asyncio.sleep(2)

async def task3():
    print(3)
    await asyncio.sleep(3)

async def main():
    await asyncio.gather(task1(),task2(),task3())
asyncio.run(main())
