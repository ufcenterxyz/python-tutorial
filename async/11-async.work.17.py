import asyncio
import time

async def fun_y():
    for i in range(1,11):
        await asyncio.sleep(1)
        print(i)
        
def fun_t():
    print("start")
    time.sleep(5)
    print("end")
    
async def main():
    await asyncio.gather(fun_y(),asyncio.to_thread(fun_t))

asyncio.run(main())

