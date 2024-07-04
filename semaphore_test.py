import asyncio

async def limited_access(sem):
    async with sem:
        # Perform task
        print("Accessing limited resource")
        await asyncio.sleep(1)

async def main():
    sem = asyncio.Semaphore(2)
    await asyncio.gather(limited_access(sem), limited_access(sem), limited_access(sem))

asyncio.run(main())