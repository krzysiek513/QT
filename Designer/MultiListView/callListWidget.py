import sys

from PyQt5.QtWidgets import QDialog, QApplication

from ListWidget import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidgetTools.itemSelectionChanged.connect(self.dispSelectedTest)
        self.show()

    def dispSelectedTest(self):
        self.ui.listWidgetSelected.clear()
        items = self.ui.listWidgetTools.selectedItems()
        x = []
        for i in list(items):
            self.ui.listWidgetSelected.addItem(i.text())
            x.append(str(i.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())