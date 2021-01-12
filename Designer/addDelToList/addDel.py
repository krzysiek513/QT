import sys

from PyQt5.QtWidgets import QDialog, QApplication

from list import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.addlist)
        self.ui.dele.clicked.connect(self.delItem)
        self.show()

    def delItem(self):
        row = self.ui.list.currentRow()
        if row != -1:
            self.ui.list.takeItem(row)

    def addlist(self):
        self.ui.list.addItem(self.ui.tekst.text())
        self.ui.tekst.setText('')
        self.ui.tekst.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())