import asyncio
from time import perf_counter



async def main():
    start = perf_counter()
    print("Start of main coroutine")
    total = await asyncio.sleep(3)        

    end = perf_counter() - start

    print(end)





asyncio.run(main())