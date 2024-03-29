import asyncio
async def count():
    print("Async One")
    await asyncio.sleep(5)
    print("Async Two")
def sync_count():
    print("Sync One")
    time.sleep(5)
    print("Sync Two")
async def main():
    await asyncio.gather(count(), count(), count())
import time
starttime = time.perf_counter()
for _a in range(3):
    sync_count()
print(f"executed in {(time.perf_counter() - starttime):0.2f} seconds.")
starttime = time.perf_counter()
asyncio.run(main())
print(f"executed in {(time.perf_counter() - starttime):0.2f} seconds.")
