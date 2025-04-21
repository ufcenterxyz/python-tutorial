# 编写一个异步函数，尝试获取url
import asyncio
import aiohttp


async def fetch_url():
    try:
        url="https://httpbin.org/get"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
    except aiohttp.ClientError as e:
        return None
    
    
async def main():
    try:
        result = await asyncio.wait_for(fetch_url(),timeout=0.5)  
        print(result)  
    except TimeoutError:
        print("超时")

asyncio.run(main())            
            
