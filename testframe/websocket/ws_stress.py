# coding=utf-8
import json
import asyncio
import threading
import websockets
import multiprocessing
from threadpool import ThreadPool, makeRequests
from testframe.common.base_common import BaseCommon


class WSStress(BaseCommon):
    def __init__(self, url, messages, processes=1, threads=1, headers=None):
        self.url = url
        self.messages = messages
        self.headers = headers

        self.processes = processes if isinstance(processes, int) else int(processes)
        self.threads = threads if isinstance(threads, int) else int(threads)

        self.start_num = 0
        self.err_count = 0

    async def stress_connect(self, url, message, headers=None, sleep=59):
        message = message if isinstance(message, dict) else message[0] if isinstance(message, list) else str(message)
        headers = None if headers in ["", {}, {'': ''}] else headers
        sleep = sleep if isinstance(sleep, int) else int(sleep)
        try:
            async with websockets.connect(url, extra_headers=headers) as websocket:
                self.start_num = self.start_num + 1

                async def con():
                    while True:
                        await websocket.send(json.dumps(message))
                        # print("> {}".format(message))
                        data = await websocket.recv()
                        print("< {}".format(data))
                        if sleep > 0:
                            await asyncio.sleep(sleep)

                t = threading.Thread(target=(await con()))
                t.start()
        except Exception as e:
            self.loggers.error('Connect error:  %s' % e)
            self.err_count += 1

    def start(self, num):
        num += 1
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.stress_connect(self.url, self.messages, self.headers))

    def thread_web_socket(self):
        # 线程池
        pool_list = ThreadPool(self.threads)
        num = list()
        # 设置开启线程的数量
        for ir in range(self.threads):
            num.append(ir)
        requests = makeRequests(self.start, num)
        [pool_list.putRequest(req) for req in requests]
        pool_list.wait()

    def run(self):
        # 进程池
        pool = multiprocessing.Pool(processes=self.processes)
        # 设置开启进程的数量
        for i in range(self.processes):
            import time
            time.sleep(2)
            pool.apply_async(self.thread_web_socket)
        pool.close()
        pool.join()

        self.loggers.debug('Strated count:  %s' % self.start_num)
        if int(self.err_count) != 0:
            self.loggers.error('Error count:  %s' % self.err_count)

if __name__ == "__main__":
    WS_URL = "ws://192.168.2.134:8081"
    message = "8" * 1024 * 1024
    WSStress(WS_URL, message).run()
