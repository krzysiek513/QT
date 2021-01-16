import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt

from mainView import *

palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionNew.triggered.connect(self.newView)
        # self.ui.actionOpen.triggered.connect(self.openFileDialog)
        # self.ui.actionSave.triggered.connect(self.saveFileDialog)
        self.show()

    def newView(self):
        pass

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(palette)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

