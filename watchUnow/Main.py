import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog

from mainView import *

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
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

