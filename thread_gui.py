
'''
Description: Read One Channel at a time, run> python thread_gui.py 3
Status: Working
@Nitish Sharma
'''

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
from communicationGang import *
from time import sleep
from multiprocessing import Queue
import threading
import numpy as np
import sys
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
        ecg = ((4*1.8*(-(16777216-ADCDecimal))/1.4)/(16777215))
    else:
        ecg = ((4*1.8*ADCDecimal)/1.4)/(16777215)
    return ecg


def reseting():
    print("Resetting Device..")
    sleep(0.5)
    reset_device()
    print("Device Resetted!")
    sleep(0.5)
    print("Initialization of device")
    print("Initializing SPI communication")
    SPI_Init()
    print("SPI Initialize Done!")


def Slave_config():
    print("Configuring Slave Device")
    SPI_WriteG(0x8A07F610)                  # FRMCTL
    sleep(0.1)
    SPI_WriteG(0x85000004)                  # CMREFCTL
    sleep(0.1)
    SPI_WriteG(0x81F800DE)                  # ECGCTL
    sleep(0.1)
    SPI_WriteG(0x1F000000)                  # OPSTAT
    sleep(0.1)
    # Read OPSTAT Reg and check PLL Lock
    OPSTAT_SLAVE = SPI_ReadG(0x00000000)
    print("OPSTAT SLAVE", OPSTAT_SLAVE)


def master_configuration():
    print("------------------------")
    print("Configuring Master device")
    SPI_Write(0x8A079600)       # FRMCTL
    sleep(0.1)
    SPI_Write(0x83000001)       # RESPCTL
    sleep(0.1)
    SPI_Write(0x85E0000B)       # CMREFCTL
    sleep(0.1)
    SPI_Write(0x81F804BA)       # ECGCTL
    sleep(0.1)
    SPI_Write(0x1F000000)       # OPSTATE
    sleep(0.1)
    OPSTAT_MASTER = SPI_Read(0x00000000)    # Read OPSTAT
    print("OPSTAT MASTER", OPSTAT_MASTER)
    sleep(0.1)

    SPI_Write(0x81F804BE)       # ECGCTL
    sleep(0.1)
    SPI_Write(0x40000000)       # FRAMES Master
    sleep(0.1)

    SPI_WriteG(0x40000000)      # FRAMES Slave
    slave_frame = SPI_ReadG(0x00000000)
    print("FRAME DATA : {}".format(slave_frame))


global in_q
in_q = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


def read_adas1000():
    global in_q
    file1 = open("ecg_17.txt", 'w')
    count = 0
    while True:
        if check_DRDY():
            pass
        else:
            try:
                temp_data = np.array([])
                temp_lst = []
                for master in range(9):
                    master_rx = SPI_Read()
                    if master_rx[0] != 128:
                        master_rx = voltage(ecgData(master_rx))
                        temp_data = np.append(temp_data, master_rx)
                        temp_lst.append(master_rx)
                for slave in range(7):
                    slave_rx = SPI_ReadG()
                    if slave_rx[0] != 128:
                        slave_rx = voltage(ecgData(slave_rx))
                        temp_data = np.append(temp_data, slave_rx)
                        temp_lst.append(slave_rx)
                in_q = np.append(in_q, [temp_data], axis=0)
                file1.write(str(temp_lst))
                file1.write("\n")

                if in_q.shape[0] >= 1700:
                    in_q = np.delete(in_q, [i for i in range(2)], axis=0)
                else:
                    pass
            except KeyboardInterrupt:
                file1.close()
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
            self.login_widget.setGeometry(QtCore.QRect(20, 30, 750, 300))

            self.button = QtGui.QPushButton('Start', self)
            self.button.move(30, 350)
            self.button.clicked.connect(self.cur1)

            self.button1 = QtGui.QPushButton('LEAD1', self)
            self.button1.move(130, 350)
            self.button1.clicked.connect(self.cur1)
            self.min_value = 0
            self.max_value = 800

            self.button11 = QtGui.QPushButton('STOP', self)
            self.button11.move(30, 400)
            self.button11.clicked.connect(self.cur11)

            self.button12 = QtGui.QPushButton('RESET', self)
            self.button12.move(530, 400)
            self.button12.clicked.connect(self.cur12)

        def cur1(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data1)
            self.timer.start(1)

        def update_data1(self):
            if in_q.shape[0] >= self.max_value:
                self.data = in_q[self.min_value:self.max_value, channel]
            else:
                self.data = self.data
            self.curve.setData(self.data)

        def cur11(self):
            self.data = [0] * x
            self.curve = self.login_widget.plot(self.data, clear=True)
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.update_data11)
            self.timer.start(1)

        def update_data11(self):
            value = 0
            self.data[:-1] = self.data[1:]
            self.data[-1] = value
            self.curve.setData(self.data)

        def cur12(self):
            print("Resetting")
            reset_device()
            print("slave Configuration")
            Slave_config()
            print("master Config")
            master_configuration()

    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    print("Resetting")
    reset_device()
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
    print("Done")
