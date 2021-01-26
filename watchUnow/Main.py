import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog, QLabel, QLineEdit, QPushButton, QDialog, \
    QGridLayout, QListWidgetItem
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt

from mainView import *
from data import  *

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
        self.mod = model()
        self.ui.setupUi(self)
        self.ui.listWidget.addItem(self.mod.list1[0].getName())
        self.ui.actionNew.triggered.connect(self.newListItem)
        # self.ui.actionOpen.triggered.connect(self.openFileDialog)
        # self.ui.actionSave.triggered.connect(self.saveFileDialog)

        ###################################################
        ##
        ##  Sygnały
        ##
        ###################################################

        self.ui.listWidget.itemClicked.connect(self.onItemClicked)

        self.show()

    def onItemClicked(self, item):
        x = self.ui.listWidget.currentRow()
        print(f'{item.text()}, miejsce {x}, typ {type(item)}')

    def newListItem(self):
        dialogBox = QDialog()
        dialogBox.setWindowTitle('dodaj')
        gridLayout = QGridLayout()
        dialogBox.setLayout(gridLayout)

        ##########################################
        ##  ustawić focus na EImie
        ##########################################

        def add():
            nazwa = EImie.text()
            if nazwa != '':
                dane = Dane(nazwa, '')
                #self.ui.listWidget.addItem(QListWidgetItem(nazwa))
                self.ui.listWidget.addItem(dane.name)
                self.ui.textEdit.setText(dane.tekst)
                self.mod.list1.append(dane)
                dialogBox.close()

        def anu():
            dialogBox.close()

        nazwa = QLabel('nazwa', dialogBox)
        EImie = QLineEdit()

        buttonAdd = QPushButton('dodaj', dialogBox)
        # dialogBox.setFixedSize(200, 200)
        buttonAdd.clicked.connect(add)

        buttonDel = QPushButton('anuluj', dialogBox)
        buttonDel.clicked.connect(anu)

        gridLayout.addWidget(nazwa, 0, 0)
        gridLayout.addWidget(EImie, 0, 1)
        gridLayout.addWidget(buttonAdd, 1, 0)
        gridLayout.addWidget(buttonDel, 1, 1)
        dialogBox.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(palette)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

