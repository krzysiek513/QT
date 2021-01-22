import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog, QLabel, QLineEdit, QPushButton, QDialog, \
    QGridLayout, QTreeWidgetItem

from lottoView import *


class MyForm(QMainWindow):
    pierwsza = 0
    druga = 0
    trzecia = 0
    czwarta = 0
    piata = 0
    szosta = 0

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ile
        self.ui.setupUi(self)
        print(self.losowe())
        self.ui.pushButton.clicked.connect(self.pokaz)
        self.ui.spinBox.valueChanged.connect(self.ui.spinBox.value())

    def pokaz(self):
        self.ui.textEdit.addItem(str(self.losowe()))

    def poka(self):
        print(self.ui.lineEdit.text())
        c = self.ui.lineEdit.text()
        print(type(c))
        a = c.split()
        count = 0
        for int3 in a:
            count += 1
            print(type(int(int3)))
        print(count)


    def losowe(self):
        pierwsza = random.randint(1, 60)
        druga = random.randint(1, 60)
        trzecia = random.randint(1, 60)
        czwarta = random.randint(1, 60)
        piata = random.randint(1, 60)
        szosta = random.randint(1, 60)
        while pierwsza != druga and pierwsza != trzecia \
                and pierwsza != czwarta and pierwsza != piata \
                and pierwsza != szosta and druga != trzecia and druga != czwarta \
                and druga != piata and druga != szosta and trzecia != czwarta \
                and trzecia != piata and trzecia != szosta and czwarta != piata \
                and czwarta != szosta and piata != szosta:
            pierwsza = random.randint(1, 60)
            druga = random.randint(1, 60)
            trzecia = random.randint(1, 60)
            czwarta = random.randint(1, 60)
            piata = random.randint(1, 60)
            szosta = random.randint(1, 60)
        lista = (pierwsza, druga, czwarta, trzecia, piata, szosta)
        return lista


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
