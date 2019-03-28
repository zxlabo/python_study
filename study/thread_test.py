import threading
from threading import current_thread
import time

'''
多线程
'''


def my_thread():
    print(current_thread().getName())


for i in range(1, 6):
    t1 = threading.Thread(target=my_thread(), args=(1, 2))
    t1.start()
