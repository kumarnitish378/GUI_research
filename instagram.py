import sys
from PyQt5 import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from functools import partial


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        l = 800
        b = 450
        a = l / 16
        c = l / 80
        d = c / 2
        self.resize(l, b)
        self.button = []
        name = 1
        self.st = (""
                   "QPushButton{"
                   "color: white;"
                   "background-color: #050065;"
                   "border-radius: 40px;"
                   "}"
                   "QPushButton:hover {"
                   "background-color: black;"
                   "color: black")

        for _ in range(16):
            self.btn = QPushButton(str(name), self)
            self.btn.setFont(QtGui.QFont('Times', int(3 * c)))
            shadow = QGraphicsDropShadowEffect(blurRadius=2, xOffset=0, yOffset=3)
            self.btn.setGraphicsEffect(shadow)
            self.btn.setStyleSheet('''
                     QPushButton{
                         color: white;
                         background-color: #787878;
                         border-radius: 5px;
                         margin: 5px
                     }  
                     QPushButton:hover {
                         background-color: white;
                         color: black;
                     }
                 ''')

            self.button.append(self.btn)
            self.btn.show()
            name += 1

        index = 0
        for row in range(int(2 * c), int(b), int((2 * a) + c)):  # int((2*a)-d)
            for col in range(int(2 * c), int(l), int((4 * a) - d)):
                self.button[index].setGeometry(col, row, int((3 * a) + (2 * c)), int((2 * a) - (2 * c)))
                index += 1

        self.button[0].clicked.connect(self.change0)
        self.button[1].clicked.connect(self.change1)
        self.button[2].clicked.connect(self.change2)
        self.button[3].clicked.connect(self.change3)
        self.button[4].clicked.connect(self.change4)
        self.button[5].clicked.connect(self.change5)
        self.button[6].clicked.connect(self.change6)
        self.button[7].clicked.connect(self.change7)
        self.button[8].clicked.connect(self.change8)
        self.button[9].clicked.connect(self.change9)
        self.button[10].clicked.connect(self.change10)
        self.button[11].clicked.connect(self.change11)
        self.button[12].clicked.connect(self.change12)
        self.button[13].clicked.connect(self.change13)
        self.button[14].clicked.connect(self.change14)
        self.button[15].clicked.connect(self.change15)

    def change0(self):
        self.button[0].setStyleSheet(self.st)

    def change1(self):
        self.button[1].setStyleSheet(self.st)

    def change2(self):
        self.button[2].setStyleSheet(self.st)

    def change3(self):
        self.button[3].setStyleSheet(self.st)

    def change4(self):
        self.button[4].setStyleSheet(self.st)

    def change5(self):
        self.button[5].setStyleSheet(self.st)

    def change6(self):
        self.button[6].setStyleSheet(self.st)

    def change7(self):
        self.button[7].setStyleSheet(self.st)

    def change8(self):
        self.button[8].setStyleSheet(self.st)

    def change9(self):
        self.button[9].setStyleSheet(self.st)

    def change10(self):
        self.button[10].setStyleSheet(self.st)

    def change11(self):
        self.button[11].setStyleSheet(self.st)

    def change12(self):
        self.button[12].setStyleSheet(self.st)

    def change13(self):
        self.button[13].setStyleSheet(self.st)

    def change14(self):
        self.button[14].setStyleSheet(self.st)

    def change15(self):
        self.button[15].setStyleSheet(self.st)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
