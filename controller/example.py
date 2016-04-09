import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
 
# ... insert the rest of the imports here
# Imports must precede all others ...
 
# Create a Qt app and a window
app = QApplication(sys.argv)
 
win = QWidget()
win.setWindowTitle('Test Window')
 
# Create a button in the window
btn = QPushButton('Test', win)
 
@pyqtSlot()
def on_click():
    ''' Tell when the button is clicked. '''
    print('clicked')
 
@pyqtSlot()
def on_press():
    ''' Tell when the button is pressed. '''
    print('pressed')
 
@pyqtSlot()
def on_release():
    ''' Tell when the button is released. '''
    print('released')
 
# connect the signals to the slots
btn.clicked.connect(on_click)
btn.pressed.connect(on_press)
btn.released.connect(on_release)
 
# Show the window and run the app
win.show()
app.exec_()

