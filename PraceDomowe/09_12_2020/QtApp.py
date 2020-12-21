import sys

from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout, \
    QWidget, QListWidget, QPlainTextEdit, QListView, QAbstractItemView, QListWidgetItem, QDialog, QGridLayout, \
    QLineEdit, QLabel, QProgressBar


class QtApp(QWidget):
    def __init__(self, *args, **kwargs):
        super(QtApp, self).__init__(*args, **kwargs)
        self.setWindowTitle('QtApp')
        self.listWidget = QListWidget(self)
        self.initUI()

    def initUI(self):
        button_A = QPushButton('dodaj', self)
        button_A.setFixedSize(75, 50)
        button_A.clicked.connect(self.dodaj)
        button_B = QPushButton('usuń', self)
        button_B.setFixedSize(75, 50)
        button_B.clicked.connect(self.usun)

        self.progressBar = QProgressBar(self)

        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget.setMovement(QListView.Free)
        self.listWidget.setMouseTracking(True)

        self.listWidget.addItem('Krzysiek Jot')
        self.listWidget.addItem('replika Jot')

        self.resultView = QPlainTextEdit(self)
        self.resultView.setReadOnly(True)

        h_box = QHBoxLayout()
        h_box.addWidget(button_A)
        h_box.addWidget(button_B)

        h2_box = QHBoxLayout()
        h2_box.addWidget(self.listWidget)
        h2_box.addWidget(self.resultView)

        h3_box = QHBoxLayout()
        h3_box.addWidget(self.progressBar)

        v_box = QVBoxLayout()
        v_box.addLayout(h2_box)
        v_box.addLayout(h_box)
        v_box.addLayout(h3_box)
#        v_box.setGeometry(300, 300, 300, 150)

        self.listWidget.itemClicked.connect(self.showCurrentInfo)
        self.setLayout(v_box)

    # def onItemEntered(self):
    #     self.resultView.appendHtml(
    #         '{0}: {1}'.format(formatColor('itemEntered', QColor(Qt.darkCyan)), item.text()))

    def TimeCount(self):
        value = self.listWidget.__len__()*10
        if value < 100:
            self.progressBar.setValue(value)
        else:
            self.listWidget.setDisabled()
            print('Mamy 100%')

    def showCurrentInfo(self, pozycja):
        x = self.listWidget.currentRow()
        self.resultView.appendPlainText(f'{pozycja.text()}, miejsce {x+1}')

    def dodaj(self):
        dialogBox = QDialog()
        dialogBox.setWindowTitle('dodaj')
        gridLayout = QGridLayout()
        dialogBox.setLayout(gridLayout)

        def add():
            imie = EImie.text()
            nazwisko = ENazwisko.text()
            if nazwisko!='' and imie!='':
                text=imie+' '+nazwisko
                self.listWidget.addItem(QListWidgetItem(text))
                EImie.clear()
                ENazwisko.clear()
                x = self.listWidget.__len__()
                self.resultView.appendPlainText(f'dodano {text}, miejsce {x}')
                self.progressBar.setValue(x*10)

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
        row = self.listWidget.currentRow()
        print(row)
        if row!=-1:
            self.resultView.appendPlainText(f'usunieto {self.listWidget.item(row).text()}, miejsce {row + 1}')
            self.listWidget.takeItem(row)
            value = self.listWidget.__len__()
            print(value)
            self.progressBar.setValue(value*10)



            # def initSignals(self):
    #     # self.listWidget.currentItemChanged.connect(self.onCurrentItemChanged)
    #     # self.listWidget.currentRowChanged.connect(self.onCurrentRowChanged)
    #     # self.listWidget.currentTextChanged.connect(self.onCurrentTextChanged)
    #     # self.listWidget.itemActivated.connect(self.onItemActivated)
    #     # self.listWidget.itemChanged.connect(self.onItemChanged)
    #     self.listWidget.itemClicked.connect(self.onItemClicked)
    #     # self.listWidget.itemDoubleClicked.connect(self.onItemDoubleClicked)
    #     self.listWidget.itemEntered.connect(self.onItemEntered)
    #     # self.listWidget.itemPressed.connect(self.onItemPressed)
    #     # self.listWidget.itemSelectionChanged.connect(self.onItemSelectionChanged)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QtApp()
    window.show()
    app.exec_()
