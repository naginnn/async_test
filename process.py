import threading
import time

class ClockThread(threading.Thread):

    def __init__(self, interval):
        super(ClockThread, self).__init__()
        # если False не дает основному потоку закончить работу пока сам не закончит
        # если True то основной поток закончит, а поток продолжит работу
        self.daemon = False
        self.interval = interval

    def run(self):
        while True:
            print("The time is %s" % time.ctime())
            time.sleep(self.interval)

if __name__ == '__main__':
    t = ClockThread(1)
    t.start()
    time.sleep(3)
    print("eby alibaby")