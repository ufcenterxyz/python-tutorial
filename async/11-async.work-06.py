# 实现并发http请求处理
import aiohttp
import asyncio

url1="https://httpbin.org/get"

url2="https://api.github.com"

url3="https://jsonplaceholder.typicode.com/posts/1"

async def fun_url(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(response)
                return await response.text()             
    except aiohttp.ClientError as e:
        return None
async def fetch_url1():
    result=await fun_url(url1)  
    print(f"""url1: {result}""")
async def fetch_url2():
    result=await fun_url(url2)
    print(f"""url2: {result}""")
async def fetch_url3():
    result=await fun_url(url3)
    print(f"""url3:{result}""")

async def main():
    await asyncio.gather(fetch_url1(),fetch_url2(),fetch_url3())
asyncio.run(main())

        