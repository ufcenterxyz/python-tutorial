# 实现异步任务取消
import asyncio
async def fut():
    print(2)
async def main():
    count=0
    while True:
        await asyncio.wait_for(fut(),timeout=1)
        if count==3:
            break
asyncio.run(main())