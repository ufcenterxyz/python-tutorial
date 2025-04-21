import aiofiles
import asyncio
async def read_file():
    try:
        async with aiofiles.open("async/file.txt","r") as f:
                content=await f.read()
                print(content)
    except FileExistsError:
            print("file doesn't exist")
asyncio.run(read_file())

