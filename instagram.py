import sys
from PyQt5 import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


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
        for _ in range(16):
            self.btn = QPushButton(str(name), self)
            self.btn.setFont(QtGui.QFont('Times', int(3 * c)))
            shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=0, yOffset=3)
            self.btn.setGraphicsEffect(shadow)
            self.btn.setStyleSheet('''
                     QPushButton{
                         color: white;
                         background-color: pink;
                         border-radius: 5px;
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
        for row in range(int(2*c), int(b), int((2*a)+c)):#int((2*a)-d)
            for col in range(int(2*c), int(l), int((4*a)-d)):
                self.button[index].setGeometry(col,row,int((3*a)+(2*c)),int((2*a)-(2*c)))
                index += 1

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())