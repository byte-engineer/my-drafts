# Draft/Librarys/QT.py
import os
os.system('cls')

#|> QtDesigner
# * QtDesigner interface is very simple and depends on drag and drop.
# * We can Convert `.iu` files to python files by this commend `pyuic5 -x app.ui -o app.py`

#|> Tips:
#  * start with child elements then the parent.


# ___________________________________________________________________
# |# | Name        | Description                                    |
# |--|-------------|------------------------------------------------|
# |1 | QtCore      | Core non-GUI classes used by other modules     |
# |5 | QtWidgets   | Classes for creating classic desktop-style UIs |
# |2 | QtGui       | Graphical user interface components            |
# |3 | QtMultimedia|  Classes for low-level multimedia programming  |
# |4 | QtOpenGL    | OpenGL support classes                         |


# Import The modules.
import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
from PyQt5 import QtWidgets, QtGui, QtCore, QtMultimedia
import PyQt5.QtWebEngineWidgets               # If you want it you have to install it individually.
from PyQt5.QtCore import Qt
import sys                                    # We should import also this python built-In Module.


# Start coding.
class Qwidgets(QtWidgets.QMainWindow):                               # We have to subclass 'QMainWindow' in Main window class.

    def __init__(self):
        super().__init__()                                           # initialize the 'QMainWindow' class.



    def QMainWindow(self):
        self.setGeometry(100, 100, 300, 300)                         # Set The dimentions of The main window. | setGeometry(xpos, ypos, Width, Height)
        self.resize(500, 400)                                        # We can use it instead of setGeometry method.
        self.move(100, 100)                                          # place the window in specefic co-ordinates.
        self.setFixedSize(300, 300)                                  # Set Fixed Size. setFixedSize(Width, Height)
        self.setMinimumSize(QtCore.QSize(100, 100))                  # Minimam Size.
        self.setMaximumSize(QtCore.QSize(1000, 1000))                # MAximam Size.
        self.setWindowTitle('Window Name')                           # Set window title.
        self.setCentralWidget(QtWidgets.QWidget())                   # Set a widget as a central widget.
        self.setLayout(QtWidgets.QLayout())                          # place QLayout in the window.
        self.setCentralWidget(QtWidgets.QWidget)                     # Set A widget as a Central widget allmost used in layouts.
        self.setWindowIcon(QtGui.QIcon('path/to/icon.png'))          # Set an Icon for the window.
        self.setWindowOpacity(0.95)                                  # Opasite bettween 0 and 1.
        self.setStyleSheet('{background-color: black;}')             # Set stylesheet in QSS (for the elements of the window).
        self.setWindowState(Qt.WindowMinimized)                      # Set Window state {WindowMinimized, WindowMaximized, WindowFullScreen} |> Use '|' to compine.
        self.setMouseTracking(True)                                  # Enable mouse tracking captured in 'mouseMoveEvent' method.
        self.setWindowFlags(Qt.WindowStaysOnTopHint)                 # Set Window Flages {WindowStaysOnTopHint, FramelessWindowHint}         |> Use '|' to compine.
        self.menuBar()                                               # Adds A menu bar to the window. |More later.
        # self.close()                                               # If we want to close the window.



    def Flages(self):
        # Windows types                                              # Type: Qt.WindowType
        Qt.WindowType.Widget                                         # For normal Widgits.
        Qt.WindowType.Window                                         # For normal Wendows.
        Qt.WindowType.CoverWindow                                    # Like fullscreen app Used in games.
        Qt.WindowType.SplashScreen                                   # Used in start-up.
        Qt.WindowType.SubWindow                                      # internal window within a larger window Used with (QMdiArea, QMdiSubWindow) more later.

        # Modifiers                                                  # Not All.
        Qt.WindowType.WindowTransparentForInput                      # The window become transparant for mouse input. 
        Qt.WindowType.FramelessWindowHint                            # Window With out frame.
        Qt.WindowType.CustomizeWindowHint                            # Indecate that the developer want to custamize Window hint.
        Qt.WindowType.WindowTitleHint                                # Add A title bar.
        Qt.WindowType.WindowCloseButtonHint                          # Add Close Button.
        Qt.WindowType.WindowMinimizeButtonHint                       # Add Minimize Button.
        Qt.WindowType.WindowMaximizeButtonHint                       # Add Maximize Button.
        Qt.WindowType.WindowMinMaxButtonsHint                        # Add both Maximize and Minimize Buttons.
        Qt.WindowType.WindowContextHelpButtonHint                    # Add a botton '?' for Help.
        Qt.WindowType.WindowStaysOnTopHint                           # Window Will always stay on top.
        Qt.WindowType.WindowStaysOnBottomHint                        # Window will always stay on bottom
        Qt.WindowType.WindowOverridesSystemGestures                  # Give app ability to handell Gestures.
        # Widgets attributes
        ...


    def QFont(self):
        font = QtGui.QFont('Arial', 16, QtGui.QFont.Bold)            # Used in label.setFont()
        font.setFamily('')                                           # Returns the name of font.
        font.setPointSize(10)                                        # Returns the font size.
        font.setBold()                                               # Returns True if font is bold.
        return font


    def QPixmap(self):
        map = QtGui.QPixmap(r'Results/mos.png')                            # Create an instance and load the image.
        map.scaled(32, 32, aspectMode= Qt.AspectRatioMode.KeepAspectRatio) # Resize the image with Keep aspect ratio. {KeepAspectRatio, KeepAspectRatioByExpanding, IgnoreAspectRatio}



    def QWidget(self):
        widget = QtWidgets.QWidget(self)                             # Main Abctract class for All QtWidgets in PyQt5.
        widget.setParent(self)                                       # Its parent.
        widget.setEnabled(True)                                      # Inable Widget.
        widget.setVisible(True)                                      # Set widget visible.
        widget.setStyleSheet({'color: black;'})                      # Set QSS for the Widget.
        widget.update()                                              # Will repaint the widget again.
        widget.repaint()                                             # Forces the widget to be repainted immediately.
        widget.setGeometry(100, 100, 300, 300)                       # Sets the position and size of the button.
        widget.move(50, 50)                                          # Moves the button to a specified position.
        widget.resize(50, 20)                                        # Resizes the button to the specified dimensions.
        widget.setFocus()                                            # Sets focus to the item.
        widget.setToolTip('This is widget')                          # Set tool tip.



    def QAbstractButton(self):                                       # Applaied for QtPushButton, QCheckBox, QRadioButton
        abcbtn = QtWidgets.QAbstractButton()                         # Create the instance.
        abcbtn.setAutoRepeat(True)                                   # Enable auto-repeat when button is held down
        abcbtn.setAutoRepeatDelay(1000)                              # Delay before the repeat starts (in milliseconds)
        abcbtn.setAutoRepeatInterval(200)                            # Interval between repeats (in milliseconds)
        abcbtn.setWhatsThis('This is button')                        # For help reasones and appares when the user click F1 key.
        abcbtn.setIcon(QtGui.QIcon)                                  # Icon next to the element.
        abcbtn.setIconSize(QtCore.QSize)                             # Set Icon size.



    def QLabel(self):                                                # All QWidget methods Above Can be used for QLabel.
        label = QtWidgets.QLabel('the main text here', self)         # Create a label instance.
        label.setText('the change the text')                         # Used the change the text of the label.
        label.adjustSize()                                           # We need this comend when the set a new longer text.
        label.setObjectName('lbl')                                   # Will help us in QSS Stylesheets.
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)             # Set the alignment {AlignCenter, AlignLeft, AlignRight, AlignJustify}
        label.setFont(self.font())                                   # It's parameter must be an instance from 'QFont'



    def QPushButton(self):                                           # All QWidget and QAbstractButton methods Above Can be used for button.
        button = QtWidgets.QPushButton('click me!', self)            # create pushbutton inctance.  |  QPushButton(QIcon, str, QWidget parent=None)
        button.setShortcut(QtGui.QKeySequence('Return'))             # Set Shortcut for the button.
        button.setDefault(True)                                      # Set the button activated when 'Enter' pressed.
        button.setIcon(QtGui.QIcon)                                  # Icon before text.
        button.setFlat(True)                                         # Remove 3D effects & borders.
        button.setCheckable(True)                                    # Button toggle bettwen True & False.
        button.setChecked(True)                                      # Put Buton in checked state.
        button.toggle()                                              # Toggles the button state between checked and unchecked.
        button.click()                                               # Simulates a button click. triggering button actions programmatically.
        button.animateClick(200)                                     # Simulates a button click with it's animation and hold 200ms.

        button.clicked.connect(self.action)                          # The action method runs then the button clicked.
        button.toggled.connect(self.action)                          # function in this syntax -> toggled(self, checked)
        button.released.connect(self.action)                         # The action method runs then the button released.
        button.pressed.connect(self.action)                          # The action method runs then the button pressed.




    def QLineEdit_QTextEdit(self):                                   # All QWidget and QAbstractButton methods Above Can be used for QLineEdit.
        line = QtWidgets.QLineEdit(self)                             # One line string input.
        text = QtWidgets.QTextEdit(self)                             # Multible lines string input.
        line.text()                                                  # To get the text.
        line.textChanged(self.textchanged)                           # If text changed will call this function function should be in this formate func(parent, text)
        line.setPlaceholderText('QlineEdit')                         # Set a text in the background.
        line.setText('string Input')                                 # Writes a text in QlineEdit.
        line.clear()                                                 # Clear Line edit.
        line.setReadOnly(True)                                       # User can't change the content of the line Edit.
        line.setMaxLength(3)                                         # Set maximum number of characters that allowed.
        line.setEchoMode(QtWidgets.QLineEdit.Normal)                 # Set the Mode default Normal. options {Normal, Password, NoEcho, PasswordEchoOnEdit}
        line.setAlignment(Qt.AlignmentFlag.AlignCenter)              # Set text alignment {AlignCenter, AlignLeft, AlignRight}.
        line.selectAll()                                             # Just select all text inside.
        line.setSelection(0, 5)                                      # Select spesefic characters.  setSelection(start, end)
        line.setCursorPosition(0)                                    # Set cursor in spesefic index.
        line.undo()                                                  # Return to the last state.
        line.redo()                                                  # Do last step again.
        line.clearFocus()                                            # Clear focus and remove the cursor.
        line.setDragEnabled(True)                                    # If inabled it allowed to drage the text from edit line.
        # only for Text
        text.setPlainText("Hello PyQt5!\nGreat lib")                 # Set text in multible lines.
        text.setHtml("<font color='red'><red>Hello PyQt5!</font>")   # Set text as HTML Code.


    def QCheckBox_QRadioButton(self):                                # All QWidget and QAbstractButton methods Above Can be used for QCheckBox.
        radio = QtWidgets.QRadioButton(self)                         # Create a QRadioButton instance.
        checkbox = QtWidgets.QCheckBox(self)                         # Create a QCheckBox instance.
        checkbox.setChecked(True)                                    # Check the box.
        checkbox.toggle()                                            # Toggel between checked and unchecked.
        checkbox.setTristate(False)                                  # If True adds PartiallyChecked state.
        checkbox.setCheckState(Qt.CheckState.Checked)                # Set state {Qt.Checked, Qt.Unchecked, Qt.PartiallyChecked} Type: Qt.CheckState
        checkbox.setText("Check box")                                # set a text to next to the check box.
        checkbox.setIcon(QtGui.QIcon("icon.png"))                    # set a icon to next to the check box.
        checkbox.stateChanged.connect(self.chechboxstate)            # This signal is emitted whenever the state of the checkbox changes.
        checkbox.clicked.connect(self.action)                        # This signal is emitted when the checkbox is clicked



    def QComboBox(self):                                             # All QWidget methods Above Can be used for QComboBox.
        index = 1
        combo = QtWidgets.QComboBox(self)                            # Create QComoBobox instace which is dropdown list allowing single selection.

        # Creation
        combo.addItem("Option 1", userData=100)                      # Add an Item to combo box associated with some data.
        combo.addItems(['option2', 'option3'])                       # Adds multible items in QComboBox.
        combo.insertItem(index, 'option0', userData='Good option')   # insert item in spesefic index.
        combo.insertItems(index, ['op4', 'op5'])                     # Inserts multiple items at the specified index.
        combo.removeItem(index)                                      # Remove item in specified index.
        combo.clear()                                                # Remove all items.

        # Accessing Items
        combo.itemText(index)                                        # Get item data in index.
        combo.itemData(index, Qt.ItemDataRole.UserRole)              # Get item data in index, Rules: {Qt.UserRule, Qt.FontRole, Qt.BackgroundRole, Qt.ToolTipRole}
        combo.setItemText(index, 'option two')                       # To change the text of an item.
        combo.setItemData(index, 'Combo Data')                       # To change the use data of an item.

        # Current item
        combo.currentText()                                          # Returns the text of the currently selected item.
        combo.currentIndex()                                         # Returns the index of the currently selected item.
        combo.setCurrentIndex(index)                                 # Sets the currently selected item by index.
        combo.setCurrentText('New text')                             # Sets the currently selected item by text.

        # Signals
        combo.currentIndexChanged.connect(self.action)               # Emitted when the selected item is changed. It passes the new index
        combo.currentTextChanged.connect(self.action)                # Emitted when the selected item text is changed. It passes the new test (it similar to previos.)
        combo.activated.connect(self.action)                         # Emitted when an item is selected. It passes the index of the selected item.
        combo.highlighted.connect(self.action)                       # Emitted when an item is highlighted (usually when you hover over the item).

        # Other settings
        combo.setEditable(True)                                      # User can edit Just if Editable True.
        combo.setLineEdit()                                          # Set all items as line edit.
        combo.count()                                                # Returns Items number.
        combo.setView(QtWidgets.QAbstractItemView)                   # More Later.



    def QSpinBox_QDoubleSpinBox(self):
        spinBox = QtWidgets.QSpinBox(self)                           # Create the instance.QSpinBox deal with integers.
        doublespin = QtWidgets.QDoubleSpinBox(self)                  # QDoubleSpinBox deal with Floats.
        # Handelling value
        spinBox.value()                                              # Return Current value of QspainBox.
        spinBox.setValue(12)                                         # Set a value of QspainBox.
        spinBox.clear()                                              # Clears the current value (sets it to 0 or the minimum value).
        spinBox.setMinimum(100)                                      # Set max value user cannot go above it.
        spinBox.setMaximum(0)                                        # Set min value user cannot go bellow it.
        spinBox.setRange(0, 100)                                     # Set both Min & Max.
        # Step Handling
        spinBox.setSingleStep(1)                                     # Set jump step in a certain value.
        spinBox.stepBy(5)                                            # Add 5 to current spin Box value.
        # Display handling
        spinBox.setPrefix('pre')                                     # Sets the prefix of the spin box.
        spinBox.setSuffix('Suff')                                    # Sets the suffix of the spin box.
        spinBox.prefix()                                             # Returns the prefix of the spin box (text displayed before the value).
        spinBox.suffix()                                             # Returns the suffix of the spin box (text displayed after the value).
        spinBox.cleanText()                                          # Returns the spin box’s text without the prefix and suffix.
        spinBox.setDisplayIntegerBase(16)                            # Set the display base to hexadecimal (base 16)
        spinBox.setWrapping(True)                                    # Sets whether the spin box should wrap around at the minimum and maximum values.
        # Signals
        spinBox.valueChanged.connect(function(self, int))            # Integer version.
        spinBox.valueChanged.connect(function(self, str))            # Text version.



    def QSlider(self):
        slider = QtWidgets.QSlider(self)                             # Create an instance of QSlider.
        # Handelling value.
        slider.setMaximum(100)                                       # set maximum value for slider
        slider.setMinimum(0)                                         # set minimum value for slider
        slider.setRange(0, 100)                                      # Set both Min & Max.
        slider.value()                                               # Return Current value of QSlider.
        slider.setValue(50)                                          # Set slider to value 50.
        slider.setSingleStep(10)                                     # Set steps to the slider.
        # Tick settings
        slider.setTickPosition(QtWidgets.QSlider.TicksBelow)         # Tick Position {NoTicks, TicksBelow, TicksAbove, TicksBothSides}
        slider.setTickInterval(5)                                    # Set length for each tick.
        slider.setOrientation(Qt.Orientation.Vertical)               # We have also Horezontal option.
        # Signals
        slider.valueChanged.connect(function(int))                   # Integer version.
        slider.valueChanged.connect(function(str))                   # Text version.
        slider.sliderMoved.connect(function(int))                    # return position of the slider.
        slider.sliderPressed.connect(function())                     # function run when slider pressed.
        slider.sliderReleased.connect(function())                    # function run when slider released.


    def QWebEngineView(self):
        browser = PyQt5.QtWebEngineWidgets.QWebEngineView()          # Create a browser widget.
        browser.setUrl(PyQt5.QtCore.QUrl('https://www.google.com'))  # spesify URL.
        browser.setHtml('Normal HTML')                               # Set HTML.
        browser.runJavaScript('document.body.style.backgroundColor = "lightblue";')  # Run JS code in to the current cuntent.


    def QFileDiaLog(self):
        # Static methods.
        file_name, _  = QtWidgets.QFileDialog.getOpenFileName(self,              # Parent.
                                                              'Title',           # Title.
                                                              '',                # opening directory.
                                                              'Images (*.png)')  # Files Filter.      | Images (*.png *.jpg *.bmp);;Text files (*.txt);;All files (*)

        dir = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Dir")     # Select directory.


    def QMeuw(self):
        # Mechanism.
        bar = self.menuBar()                                         # Add a menu bar to the window.

        # Adding Menus inside it.
        file_menu = bar.addMenu('File')                              # Add a menu inside menu bar called 'File'
        edit_menu = bar.addMenu('Edit')                              # Add menu bar called 'Edit'

        # Add Actions to the menus.
        save_act = QtWidgets.QAction('save', self)                   # Create an action.
        file_menu.addAction(save_act)                                # Add the Action.
        file_menu.addSeparator()                                     # Seperator between 'save' and 'image'
        file_menu.addMenu('image')                                   # Add menu inside menu.
        save_act.triggered.connect(self.action)                      # Connect it to a function if triggered.
        save_act.hovered.connect(self.action)                        # Connect it to a function when hovering over it.


    def QTapWidget(self):                                            # TapWiget Actualy uses QtapBar class.
        tabs = QtWidgets.QTabWidget()                                # Create the tab widget which will contain all tabs.

        tab0 = QtWidgets.QWidget()                                   # Create the individual tabs as a normal Widgets.
        tab1 = QtWidgets.QWidget()                                   # All tabs elements Will be inside those Widgets.
        tab2 = QtWidgets.QWidget()                                   # All tabs are indexed with Zero-base indexing .

        tabs.addTab(tab0, 'Tab 0')                                   # This Commend to add Widgets as a tabs.
        tabs.addTab(tab1, 'Tab 1')                                   # First Argument is the QWidget (or any QtWidgets instance).
        tabs.addTab(tab2, 'Tab 2')                                   # Second argument is the text of the tab header.

        tabs.setTabsClosable(True)                                   # Shows or hides close buttons on tabs.
        tabs.setMovable(True)                                        # Allows the tabs to be moved around.


    def QGridLaypout(self):

        grid = QtWidgets.QGridLayout()                               # Create Instance.

        grid.addWidget(QtWidgets.QWidget('Added'), 1, 1)             # Row 1, Col 1.
        grid.addWidget(QtWidgets.QWidget('Span'), 2, 0, 1, 2)        # Spanning 2 columns. | addWidget(widget, row, column, rowspan, colspan)
        grid.removeWidget(QtWidgets)                                 # Remove a widget from the grid.

        grid.setContentsMargins(1, 1, 1, 1)                          # Set a margin to all grid elements. | setContentsMargins(left, top, right, bottom)

        grid.setColumnStretch(1, 2)                                  # stretch a column | setColumnStretch(column, stretch)
        grid.setRowStretch(1, 2)                                     # stretch a Row.


    def QDialog(self):                                               # QDialog.Accepted or (QDialog.Rejected): Returned when the dialog is accepted (or Rejected)
        dialog = QtWidgets.QDialog()                                 # Create a dialog window. almost we sub-class QDialog to create Custom Dialogs windos.
        dialog.setWindowTitle("Title")                               # set title (like any ordinary window).
        dialog.reject()                                              # Called when dialog rejected (make QDialog (QDialog.exec()) Object return QDialog.Rejected).
        dialog.accept()                                              # Called when dialog accepted (make QDialog (QDialog.exec()) Object return QDialog.Accepted).

        if dialog.exec() == QtWidgets.QDialog.accepted():            # Same for QDialog.Rejected
            ... # Do some thing


    def play(self):                                                  # Play sound in PyQt.
        self.player = QtMultimedia.QMediaPlayer()                    # Create the player.
        url = QtCore.QUrl.fromLocalFile('path/to/sound.wav')         # Set URL from local file.
        self.player.setMedia(QtMultimedia.QMediaContent(url))        # Set the content of the player.
        self.player.play()                                           # Play the Sound.


    def QProcess(self):
        process = QtCore.QProcess()
        process.start("picker.exe")


    # Actions--------------------------------------------------------

    def action(self):
        print('Action')


    def textchanged(self, text):
        print(text)


    def chechboxstate(self, state):
        # Handle the state change
        if state == Qt.CheckState.Checked:
            print("checked")
        elif state == Qt.CheckState.Unchecked:
            print("unchecked")
        elif state == Qt.CheckState.PartiallyChecked:
            print("partially checked")

    # Events---------------------------------------------------------

    def moveEvent(self, event: QtGui.QMoveEvent):
        print(event.pos().x(), event.pos().y())                      # Extract x & y position. It Returns QPoint.
        super().moveEvent(event)                                     # Return the event.


    def resizeEvent(self, event: QtGui.QResizeEvent):
        print(event.size().height(), event.size().width())           # It Returns QSize.
        super().resizeEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)                           # Create the app.
    win = Qwidgets()
    win.show()                                                       # Show the window.
    sys.exit(app.exec_())                                            # start Event loop ( exec_() replaced in PyQt5 with exec() )
