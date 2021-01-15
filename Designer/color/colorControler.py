import sys

from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog
from PyQt5.QtGui import QColor

from colorView import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        col = QColor(0, 0, 0)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.frame.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.ui.pushButton.clicked.connect(self.dispcolor)
        self.show()

    def dispcolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.ui.frame.setStyleSheet("QWidget { background-color: %s }" % col.name())
            self.ui.label.setText("color code: " + str(col.name()))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

