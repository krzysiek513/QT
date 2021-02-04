import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog, QLabel, QLineEdit, QPushButton, QDialog, \
    QGridLayout, QListWidgetItem
from PyQt5.QtGui import QKeySequence, QPalette, QColor, QContextMenuEvent
from PyQt5.QtCore import Qt

from mainView import *
from data import *
from ContextMenu import *

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
        #self.ctx = ContextMenu(self)
        self.ui.setupUi(self)
        # self.ui.listWidget.addItem(self.mod.list1[0].getName())
        # self.ui.textEdit.setText(self.mod.list1[0].getTekst())
        self.ui.actionNew.triggered.connect(self.newList)
        self.ui.actionQuit.triggered.connect(self.quit)
        if self.mod.list1 == []:
            self.ui.textEdit.setReadOnly(True)

        # actionBugs - howto
        #
        self.ui.actionBugs.triggered.connect(self.bugs)
        self.ui.actionWorking.triggered.connect(self.working)
        self.ui.actionAbout.triggered.connect(self.showInfo)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.saveFile)

    def newList(self):
        choice = QMessageBox.question(self, 'Nowa lista', 'Czy na pewno chciałesz usunąć starą liste?',
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            self.mod.list1.clear()
            self.ui.listWidget.clear()
            self.ui.textEdit.clear()
            self.ui.textEdit.setReadOnly(True)

    def bugs(self):
        msgb = QMessageBox()
        msgb.setIcon(QMessageBox.Information)
        msgb.setText(self.mod.bug)
        msgb.setWindowTitle('Working')
        msgb.setStandardButtons(QMessageBox.Ok)
        msgb.exec_()

    def working(self):
        msgb = QMessageBox()
        msgb.setIcon(QMessageBox.Information)
        msgb.setText(self.mod.done)
        msgb.setWindowTitle('Working')
        msgb.setStandardButtons(QMessageBox.Ok)
        msgb.exec_()

    def showInfo(self):
        msgb = QMessageBox()
        msgb.setIcon(QMessageBox.Information)
        msgb.setText(self.mod.info)
        msgb.setWindowTitle('About')
        msgb.setStandardButtons(QMessageBox.Ok)
        msgb.exec_()

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            self.mod.list1.clear()
            self.ui.listWidget.clear()
            self.ui.textEdit.clear()

            with f:
                data = f.read()
                print(data)
                lines = data.split('\n')
                for line in lines:
                    x = line.find('nazwaPolaDanych:')
                    y = line.find('danePodpieteDoPolaDanych:')
                    if x != -1 and y != -1:
                        # print(line[16:y])
                        # print(line[y+25:])
                        # print(x)
                        # print(y)
                        dane = Dane(line[16:y], line[y+25:])
                        print(type(dane))
                        print(dane.name)
                        print(dane.tekst)
                        self.mod.list1.append(dane)
                        self.ui.listWidget.addItem(dane.name)
            print(self.mod.list1[1].getTekst())
            self.ui.textEdit.setText(self.mod.list1[0].getTekst())

    def saveFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        f = open(fileName, 'w')
        i = 0
        for item in self.mod.list1:
            dane = self.mod.list1[i].getTekst()
            name = self.mod.list1[i].getName()
            output = f"nazwaPolaDanych:{name}danePodpieteDoPolaDanych:{dane}\n"
            f.write(output)
            i = i + 1
        f.close()

    def quit(self):
        qApp.quit()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction('New Item')
        dele = cmenu.addAction('Delete Item')
        quitAction = cmenu.addAction('Quit')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAction:
            qApp.quit()

        if action == newAct:
            self.newListItem()

        if action == dele:
            if self.ui.listWidget.currentItem() != None:
                dele = self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
                self.ui.textEdit.setText('')
                # print(dele.text())
                # print(self.mod.list1)
                # print(self.ui.listWidget.count())
                # x = self.ui.listWidget.currentRow()
                # print(x)
                # self.mod.list1.remove()
                for c in self.mod.list1:
                    if c.getName() == dele.text():
                        self.mod.list1.remove(c)

        ###################################################
        ##
        ##  Sygnały
        ##
        ###################################################

        self.ui.textEdit.textChanged.connect(self.onTextChanged)
        self.ui.listWidget.itemClicked.connect(self.onItemClicked)

        self.show()

    def onTextChanged(self):
        if self.ui.listWidget.currentItem() != None:
            x = self.ui.listWidget.currentRow()
            # print(f'{x}, typ {type(x)}, tekst {self.ui.textEdit.toPlainText()}')
            self.mod.list1[x].setText(self.ui.textEdit.toPlainText())

    def onItemClicked(self, item):
        if self.ui.listWidget.currentItem() != None:
            x = self.ui.listWidget.currentRow()
            # print(f'{item.text()}, miejsce {x}, typ {type(item)}')
            self.ui.textEdit.setText(self.mod.list1[int(x)].getTekst())
            # print(self.mod.list1[int(x)].getTekst())

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
                self.mod.list1.append(dane)
                self.ui.textEdit.setReadOnly(False)
                dialogBox.close()

        def anu():
            dialogBox.close()

        nazwa = QLabel('nazwa', dialogBox)
        EImie = QLineEdit()
        EImie.setFocus()


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

