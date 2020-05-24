# default global variables

from threading import Semaphore

QUEEN_NUM = 8

COLUMNS = [-1 for i in range(8)]

STOP_FLAG = False

RET_FLAG = False

SLEEP_TIME = 1000

semStop = Semaphore(0)
