import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu


class Tilebar(QMainWindow):
    # def __init__(self):
    #     super().__init__()
    #     self.titlebar()

    def titlebar(self):
        self.statusBar().showMessage('Ready to work')

        exitApp = QAction('Exit', self)
        exitApp.setShortcut('Ctrl+Q')
        exitApp.setStatusTip('Wyjście z aplikacji.')
        exitApp.triggered.connect(qApp.quit)

        importMenu = QMenu('Import', self)
        importHTML = QAction('HTML', self)
        importCSV = QAction('CSV', self)
        importTXT = QAction('TXT', self)

        importMenu.addAction(importHTML)
        importMenu.addAction(importCSV)
        importMenu.addAction(importTXT)



        lineShow = QAction('Wyświetl numer linii', self, checkable=True)
        lineShow.setStatusTip('Wyświetl nr linii')
        lineShow.triggered.connect(self.toggleButton)


        menu = self.menuBar()
        fileMenu = menu.addMenu('File')
        fileMenu.addAction(exitApp)
        fileMenu.addMenu(importMenu)

        viewMenu = menu.addMenu('View')
        viewMenu.addAction(lineShow)

        self.setGeometry(0, 0, 400, 400)
        self.show()

    def toggleButton(self, status):
        if status:
            print('Aktywny.')
        else:
            print('Nieaktywny.')
