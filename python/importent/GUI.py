from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QFileDialog, QApplication, QFormLayout, QMessageBox)
from PyQt5.QtCore import Qt
import sys
import numpy as np
import soundfile as sf

# Import classes from waves.py
from waves import generate, Noise, analysis  # Ensure waves.py is in the same directory

class AudioGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize classes
        self.sample_rate = 44100
        self.gen = generate(self.sample_rate)
        self.nis = Noise(self.sample_rate)
        self.anls = analysis(self.sample_rate)

        # Set default wave parameters
        self.wave_params = {}

        # Set up GUI
        self.init_ui()
        self.load_stylesheet('dark')  # Load default theme
        self.setFixedSize(400, 300)  # Initial fixed size

    def init_ui(self):
        # Layouts
        self.main_layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.button_layout = QHBoxLayout()

        # Widgets
        self.wave_type_combo = QComboBox()
        self.wave_type_combo.addItems(['Sine', 'Square', 'Triangle', 'Noise', 'Normal Noise', 'Cosine', 'AM (Amplitude Modulation)', 'FM (Frequency Modulation)'])
        self.wave_type_combo.currentIndexChanged.connect(self.update_wave_params)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(['Dark Theme', 'Colorful Theme'])
        self.theme_combo.currentIndexChanged.connect(self.change_theme)

        # Inputs and labels
        self.time_input = QLineEdit()
        self.frequency_input = QLineEdit()
        self.amplitude_input = QLineEdit()
        self.carrier_freq_input = QLineEdit()
        self.modulation_index_input = QLineEdit()
        self.scale_input = QLineEdit()

        # Labels
        self.time_label = QLabel('Time (seconds):')
        self.frequency_label = QLabel('Frequency (Hz):')
        self.amplitude_label = QLabel('Amplitude:')
        self.carrier_freq_label = QLabel('Carrier Frequency (Hz):')
        self.modulation_index_label = QLabel('Modulation Index:')
        self.scale_label = QLabel('Scale:')
        self.filepath_label = QLabel('Save File Path: ')

        # Buttons
        self.generate_btn = QPushButton('Generate Wave')
        self.save_btn = QPushButton('Save Audio')
        self.fft_btn = QPushButton('Show FFT')

        # Connect buttons to functions
        self.generate_btn.clicked.connect(self.generate_wave)
        self.save_btn.clicked.connect(self.save_audio)
        self.fft_btn.clicked.connect(self.show_fft)

        # Add widgets to layout
        self.form_layout.addRow('Wave Type:', self.wave_type_combo)
        self.form_layout.addRow('Theme:', self.theme_combo)
        self.form_layout.addRow(self.time_label, self.time_input)
        self.form_layout.addRow(self.frequency_label, self.frequency_input)
        self.form_layout.addRow(self.amplitude_label, self.amplitude_input)
        self.form_layout.addRow(self.carrier_freq_label, self.carrier_freq_input)
        self.form_layout.addRow(self.modulation_index_label, self.modulation_index_input)
        self.form_layout.addRow(self.scale_label, self.scale_input)
        self.form_layout.addWidget(self.filepath_label)

        self.button_layout.addWidget(self.generate_btn)
        self.button_layout.addWidget(self.save_btn)
        self.button_layout.addWidget(self.fft_btn)

        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)
        self.setWindowTitle('Audio Wave Generator')
        self.update_wave_params()  # Update parameters based on initial selection
        self.show()

    def load_stylesheet(self, theme):
        """Load QSS file and apply it to the application."""
        if theme == 'dark':
            stylesheet = """
                QWidget {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                QPushButton {
                    background-color: #3c3f41;
                    border: 1px solid #555;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #4c4f51;
                }
                QLineEdit {
                    background-color: #3c3f41;
                    border: 1px solid #555;
                    padding: 5px;
                    color: #ffffff;
                }
                QLabel {
                    color: #ffffff;
                }
                QComboBox {
                    background-color: #3c3f41;
                    border: 1px solid #555;
                    padding: 5px;
                    color: #ffffff;
                }
            """
        elif theme == 'colorful':
            stylesheet = """
                QWidget {
                    background-color: #ffffff;
                    color: #000000;
                }
                QPushButton {
                    background-color: #f0f0f0;
                    border: 1px solid #333;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
                QLineEdit {
                    background-color: #f0f0f0;
                    border: 1px solid #333;
                    padding: 5px;
                    color: #000000;
                }
                QLabel {
                    color: #000000;
                }
                QComboBox {
                    background-color: #f0f0f0;
                    border: 1px solid #333;
                    padding: 5px;
                    color: #000000;
                }
            """
        self.setStyleSheet(stylesheet)

    def change_theme(self):
        """Change the application theme based on combo box selection."""
        selected_theme = self.theme_combo.currentText()
        if selected_theme == 'Dark Theme':
            self.load_stylesheet('dark')
        elif selected_theme == 'Colorful Theme':
            self.load_stylesheet('colorful')

    def update_wave_params(self):
        """Update the visible input fields based on the selected wave type."""
        wave_type = self.wave_type_combo.currentText()

        # Hide all fields first
        self.time_label.hide()
        self.time_input.hide()
        self.frequency_label.hide()
        self.frequency_input.hide()
        self.amplitude_label.hide()
        self.amplitude_input.hide()
        self.carrier_freq_label.hide()
        self.carrier_freq_input.hide()
        self.modulation_index_label.hide()
        self.modulation_index_input.hide()
        self.scale_label.hide()
        self.scale_input.hide()

        # Show necessary fields for each wave type
        self.time_label.show()
        self.time_input.show()
        if wave_type in ['Sine', 'Square', 'Triangle', 'Cosine']:
            self.frequency_label.show()
            self.frequency_input.show()
            self.scale_label.show()
            self.scale_input.show()
            self.setFixedSize(400, 300)
        elif wave_type == 'Noise':
            self.frequency_label.show()  # Main frequency
            self.frequency_input.show()
            self.amplitude_label.show()
            self.amplitude_input.show()
            self.scale_label.show()
            self.scale_input.show()
            self.setFixedSize(400, 350)
        elif wave_type == 'Normal Noise':
            self.scale_label.show()
            self.scale_input.show()
            self.setFixedSize(400, 250)
        elif wave_type == 'AM (Amplitude Modulation)':
            self.frequency_label.show()  # Message frequency
            self.frequency_input.show()
            self.carrier_freq_label.show()
            self.carrier_freq_input.show()
            self.scale_label.show()
            self.scale_input.show()
            self.setFixedSize(400, 350)
        elif wave_type == 'FM (Frequency Modulation)':
            self.frequency_label.show()  # Message frequency
            self.frequency_input.show()
            self.carrier_freq_label.show()
            self.carrier_freq_input.show()
            self.modulation_index_label.show()
            self.modulation_index_input.show()
            self.scale_label.show()
            self.scale_input.show()
            self.setFixedSize(400, 400)

    def generate_wave(self):
        try:
            wave_type = self.wave_type_combo.currentText()
            time = float(self.time_input.text() or 0)
            frequency = float(self.frequency_input.text() or 0)
            amplitude = float(self.amplitude_input.text() or 1)
            carrier_freq = float(self.carrier_freq_input.text() or 0)
            modulation_index = float(self.modulation_index_input.text() or 0)
            scale = float(self.scale_input.text() or 1)

            if wave_type == 'Sine':
                self.wave = self.gen.sin(time, frequency, scale=scale)
            elif wave_type == 'Square':
                self.wave = self.gen.square(time, frequency, scale=scale)
            elif wave_type == 'Triangle':
                self.wave = self.gen.triangle(time, frequency, scale=scale)
            elif wave_type == 'Cosine':
                self.wave = self.gen.cos(time, frequency, scale=scale)
            elif wave_type == 'Noise':
                self.wave = self.nis.noise_deform(time, frequency, amplitude=amplitude, factor=scale)
            elif wave_type == 'Normal Noise':
                self.wave = self.nis.normal(time, scale=scale)
            elif wave_type == 'AM (Amplitude Modulation)':
                self.wave = self.gen.AM(self.gen.sin(time, frequency), carrier_freq, scale=scale)
            elif wave_type == 'FM (Frequency Modulation)':
                self.wave = self.gen.FM(self.gen.sin(time, frequency), carrier_freq, modulation_index, scale=scale)
            else:
                self.show_error("Unknown wave type selected!")
        except ValueError as e:
            self.show_error(f"Invalid input: {e}")

    def save_audio(self):
        if hasattr(self, 'wave'):
            filepath, _ = QFileDialog.getSaveFileName(self, 'Save Audio File', '', 'WAV Files (*.wav)')
            if filepath:
                sf.write(filepath, self.wave, self.sample_rate)
                self.filepath_label.setText(f'Saved to: {filepath}')
        else:
            self.show_error("No wave generated to save!")

    def show_fft(self):
        if hasattr(self, 'wave'):
            self.anls.show_fft(self.wave)
        else:
            self.show_error("Generate a wave first!")

    def show_error(self, message):
        """Show error message in a floating message box."""
        error_msg = QMessageBox(self)
        error_msg.setIcon(QMessageBox.Critical)
        error_msg.setText(message)
        error_msg.setWindowTitle('Error')
        error_msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AudioGeneratorApp()
    sys.exit(app.exec_())

