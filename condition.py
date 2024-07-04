import asyncio

async def condition_test(cond):
    async with cond:
        await cond.wait()
        print("ok")
        # Perform some operation after wait
async def main():
    cond = asyncio.Condition()
    task = asyncio.create_task(condition_test(cond))
    
    await asyncio.sleep(1)
    await cond.acquire()
    cond.notify()
    cond.release()
    await task

asyncio.run(main())