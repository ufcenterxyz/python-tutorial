# 实现异步Http请求

import asyncio
import aiohttp

async def http_fun(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.status
    except aiohttp.ClientError as e:
        print("请求错误") 
        return None   
async def main():
    url="https://invalid.url"
    html=await http_fun(url)
    print(1)
    
asyncio.run(main())
