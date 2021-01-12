import sys

from PyQt5.QtWidgets import QDialog, QApplication

from sliders import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.sugarhorizontalScrollBar.valueChanged.connect(self.scrollhorizontal)
        self.ui.pusleLVLverticalScrollBar.valueChanged.connect(self.scrollvertical)
        self.ui.presyrehorizontalSlider.valueChanged.connect(self.sliderhorizontal)
        self.ui.cholesterolLVLverticalSlider.valueChanged.connect(self.slidervertical)
        self.show()

    def scrollhorizontal(self, value):
        self.ui.result.setText("Sugar Level : " + str(value))

    def scrollvertical(self, value):
        self.ui.result.setText("Pulse Rate : " + str(value))

    def sliderhorizontal(self, value):
        self.ui.result.setText("Blood Pressure : " + str(value))

    def slidervertical(self, value):
        self.ui.result.setText("Cholestrol Level : " + str(value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())