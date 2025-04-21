import asyncio
# 创建一个协程函数,协程可以被挂起和恢复，时间循环：async用于定义异步函数，await用于挂起当前函数
async def main():
    print("hello")
    await asyncio.sleep(1)
    print("World")
    
asyncio.run(main())