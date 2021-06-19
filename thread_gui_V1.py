'''
Description: 
Status: Working
@Nitish Sharma
'''

from PyQt5 import QtCore, QtGui
import pyqtgraph as pg
# from communicationGang import *
from time import sleep
from multiprocessing import Queue
import threading
import numpy as np
import sys
from random import randint

# -------------------------ADAS1000SDZ-----------------------------------
global channel
channel = 2
try:
    channel = int(sys.argv[1])
    print(int(channel[1]))
except:
    pass

x = 400


def voltage(ADCDecimal):
    ecg = 0
    if ADCDecimal > 8388608:
        ecg = ((4 * 1.8 * (-(16777216 - ADCDecimal)) / 1.4) / (16777215))
    else:
        ecg = ((4 * 1.8 * ADCDecimal) / 1.4) / (16777215)
    return ecg


def resetting():
    print("Resetting Device..")
    sleep(0.5)
    # reset_device()
    print("Device Resettled!")
    sleep(0.5)
    print("Initialization of device")
    print("Initializing SPI communication")
    # SPI_Init()
    print("SPI Initialize Done!")


def Slave_config():
    print("Configuring Slave Device")
    # SPI_WriteG(0x8A07F610)                  # FRMCTL
    sleep(0.1)
    # SPI_WriteG(0x85000004)                  # CMREFCTL
    sleep(0.1)
    # SPI_WriteG(0x81F800DE)                  # ECGCTL
    sleep(0.1)
    # SPI_WriteG(0x1F000000)                  # OPSTAT
    sleep(0.1)
    # OPSTAT_SLAVE = SPI_ReadG(0x00000000)    # Read OPSTAT Reg and check PLL Lock
    # print("OPSTAT SLAVE", OPSTAT_SLAVE)


def master_configuration():
    print("------------------------")
    print("Configuring Master device")
    # SPI_Write(0x8A079600)       # FRMCTL
    sleep(0.1)
    # SPI_Write(0x83000001)       # RESPCTL
    sleep(0.1)
    # SPI_Write(0x85E0000B)       # CMREFCTL
    sleep(0.1)
    # SPI_Write(0x81F804BA)       # ECGCTL
    sleep(0.1)
    # SPI_Write(0x1F000000)       # OPSTATE
    sleep(0.1)
    # OPSTAT_MASTER = SPI_Read(0x00000000)    # Read OPSTAT
    # print("OPSTAT MASTER",OPSTAT_MASTER)
    sleep(0.1)

    # SPI_Write(0x81F804BE)       # ECGCTL
    sleep(0.1)
    # SPI_Write(0x40000000)       # FRAMES Master
    sleep(0.1)

    # SPI_WriteG(0x40000000)      # FRAMES Slave
    # slave_frame = SPI_ReadG(0x00000000)
    # print("FRAME DATA : {}".format(slave_frame))


def ecgData(array_data=[0x00, 0x00, 0x00, 0x00]):
    byte1 = array_data[1] << 16
    byte2 = array_data[2] << 8
    byte3 = array_data[3] << 0
    original_data = byte3 | byte2 | byte1
    return original_data


global in_q
in_q = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


def read_adas1000():
    global in_q
    while True:
        if True:
            try:
                temp_data = np.array([])
                for master in range(9):
                    master_rx = [randint(0, 5), randint(0, 1 + master ** 2), randint(0, 1 + master ** 2),
                                 randint(0, 1 + master ** 2)]  # SPI_Read()
                    if master_rx[0] >= 0:
                        master_rx = voltage(ecgData(master_rx))
                        temp_data = np.append(temp_data, master_rx)
                for slave in range(7):
                    slave_rx = [randint(25, 50 + slave ** 2), randint(25, 50 + slave ** 2),
                                randint(25, 50 + slave ** 2), randint(25, 50 + slave ** 2)]  # SPI_ReadG()
                    if slave_rx[0] >= 0:
                        slave_rx = voltage(ecgData(slave_rx))
                        temp_data = np.append(temp_data, slave_rx)
                in_q = np.append(in_q, [temp_data], axis=0)
                if in_q.shape[0] >= 1700:
                    in_q = np.delete(in_q, [i for i in range(2)], axis=0)
                else:
                    pass
            except KeyboardInterrupt:
                break

    pass


# -------------------------------------------------


x = 400


def plot_ecg():
    global in_q

    class MainWindow(QtGui.QMainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent)
            self.resize(800, 500)
            self.setWindowTitle("garph of given value")
            self.login_widget = pg.PlotWidget(self)
            self.login_widget.setBackground("#104C91")
            self.login_widget.setGeometry(QtCore.QRect(20, 30, 750, 300))
            self.style = "*{border: 2px solid '#BC006C';" + "border-radius: 10px;" + "background: #293250;"+"font-size: 15px;" + "color: '#6DD47E';" +"padding: 5px 0;" + "margin: 2px 2px}" + "*:hover{background: #BC006C}"

            self.button = QtGui.QPushButton('Start', self)
            self.button.setStyleSheet(self.style)
            self.button.move(30, 350)
            self.button.clicked.connect(self.cur1)

            self.button1 = QtGui.QPushButton('LEAD1', self)
            self.button1.setStyleSheet(self.style)
            self.button1.move(130, 350)
            self.button1.clicked.connect(self.cur1)
            self.min_value = 0
            self.max_value = 800

            self.button2 = QtGui.QPushButton('LEAD2', self)
            self.button2.setStyleSheet(self.style)
            self.button2.move(230, 350)
            self.button2.clicked.connect(self.cur2)

            self.button3 = QtGui.QPushButton('LEAD3', self)
            self.button3.setStyleSheet(self.style)
            self.button3.move(330, 350)
            self.button3.clicked.connect(self.cur3)

            self.button4 = QtGui.QPushButton('V1', self)
            self.button4.setStyleSheet(self.style)
            self.button4.move(430, 350)
            self.button4.clicked.connect(self.cur4)

            self.button5 = QtGui.QPushButton('V2', self)
            self.button5.setStyleSheet(self.style)
            self.button5.move(530, 350)
            self.button5.clicked.connect(self.cur5)

            self.button6 = QtGui.QPushButton('V3', self)
            self.button6.setStyleSheet(self.style)
            self.button6.move(630, 350)
            self.button6.clicked.connect(self.cur6)

            self.button7 = QtGui.QPushButton('V4', self)
            self.button7.setStyleSheet(self.style)
            self.button7.move(130, 400)
            self.button7.clicked.connect(self.cur7)

            self.button8 = QtGui.QPushButton('V5', self)
            self.button8.setStyleSheet(self.style)
            self.button8.move(230, 400)
            self.button8.clicked.connect(self.cur8)

            self.button9 = QtGui.QPushButton('V6', self)
            self.button9.setStyleSheet(self.style)
            self.button9.move(330, 400)
            self.button9.clicked.connect(self.cur9)

            self.button10 = QtGui.QPushButton('RESPM', self)
            self.button10.setStyleSheet(self.style)
            self.button10.move(430, 400)
            self.button10.clicked.connect(self.cur10)

            self.button11 = QtGui.QPushButton('STOP', self)
            self.button11.setStyleSheet(self.style)
            self.button11.move(30, 400)
            self.button11.clicked.connect(self.cur11)

            self.button12 = QtGui.QPushButton('Exit', self)
            self.button12.setStyleSheet(self.style)
            self.button12.move(530, 400)
            self.button12.clicked.connect(self.cur12)

            self.button13 = QtGui.QPushButton('Save', self)
            self.button13.setStyleSheet(self.style)
            self.button13.move(630, 400)
            self.button13.clicked.connect(self.save)


        def cur1(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data1)
            self.timer.start(1)

        def update_data1(self):
            if in_q.shape[0] >= self.max_value:
                self.data = in_q[self.min_value:self.max_value, 1]
            else:
                self.data = self.data
            self.curve.setData(self.data)
            print("LA")

        def cur2(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data2)
            self.timer.start(1)

        def update_data2(self):
            if in_q.shape[0] >= self.max_value:
                self.data = in_q[self.min_value:self.max_value, 2]
            else:
                self.data = self.data
            self.curve.setData(self.data)
            print("Lead 2")

        def cur3(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data3)
            self.timer.start(1)

        def update_data3(self):
            if in_q.shape[0] >= self.max_value:
                self.data = in_q[self.min_value:self.max_value, 3]
            else:
                self.data = self.data
            self.curve.setData(self.data)
            print("Lead 3")

        def cur4(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data4)
            self.timer.start(1)

        def update_data4(self):
            if in_q.shape[0] >= self.max_value:
                self.data = in_q[self.min_value:self.max_value, 4]
            else:
                self.data = self.data
            self.curve.setData(self.data)
            print("V1")

        def cur5(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data5)
            self.timer.start(1)

        def update_data5(self):
            if in_q.shape[0] >= self.max_value:
                self.data = in_q[self.min_value:self.max_value, 5]
            else:
                self.data = self.data
            self.curve.setData(self.data)
            print("V2")

        def cur6(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data6)
            self.timer.start(1)

        def update_data6(self):
            if in_q.shape[0] >= self.max_value:
                self.data = in_q[self.min_value:self.max_value, 6]
            else:
                self.data = self.data
            self.curve.setData(self.data)
            print("V3")

        def cur7(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data7)
            self.timer.start(1)

        def update_data7(self):
            if in_q.shape[0] >= self.max_value:
                self.data = in_q[self.min_value:self.max_value, 7]
            else:
                self.data = self.data
            self.curve.setData(self.data)
            print("V4")

        def cur8(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data8)
            self.timer.start(1)

        def update_data8(self):
            if in_q.shape[0] >= self.max_value:
                self.data = in_q[self.min_value:self.max_value, 8]
            else:
                self.data = self.data
            self.curve.setData(self.data)
            print("V5")

        def cur9(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data9)
            self.timer.start(1)

        def update_data9(self):
            if in_q.shape[0] >= self.max_value:
                self.data = in_q[self.min_value:self.max_value, 9]
            else:
                self.data = self.data
            self.curve.setData(self.data)
            print("V6")

        def cur10(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data10)
            self.timer.start(1)

        def update_data10(self):
            if in_q.shape[0] >= self.max_value:
                self.data = in_q[self.min_value:self.max_value, 10]
            else:
                self.data = self.data
            self.curve.setData(self.data)
            print("RESPM")

        def cur11(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data11)
            self.timer.start(1)


        def update_data11(self):
            self.curve.setData(self.data)

        def cur12(self):
            print("Resetting")
            # reset_device()
            print("slave Configuration")
            # Slave_config()
            print("master Config")
            # master_configuration()

            pg.QtCore.QTimer().timeout()
            sys.exit("Bye")

        def save(self):
            print("Data Saved")

    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    # q = Queue()
    print("Resetting")
    # reset_device()
    print("slave Configuration")
    Slave_config()
    print("master Config")
    master_configuration()
    q = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    t1 = threading.Thread(target=read_adas1000)
    t2 = threading.Thread(target=plot_ecg)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
