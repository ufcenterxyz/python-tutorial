import asyncio

async def main(fun1):
    print("main")
    await asyncio.sleep(1)
    return await fun1()

async def fun1():
    print("fun1")

asyncio.run(main(fun1))