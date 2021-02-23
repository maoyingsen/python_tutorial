
import asyncio  
import time  
from datetime import datetime

"""
async def custom_sleep():  
    print('SLEEP', datetime.now())
    time.sleep(1)

async def factorial(name, number):  
    f = 1
    for i in range(2, number+1):
        print('Task {}: Compute factorial({})'.format(name, i))
        await custom_sleep()
        f *= i
    print('Task {}: factorial({}) is {}n'.format(name, number, f))


start = time.time()  
loop = asyncio.get_event_loop()

tasks = [  
    asyncio.ensure_future(factorial("A", 3)),
    asyncio.ensure_future(factorial("B", 4)),
]
loop.run_until_complete(asyncio.wait(tasks))  
loop.close()

end = time.time()  
print("Total time: {}".format(end - start)) 
"""
"""
output
Task A: Compute factorial(2)
SLEEP 2021-02-23 16:14:42.327061
Task A: Compute factorial(3)
SLEEP 2021-02-23 16:14:43.329401
Task A: factorial(3) is 6n
Task B: Compute factorial(2)
SLEEP 2021-02-23 16:14:44.332196
Task B: Compute factorial(3)
SLEEP 2021-02-23 16:14:45.332729
Task B: Compute factorial(4)
SLEEP 2021-02-23 16:14:46.334223
Task B: factorial(4) is 24n
Total time: 5.031582832336426
"""
"""
async def custom_sleep():  
    print('SLEEP {}n'.format(datetime.now()))
    await asyncio.sleep(1)

async def factorial(name, number):  
    f = 1
    for i in range(2, number+1):
        print('Task {}: Compute factorial({})'.format(name, i))
        await custom_sleep()
        f *= i
    print('Task {}: factorial({}) is {}n'.format(name, number, f))


start = time.time()  
loop = asyncio.get_event_loop()

tasks = [  
    asyncio.ensure_future(factorial("A", 3)),
    asyncio.ensure_future(factorial("B", 4)),
]
loop.run_until_complete(asyncio.wait(tasks))  
loop.close()

end = time.time()  
print("Total time: {}".format(end - start))
"""
"""
Task A: Compute factorial(2)
SLEEP 2021-02-23 16:28:20.542867n
Task B: Compute factorial(2)
SLEEP 2021-02-23 16:28:20.543866n
Task A: Compute factorial(3)
SLEEP 2021-02-23 16:28:21.545566n
Task B: Compute factorial(3)
SLEEP 2021-02-23 16:28:21.546566n
Task A: factorial(3) is 6n
Task B: Compute factorial(4)
SLEEP 2021-02-23 16:28:22.547926n
Task B: factorial(4) is 24n
Total time: 3.0077457427978516
"""


import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
#tasks = [hello(), hello()]
#loop.run_until_complete(asyncio.wait(tasks))
#tasks = []
loop.run_until_complete(asyncio.gather(hello(), hello()))
loop.close()