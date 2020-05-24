import sys
import globals
import time
from threading import Thread
from PySide2.QtCore import Signal, QObject

class SingalUpdateView(QObject):
    sigUpdateView = Signal()

class Solver(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.signals = SingalUpdateView()

    def run(self):
        print('start to run')
        self.dfs(0)
        print('run finished')

    def dfs(self, row):
        for c in range(globals.QUEEN_NUM):
            if self.isOk(row, c):
                globals.COLUMNS[row] = c; 
                if row == globals.QUEEN_NUM - 1:
                    # self.printChessboard()
                    self.signals.sigUpdateView.emit()
                    time.sleep(globals.SLEEP_TIME / 1000)
                    if globals.STOP_FLAG == True:
                        globals.semStop.acquire()
                else:
                    if globals.RET_FLAG == True:
                        return
                    self.dfs(row + 1)
        globals.COLUMNS[row] = -1

    def isOk(self, row, col) -> bool:
        for r in range(row):
            if globals.COLUMNS[r] == col:
                return False
            if globals.COLUMNS[r] + r == row + col or\
            globals.COLUMNS[r] - r == row -col:
                return False
        return True

    def printChessboard(self):
        for r in range(globals.QUEEN_NUM):
            for c in range(globals.QUEEN_NUM):
                if globals.COLUMNS[r] == c:
                    print('Q ', end='')
                else:
                    print('* ', end='')
            print('')
        print('')


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('usage: {} SIZE'.format(sys.argv[0]))
        sys.exit(1)
    globals.QUEEN_NUM = int(sys.argv[1])
    solver = Solver()
    solver.start()
