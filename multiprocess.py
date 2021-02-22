from multiprocessing import Process
import os, time, datetime, random, tracemalloc

tracemalloc.start()
children = 4    # number of child processes to spawn
maxdelay = 6    # maximum delay in seconds

def status():
    return ('Time: ' + 
        str(datetime.datetime.now().time()) +
        '\t Malloc, Peak: ' +
        str(tracemalloc.get_traced_memory()))

def child(num):
    delay = random.randrange(maxdelay)
    print(f"{status()}\t\tProcess {num}, PID: {os.getpid()}, Delay: {delay} seconds...")
    time.sleep(delay)
    print(f"{status()}\t\tProcess {num}: Done.")

if __name__ == '__main__':
    print(f"Parent PID: {os.getpid()}")
    for i in range(children):
        proc = Process(target=child, args=(i,))
        proc.start()