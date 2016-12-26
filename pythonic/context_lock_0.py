from threading import Lock
lock = Lock()

def do_something_dangerous():
    lock.acquire()
    raise Exception('oops I forgot this code could raise exceptions')
    lock.release()

try:
    do_something_dangerous()
except:
    print('Got an exception')
lock.acquire()
print('Got here')