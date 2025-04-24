import asyncio
event=asyncio.Event()
async def fun1():
    await asyncio.sleep(3)
    event.set()
    print(1)
    
async def fun2():
    await event.wait()
    print(2)

async def main():
    await asyncio.gather(fun1(),fun2())
    
asyncio.run(main())
    