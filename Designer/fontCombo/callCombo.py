
import sys

from PyQt5.QtWidgets import QDialog, QApplication

from demoCombo import *

class MyForm(QDialog):
    def __init__(self):
        fontSize = 8
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        myFont=QtGui.QFont(self.ui.fontComboBox.itemText(self.ui.fontComboBox.currentIndex()),fontSize)
        self.ui.textEdit.setFont(myFont)
        self.ui.fontComboBox.currentFontChanged.connect(self.changeFont)
        self.ui.spinBox.setValue(fontSize)
        self.ui.spinBox.valueChanged.connect(self.changeSize)
        self.show()

    def changeSize(self):
        myFont = QtGui.QFont(self.ui.fontComboBox.itemText(self.ui.fontComboBox.currentIndex()),
                             self.ui.spinBox.value())
        self.ui.textEdit.setFont(myFont)

    def changeFont(self):
        myFont=QtGui.QFont(self.ui.fontComboBox.itemText(self.ui.fontComboBox.currentIndex()),
                           self.ui.spinBox.value())
        self.ui.textEdit.setFont(myFont)


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())