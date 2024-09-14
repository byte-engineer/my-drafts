# test/test0.py

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
import test3
import sys
from os import system

system('cls')

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.UI()

        # attributes
        self.waveform = None
        self.firsthilght = False

    def UI(self):

        self.init_window()

        tabs = QTabWidget()
        tabs.setMovable(True)
        tap = self.generateTab()                  # This is the first tab for generate class
        tabs.addTab(tap, 'Generate')
        
        layout = QVBoxLayout()
        layout.addWidget(tabs)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


        
    def generateTab(self):

        tap = QWidget()
        tab_layout = QGridLayout()

        # Compo box to get the type of wave form.
        combo_label = QLabel('Choose WaveForm:  ')
        self.combo = QComboBox()
        self.combo.addItem('-- Choose --')
        self.combo.addItems(['sin', 'square', 'trianglar'])
        self.combo.highlighted.connect(self.combo_highlighted)

        freq_label = QLabel('Freqency:  ')
        self.freq_spin = QSpinBox()
        self.freq_spin.setRange(1, 1000000)
        self.freq_spin.setValue(1)
        self.freq_spin.setSuffix(' Hz')

        # Buttons
        generate_btn = QPushButton('Generate')
        generate_btn.clicked.connect(self.generate)

        save_btn = QPushButton('Save')
        freqs_btn = QPushButton('Frequencies')

        # Grid layout stuff
        tab_layout.addWidget(combo_label, 0, 0)
        tab_layout.addWidget(self.combo, 0, 1)
        tab_layout.addWidget(self.combo, 0, 1)

        tab_layout.addWidget(freq_label, 1, 0)
        tab_layout.addWidget(self.freq_spin, 1, 1)

        tab_layout.addWidget(generate_btn, 3, 0, 1, 0)
        tab_layout.addWidget(save_btn, 7, 0)
        tab_layout.addWidget(freqs_btn, 7, 1)

        tap.setLayout(tab_layout)
        return tap



    def init_window(self):
        self.setWindowTitle('Waves')
        self.bar = self.menuBar()


    def combo_highlighted(self, index):
        if not self.firsthilght:
            self.firsthilght = True
            self.combo.removeItem(0)


    def generate(self):

        if self.combo.currentText() == 'sin':
            gnrt = test3.generate(44100)
            self.waveform =  gnrt.sin(1, self.freq_spin.value())

         

def window():


    app = QApplication(sys.argv)

    win = Main()
    win.show()
    sys.exit(app.exec())

window()