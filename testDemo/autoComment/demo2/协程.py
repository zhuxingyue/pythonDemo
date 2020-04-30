import asyncio
import threading
import time

@asyncio.coroutine
def get_body(i):
    print(f'start{i}')
    yield from asyncio.sleep(1)
    print(f'end{i}')

loop = asyncio.get_event_loop()
tasks = [get_body(i) for i in range(5)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

def test1(num):
    for i in range(num):
        print("子线程运行" + str(i))
        time.sleep(1)


t1 = threading.Thread(target=test1,args=(10,))
t1.start()
for i in range(100):
    print("主线程运行" + str(i))
    time.sleep(0.5)