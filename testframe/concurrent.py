from gevent import monkey

monkey.patch_all()
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0)


gevent.joinall([
    gevent.spawn(f, 5),
    gevent.spawn(f, 4),
    gevent.spawn(f, 5),
])
