import sys
import os
from subprocess import Popen
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QPushButton
from PyQt5.QtCore import *

# Errno
def errno_1():
    QMessageBox.critical(None, "Error", "[Errno 1] Cannot start additional program.", QMessageBox.Ok | QMessageBox.Ok)
    print("ERROR: [Errno 1] Cannot start additional program.")

# Button
class QClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def onClick(self):
        try:
            Popen(args = [str(os.system("\"" + os.path.join("", "StartRRC.bat") + "\""))], shell = True)
        except:
            errno_1()
    def initUI(self):
        self.button = QPushButton(u"随机点名", self)
        self.button.setGeometry(10, 10, 100, 100)
        self.button.clicked.connect(self.onClick)
        self.resize(300, 300)
        desktop = QApplication.desktop()
        x = (desktop.width() - self.width() - 10)
        y = (desktop.height() - self.height() - 110)
        self.move(x, y)
        self.setWindowTitle(u'工具栏')
        self.setWindowFlag(Qt.Tool)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.5)
        self.show()
        self.setAttribute(Qt.WA_QuitOnClose)

# Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QClass()
    sys.exit(app.exec_())
