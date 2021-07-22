from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

from mySerial import *


def getData(s):
    s = str(s)
    # print(s)
    a = s
    s = s.replace("b", "")
    s = s.replace("'", "")
    s = s.replace("\n", "")

    # print(s[:-4])
    try:
        s = float(s[:-4])  # python 3
        # s = int(s)  # python 2
    except:
        print(a)
        s = None

    return s


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.sample = 1000
        self.resize(1200, 400)
        self.plotWidget_ted1 = pg.PlotWidget(self)
        self.plotWidget_ted1.setGeometry(QtCore.QRect(0, 0, 1200, 400))
        self.setWindowTitle("ecg graph")
        self.data1 = [0] * self.sample
        self.curve1 = self.plotWidget_ted1.plot(self.data1, clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.start(1)
        self.timer.timeout.connect(self.update_data)
        self.index = 0

    data1 = [0] * 1000
    def update_data(self):
        global data1
        # ---------------------Averaging----------
        dd = []
        for _ in range(2):
            s = read_serial_readline()
            s = getData(s)
            if s is not None:
                dd.append(s)

        avg = 0
        for i in dd:
            avg += i
        avg = avg/2
        s = avg

        try:
            value = s
            # print(value)
            # --------------Overlap GRAPH-----------
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value

            # --------------Overlap GRAPH-----------
            # self.data1[self.index] = value

            self.curve1.setData(self.data1)
            # print("Number of Sample: {}".format(1000*20))
            self.index += 1
            if self.index > self.sample-1:
                self.index = 0
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    import sys

    configure_port('COM3', 115200)
    open_port()

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
