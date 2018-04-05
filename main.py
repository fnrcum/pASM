# encoding: cp1252
import sys
from PyQt5.QtGui import *
from options_gui import Example
import PyQt5
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example(app)
    ex.show()
    sys.exit(app.exec_())
