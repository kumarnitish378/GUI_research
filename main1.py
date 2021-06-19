# INSTALL PyQt5 WITH:
# 1. ANACONDA:
# conda install -c anaconda pyqt
# 2. PIP:
# pip install PyQt5
# 3. LINUX:
# sudo apt-get install python3-pyqt5

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

widgets = {"logo": [],
           "button": [],
           "score": [],
           "qustion": [],
           "answer1": [],
           "answer2": [],
           "answer3": [],
           "answer4": []
           }

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Hello World")
window.setFixedWidth(1000)
window.move(1700, 100)
window.setStyleSheet("background: #161219")

grid = QGridLayout()


def clear_widget():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


def show_frame1():
    clear_widget()
    frame()


def start_game():
    clear_widget()
    frame2()


def create_button(answer, l_margin, r_margin):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "margin-left: " + str(l_margin) + "px;" +
        "margin-right: " + str(r_margin) + "px;" +
        "border-radius: 25px;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 25px 0;" +
        "margin: 10px 20px}"
        "*:hover{background: #BC006C;"+
        "transition-delay: 10s;"+
        "border-radius: 30px;}"
    )
    button.clicked.connect(show_frame1)
    return button


# Button widget
def frame():
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("magin-top: 100px;")
    widgets["logo"].append(logo)

    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet("*{border: 4px solid '#BC006C';" +
                         "border-radius: 15px;" +
                         "font-size: 25px;" +
                         "color: 'white';" +
                         "padding: 15px 0;" +
                         "margin: 10px 20px}"
                         "*:hover{background: #BC006C}")
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)


def frame2():
    score = QLabel("78")
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet(
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 20px 20px 20px;" +
        "border: 1px solid '#64A314';" +
        "background: #64A314;"
        "margin: 20px 200px;" +
        "border-radius: 10px;"
    )
    widgets["score"].append(score)

    qustion = QLabel("Q1: Who is the prime minister of India?")
    qustion.setAlignment(QtCore.Qt.AlignLeft)
    qustion.setWordWrap(True)
    qustion.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 75px;"
    )
    widgets["qustion"].append(qustion)

    btn1 = create_button("A. Narendra Modi", 85, 5)
    btn2 = create_button("B. Rahul Gandhi",5, 85)
    btn3 = create_button("C. Arvind Kejriwal", 85, 5)
    btn4 = create_button("D. Amit sah",5, 85)

    widgets["answer1"].append(btn1)
    widgets["answer2"].append(btn2)
    widgets["answer3"].append(btn3)
    widgets["answer4"].append(btn4)

    image = QPixmap("logo_bottom.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("magin-top: 75px; margin-bottom: 30px;")
    widgets["logo"].append(logo)

    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["qustion"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["answer3"][-1], 3, 0)
    grid.addWidget(widgets["answer4"][-1], 3, 1)
    grid.addWidget(widgets["logo"][-1], 4, 0)


frame()
# frame2()

window.setLayout(grid)
window.show()
sys.exit(app.exec())
