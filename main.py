import sys
import globals
import solver
from PySide2 import QtWidgets, QtCore, QtGui
from myform import Ui_Form

DEBUG = True

def dprint(content):
    if DEBUG:
        print(content)

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.editNum.setText('8')
        self.setWindowTitle('NQueen Problem Visualizer')

        self.isStarted = False
        self.lastCols = [0 for i in range(globals.QUEEN_NUM)]

        # table
        self.setTable(globals.QUEEN_NUM)

        # buttons
        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(False)
        self.ui.btnReset.setEnabled(False)

        # connect
        self.ui.btnExit.clicked.connect(lambda: sys.exit(1))
        self.ui.btnConfirm.clicked.connect(self.btnConfirm_clicked)
        self.ui.btnStart.clicked.connect(self.btnStart_clicked)
        self.ui.btnStop.clicked.connect(self.btnStop_clicked)
        self.ui.btnReset.clicked.connect(self.btnReset_clicked)
        self.ui.slider.valueChanged.connect(self.changeSleepTime)

        self.setFixedSize(800, 480)
        self.show()

    def setTable(self, size):
        tableWidth = self.ui.table.width() - 5
        tableHeight = self.ui.table.height() - 5
        self.ui.table.setRowCount(size)
        self.ui.table.setColumnCount(size)
        self.ui.table.verticalHeader().setVisible(False)
        self.ui.table.horizontalHeader().setVisible(False)
        for i in range(size):
            self.ui.table.setRowHeight(i, tableHeight / size)
            self.ui.table.setColumnWidth(i, tableWidth / size)

    @QtCore.Slot()
    def btnConfirm_clicked(self):
        self.ui.btnStart.setEnabled(True)
        self.ui.btnConfirm.setEnabled(False)
        self.ui.btnReset.setEnabled(True)
        
        globals.RET_FLAG = False
        globals.QUEEN_NUM = int(self.ui.editNum.text())
        globals.COLUMNS = [-1 for i in range(globals.QUEEN_NUM)]
        self.lastCols = [0 for i in range(globals.QUEEN_NUM)]
        self.setTable(globals.QUEEN_NUM)

    @QtCore.Slot()
    def btnStart_clicked(self):
        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(True)
        globals.STOP_FLAG = False
        if self.isStarted == False:
            self.solver = solver.Solver()
            self.solver.start()
            self.solver.signals.sigUpdateView.connect(self.updateView)
            self.isStarted = True
        else:
            globals.semStop.release()

    @QtCore.Slot()
    def btnStop_clicked(self):
        self.ui.btnStart.setEnabled(True)
        self.ui.btnStop.setEnabled(False)
        globals.STOP_FLAG = True

    @QtCore.Slot()
    def btnReset_clicked(self):
        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(False)
        self.ui.btnConfirm.setEnabled(True)
        self.ui.btnReset.setEnabled(False)
        if self.isStarted == True and globals.STOP_FLAG == True:
            globals.semStop.release()
        globals.STOP_FLAG = False
        globals.RET_FLAG = True
        self.isStarted = False
        for i in range(globals.QUEEN_NUM):
            for j in range(globals.QUEEN_NUM):
                self.ui.table.setItem(i, j, None)

    @QtCore.Slot()
    def changeSleepTime(self):
        globals.SLEEP_TIME = 2000 - self.ui.slider.value()
        # dprint(globals.SLEEP_TIME)

    @QtCore.Slot()
    def updateView(self):
        for row in range(globals.QUEEN_NUM):
            col = self.lastCols[row]
            self.ui.table.setItem(row, col, None)
        for row in range(globals.QUEEN_NUM):
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(QtGui.QBrush(QtCore.Qt.red))
            col = globals.COLUMNS[row]
            self.ui.table.setItem(row, col, item)
            self.lastCols[row] = globals.COLUMNS[row]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec_())
