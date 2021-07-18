import random as randint

from PyQt5.uic.properties import QtCore
from PySide2.QtWidgets import QWidget, QApplication, QPushButton
import pyqtgraph as pg
import random as randint

import pyqtgraph as pg
from PySide2.QtWidgets import QWidget, QApplication, QPushButton

file = open("C:\\Users\\saba-mampc\\PycharmProjects\\pythonProject2\\gang_gautam_ecg.txt", 'r')
# LA = []
# RA = []
# LL = []
# V1 = []
# V2 = []
# RESPM = []
# V3 = []
# V4 = []
# V5 = []
# V6 = []
# V7 = []
# for i in range(len(data)):
#     if data[i] == "LA":
#         LA.append(float(data[i+1].replace("L",'')))
#     if data[i] == "RA":
#         RA.append(float(data[i+1].replace("L",'')))
#     if data[i] == "LL":
#         LL.append(float(data[i+1].replace("L",'')))
#     if data[i] == "V1":
#         V1.append(float(data[i+1].replace("L",'')))
#     if data[i] == "V2":
#         V2.append(float(data[i+1].replace("L",'')))
#     if data[i] == "RESPM":
#         RESPM.append(float(data[i+1].replace("L",'')))
#     if data[i] == "V3":
#         V3.append(float(data[i+1].replace("L",'')))
#     if data[i] == "V4":
#         V4.append(float(data[i+1].replace("L",'')))
#     if data[i] == "V5":
#         V5.append(float(data[i+1].replace("L",'')))
#     if data[i] == "V6":
#         V6.append(float(data[i+1].replace("L",'')))

# a = int(input("enter the starting value, x:- "))
# b = int(input("enter the last value,y:- "))
# x = int(input("enter the number of samples:- "))
a = -3 * 1000
b = 3 * 1000
x = 4000


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Set the size
        self.resize(900, 800)

        # add buttons
        self.bt1 = QPushButton("start", self)
        self.bt1.clicked.connect(self.cur1)
        self.bt1.move(50, 600)

        self.bt2 = QPushButton("LEAD1", self)
        self.bt2.clicked.connect(self.cur2)
        self.bt2.move(150, 600)

        self.bt3 = QPushButton("LEAD2", self)
        self.bt3.clicked.connect(self.cur3)
        self.bt3.move(250, 600)

        self.bt4 = QPushButton("LEAD3", self)
        self.bt4.clicked.connect(self.cur4)
        self.bt4.move(350, 600)

        self.bt5 = QPushButton("V1", self)
        self.bt5.clicked.connect(self.cur5)
        self.bt5.move(450, 600)

        self.bt6 = QPushButton("V2", self)
        self.bt6.clicked.connect(self.cur6)
        self.bt6.move(550, 600)

        self.bt7 = QPushButton("V3", self)
        self.bt7.clicked.connect(self.cur7)
        self.bt7.move(150, 650)

        self.bt8 = QPushButton("V4", self)
        self.bt8.clicked.connect(self.cur8)
        self.bt8.move(250, 650)

        self.bt9 = QPushButton("V5", self)
        self.bt9.clicked.connect(self.cur9)
        self.bt9.move(350, 650)

        self.bt10 = QPushButton("V6", self)
        self.bt10.clicked.connect(self.cur10)
        self.bt10.move(450, 650)

        self.bt11 = QPushButton("RESP", self)
        self.bt11.move(550, 650)
        self.bt11.clicked.connect(self.cur11)

        self.bt12 = QPushButton("stop", self)
        self.bt12.clicked.connect(self.cur12)
        self.bt12.move(50, 650)

        self.plotWidget_ted = pg.PlotWidget(self)
        # Set the size and relative position of the control
        self.plotWidget_ted.setGeometry(QtCore.QRect(20, 30, 800, 550))
        # self.plotWidget_ted.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.plotWidget_ted.setYRange(a, b)
        # self.plotWidget_ted.setXRange(0, x)
        # layoutgrid.addWidget(self.plotWidget_ted)

        self.setWindowTitle("garph of given value")
        self.plotWidget_ted.setLabel('left', 'values------->')
        self.plotWidget_ted.setLabel('bottom', 'time(ms)------->')

    def cur1(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data1)
        self.timer.start(1)

    def update_data1(self):
        data2 = file.read()
        data2 = data2.replace("\n", ',')
        data2 = data2.replace("(", '')
        data2 = data2.replace(")", '')
        data2 = data2.replace("Data ready", '')
        data2 = data2.replace("'", "")
        data2 = data2.split(",")
        LA = []
        for i in range(len(data2)):
            if data2[i] == "LA":
                LA.append(float(data2[i + 1].replace("L", '')))
        for j in LA:
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = round(j * 1000)
            print(round(j * 1000))
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)

    def cur2(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data2)
        self.timer.start(1)

    def update_data2(self):
        try:
            value = randint(a, a + 50)
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)
            print(value)
        except Exception as e:
            print(str(e))

    def cur3(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data3)
        self.timer.start(1)

    def update_data3(self):
        try:
            value = randint(a + 50, a + 100)
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)
            print(value)
        except Exception as e:
            print(str(e))

    def cur4(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data4)
        self.timer.start(1)

    def update_data4(self):
        try:
            value = randint(a + 100, a + 150)
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)
            print(value)
        except Exception as e:
            print(str(e))

    def cur5(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data5)
        self.timer.start(1)

    def update_data5(self):
        try:
            value = randint(a + 150, a + 200)
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)
            print(value)
        except Exception as e:
            print(str(e))

    def cur6(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data6)
        self.timer.start(1)

    def update_data6(self):
        try:
            value = randint(a + 200, a + 250)
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)
            print(value)
        except Exception as e:
            print(str(e))

    def cur7(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data7)
        self.timer.start(1)

    def update_data7(self):
        try:
            value = randint(a + 250, a + 300)
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)
            print(value)
        except Exception as e:
            print(str(e))

    def cur8(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data8)
        self.timer.start(1)

    def update_data8(self):
        try:
            value = randint(a + 300, a + 350)
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)
            print(value)
        except Exception as e:
            print(str(e))

    def cur9(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data9)
        self.timer.start(1)

    def update_data9(self):
        try:
            value = randint(a + 350, a + 400)
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)
            print(value)
        except Exception as e:
            print(str(e))

    def cur10(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data10)
        self.timer.start(1)

    def update_data10(self):
        try:
            value = randint(a + 400, a + 450)
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)
            print(value)
        except Exception as e:
            print(str(e))

    def cur11(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data11)
        self.timer.start(1)

    def update_data11(self):
        try:
            value = randint(a + 450, a + 500)
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)
            print(value)
        except Exception as e:
            print(str(e))

    def cur12(self):
        self.data1 = [0] * x
        # print(self.data1)
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1", clear=True)
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data12)
        self.timer.start(1)

    def update_data12(self):
        try:
            value = 0
            self.data1[:-1] = self.data1[1:]
            self.data1[-1] = value
            # Data is filled into the drawing curve
            self.curve1.setData(self.data1)
            print(value)

        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    import sys

    # PyQt5 Program fixed writing
    app = QApplication(sys.argv)
    # Instantiate and display the window bound to the drawing control
    window = Window()
    window.show()
    # PyQt5 Program fixed writing
    sys.exit(app.exec_())
