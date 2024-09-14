from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWebEngineWidgets



class Main(QMainWindow):

    def __init__(self):

        super().__init__()
        

        layout = QVBoxLayout()


        layout.addWidget('Dont tell me what to do')

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication([])

win = Main()
win.show()

app.exec()