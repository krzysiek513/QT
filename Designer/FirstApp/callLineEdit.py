import sys
from PyQt5.QtWidgets import QDialog, QApplication
from selfui import *
#from demoLineEdit import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):
        self.ui.label_2.setText("Hello "
        +self.ui.lineEdit.text())


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())