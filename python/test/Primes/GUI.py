# TEST/Primes/GUI.py

from PyQt5 import QtWidgets
import sys  
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMainWindow, QShortcut
from PyQt5.QtGui import QPalette, QColor, QKeySequence
import primes

style = 'TEST/Primes/style.qss'

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.UI()                  # python

    def UI(self):
        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.lbl0 = QtWidgets.QLabel('Is Prime?')
        self.lbl0.setObjectName('lbl0')

        # button.
        self.button = QPushButton('(o_o)')
        self.button.clicked.connect(self.Action)
        # self.setShortcut(QKeySequence('Enter'))

        self.short = QShortcut(QKeySequence('Enter'), self)
        self.short.activated.connect(self.button.click)

        # theme button.
        self.theme = QPushButton('theme')
        self.theme.clicked.connect(self.changetheme)
        self.theme.setObjectName('theme')


        # Numbers input
        self.entry = QtWidgets.QLineEdit()
        self.entry.setPlaceholderText('Number Please')
        
        self.result = QtWidgets.QLabel()

        self.box = QVBoxLayout()
        self.box.addWidget(self.lbl0)
        self.box.addWidget(self.entry)
        self.box.addWidget(self.result)
        self.box.addWidget(self.button)
        self.box.addWidget(self.theme)

        self.central.setLayout(self.box)

    def Action(self):
        try:
            answer = 'Yes' if primes.Is_prime(int(self.entry.text())) else 'No'
        except:
            answer = '??!'

        self.result.setText(answer)

    def changetheme(self):
        style = 'TEST/Primes/style0.qss'


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = Main()

    with open(style, 'r') as file:
        win.setStyleSheet(file.read())

    win.show()
    sys.exit(app.exec_())

window()