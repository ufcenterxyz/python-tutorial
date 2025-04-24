# 异步与同步代码集成
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
    result=asyncio.to_thread(fun_t)
    await asyncio.gather(fun_y(),result)
    
asyncio.run(main())