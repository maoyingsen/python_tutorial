import asyncio

async def main():
    print("Sleep now.")
    await asyncio.sleep(1.5)
    print("OK, wake up!")

asyncio.run(main())