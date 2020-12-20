import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, \
    QWidget, QListWidget, QPlainTextEdit, QListView, QAbstractItemView, QListWidgetItem, QDialog, QGridLayout, \
    QLineEdit, QLabel
import Pracownik


class QtApp(QWidget):
    def __init__(self, *args, **kwargs):
        super(QtApp, self).__init__(*args, **kwargs)
        self.setWindowTitle('QtApp')
        self.listWidget = QListWidget()
        self.initUI()
        # self.initSignals()
        i=0
        listaPracownikow = []

    def initUI(self):
        button_A = QPushButton('dodaj', self)
        button_A.setFixedSize(75, 50)
        button_A.clicked.connect(self.dodaj)
        button_B = QPushButton('usuń', self)
        button_B.setFixedSize(75, 50)
        button_B.clicked.connect(self.usun)

        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget.setMovement(QListView.Free)
        self.listWidget.setMouseTracking(True)

        resultView = QPlainTextEdit(self)
        resultView.setReadOnly(True)

        h_box = QHBoxLayout()
        h_box.addWidget(button_A)
        h_box.addWidget(button_B)

        h2_box = QHBoxLayout()
        h2_box.addWidget(self.listWidget)
        h2_box.addWidget(resultView)

        v_box = QVBoxLayout()
        v_box.addLayout(h2_box)
        v_box.addLayout(h_box)
#        v_box.setGeometry(300, 300, 300, 150)

        self.setLayout(v_box)

    def dodaj(self):
        dialogBox = QDialog()
        dialogBox.setWindowTitle('dodaj')
        gridLayout = QGridLayout()
        dialogBox.setLayout(gridLayout)

        def add():
            imie = EImie.text()
            nazwisko = ENazwisko.text()
            if nazwisko=='':
                self.listWidget.addItem('?')
                #listaPracownikow.append(Pracownik.Pracownik(nazwisko='?'))
            else:
                nowy2 = Pracownik.Pracownik(imie="Barbara", nazwisko="Kotecka", stanowisko="Sekretrka", nrPracownika=2,
                                            wyplata=4444)
                self.listWidget.addItem(nowy2)
            # nowy2 = Pracownik.Pracownik(imie="Barbara", nazwisko="Kotecka", stanowisko="Sekretrka", nrPracownika=2,
            #                             wyplata=4444)
            # listaPracownikow.append(nowy2)
            # self.listWidget.addItem(Pracownik.Pracownik(imie, nazwisko))

        def anu():
            dialogBox.close()

        imie = QLabel('imie', dialogBox)
        EImie = QLineEdit()
        nazwisko = QLabel('nazwisko', dialogBox)
        ENazwisko = QLineEdit()


        buttonAdd = QPushButton('dodaj', dialogBox)
        #dialogBox.setFixedSize(200, 200)
        buttonAdd.clicked.connect(add)

        buttonDel = QPushButton('anuluj', dialogBox)
        buttonDel.clicked.connect(anu)

        gridLayout.addWidget(imie, 0, 0)
        gridLayout.addWidget(EImie, 0, 1)
        gridLayout.addWidget(nazwisko, 1, 0)
        gridLayout.addWidget(ENazwisko, 1, 1)
        gridLayout.addWidget(buttonAdd, 2, 0)
        gridLayout.addWidget(buttonDel, 2, 1)
        dialogBox.exec_()

    def usun(self):
        x = self.listWidget.currentRow()
        self.listWidget.itemDelegate(x)



    def initSignals(self):
        # self.listWidget.currentItemChanged.connect(self.onCurrentItemChanged)
        # self.listWidget.currentRowChanged.connect(self.onCurrentRowChanged)
        # self.listWidget.currentTextChanged.connect(self.onCurrentTextChanged)
        # self.listWidget.itemActivated.connect(self.onItemActivated)
        # self.listWidget.itemChanged.connect(self.onItemChanged)
        self.listWidget.itemClicked.connect(self.onItemClicked)
        # self.listWidget.itemDoubleClicked.connect(self.onItemDoubleClicked)
        self.listWidget.itemEntered.connect(self.onItemEntered)
        # self.listWidget.itemPressed.connect(self.onItemPressed)
        # self.listWidget.itemSelectionChanged.connect(self.onItemSelectionChanged)

    def onItemEntered(self):
        i=i+1

    def onItemClicked(self):
        print(f'Wybrany obiekt z listy: {pozycja.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QtApp()
    window.show()
    app.exec_()
