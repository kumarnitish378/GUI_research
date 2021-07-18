import random
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget,QGridLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from time import sleep, time

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Live Graph")
window.setGeometry(480, 1000, 0, 0)
window.setStyleSheet("background: red")
grid = QGridLayout()


def create_label(text):
    name = QLabel()
    name.setText(text)
    name.setAlignment(QtCore.Qt.AlignCenter)
    name.setStyleSheet("color: white;"
                       "background: black;"
                       "padding: 20px 20px;"
                       "margin: 2px;"
                       "font-size: 80px;" 
                       "border: 5px solid 'blue';"
                       "border-radius: 25px;")

    return name

def create_button(name):
    button = QPushButton()
    button = QPushButton(name)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
                *{
                    border: 4px solid '#BC006C';
                    border-radius: 45px;
                    font-size: 35px;
                    color: 'white';
                    padding: 25px 0;
                    margin: 10px 10px;
                    background: 'green';
                }
                *:hover{
                    background: '#BC006C';
                }
                '''
    )
    return button

global count
count = 0
def update():
    count = 0
    for i in range(1, 16):
        QApplication.processEvents()
        p1.setText("BP: " + str(i))
        sleep(1)
    p2.setText("SPO2: \n"+ str(random.randint(20,50)))
    p3.setText("QR: "+str(random.randint(20, 50)))
    p4.setText("PR: "+str(random.randint(20, 50)))

def reset():
    count = 0
    update()

p1 = create_label("BP: 100/120")
p2 = create_label("SPO2: 67")
p3 = create_label("QR: 120")
p4 = create_label("PR: 120")

button = create_button("Start")
button1 = create_button("Reset")
grid.addWidget(button, 2, 0)
grid.addWidget(button1, 2,1)
grid.addWidget(p1, 0, 0)
grid.addWidget(p2, 0, 1)
grid.addWidget(p3, 1, 0)
grid.addWidget(p4, 1, 1)
button.clicked.connect(update)
button1.clicked.connect(reset)



window.setLayout(grid)
window.show()
count = 1
sys.exit(app.exec())
