import contextvars
import asyncio
var =contextvars.ContextVar("var",default=0)
async def fun_context_get():
    var.get()
    print(1)
    
async def fun_context_set():
    var.set(1)
    print(2)
    
async def main():
    await asyncio.gather(fun_context_get(),fun_context_set())

asyncio.run(main())