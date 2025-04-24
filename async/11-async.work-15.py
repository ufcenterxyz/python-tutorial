# 异步流控制，他限制并发并执行的协程数量不超过3个
import asyncio
async_three=asyncio.Semaphore(3)
async def download(url):
    async with async_three:
        await asyncio.sleep(1)
        print(url)


async def main():
    task= [download(i) for i in range(10)]
    await asyncio.gather(*task)

asyncio.run(main())