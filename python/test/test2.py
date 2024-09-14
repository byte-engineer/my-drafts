# Tabs

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtMultimedia




class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.UI()


    def UI(self):

        layout = QVBoxLayout()
# ---------------------------------------------------------------------

        btn = QPushButton("Don't click me", self)
        btn.setCheckable(True)

        btn.clicked.connect(self.play)

        self.player = QtMultimedia.QMediaPlayer()

# ---------------------------------------------------------------------

        layout.addWidget(btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def play(self):
        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile('Results/Audio/part_Quran.wav')))
        self.player.play()

app = QApplication([])

win = Main()
win.show()

app.exec()