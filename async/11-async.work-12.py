# 创建长时间运行的协程
import asyncio
async def fun1():
    while True:
        print(1)
        await asyncio.sleep(1)
async def main():
    try:
        for i in range(10):
            task=asyncio.create_task(fun1())
            if i==2:
                await asyncio.sleep(2)
                task.cancel()
                await task
    except asyncio.CancelledError:
        print("error")

asyncio.run(main())
    
        
    