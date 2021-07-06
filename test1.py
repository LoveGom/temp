import asyncio, datetime
from datetime import datetime

now = datetime.now()

async def wait():
    while not now.hour == 18:
        asyncio.sleep(0.1)

async def task():
    print("task1")
        

while(True):
    try:
        wait()
        task()
    except KeyboardInterrupt:
        exit