import asyncio
import sys
import threading



class A(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = False

    async def _main(self):
        tasks = []
        function_list = [func for func in dir(self) if callable(getattr(self, func)) and func.startswith('_') is False and func != 'run' and func.startswith('a_') is True]
        print(function_list)
        for func in function_list:
            tasks.append(asyncio.create_task(getattr(self, func)()))
        await asyncio.gather(*tasks)

    def run(self):
        asyncio.run(self._main())


class B(A):
    def __init__(self):
        super().__init__()

    async def a_test1(self):
        for i in range(5):
            print('B -> a_test1', i)
            await asyncio.sleep(0)
        # self.result_test1 = 100

    async def a_test2(self):
        for i in range(10):
            print('B -> a_test2', i)
            await asyncio.sleep(0)
        # self.result_test2 = 100

    def test3(self):
        return 300


class C(A):

    async def a_test1(self):
        for i in range(5):
            print('C -> a_test1', i)
            await asyncio.sleep(0)
        # self.result_test1 = 100

    async def a_test2(self):
        for i in range(10):
            print('C -> a_test2', i)
            await asyncio.sleep(0)
        # self.result_test2 = 100

    def test3(self):
        return 300


if __name__ == '__main__':
    b = B()
    b.start()
    c = C()
    c.start()
    print('MAIN THREAD')

    # c = C()
    # c.run()
    # print(b.result_test1)
    # print(b.result_test2)
    # print(b.test3())



