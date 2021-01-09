import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu, QHBoxLayout, QComboBox, QLabel


#from title import titlebar

class watchUnow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.comboBox = QComboBox()
        self.initUI()

    def initUI(self):
        self.resize(300, 300)
        self.setWindowTitle('watchUnow')

        self.statusBar().showMessage('Ready to work')

        #titlebar
        newCanvas = QAction('New', self)
        newCanvas.setShortcut('Ctrl+N')
        newCanvas.setStatusTip('New file')
        newCanvas.triggered.connect(self.toggleButton)

        openCanvas = QAction('Open', self)
        openCanvas.setShortcut('Ctrl+O')
        openCanvas.setStatusTip('Open file')
        openCanvas.triggered.connect(self.toggleButton)

        saveCanvas = QAction('Save', self)
        saveCanvas.setShortcut('Ctrl+S')
        saveCanvas.setStatusTip('Open file')
        saveCanvas.triggered.connect(self.toggleButton)

        preferences = QAction('Preferences', self)
        preferences.setStatusTip('App settings')
        preferences.triggered.connect(self.toggleButton)

        menu = self.menuBar()
        fileMenu = menu.addMenu('file')
        fileMenu.addAction(newCanvas)
        fileMenu.addAction(openCanvas)
        fileMenu.addAction(saveCanvas)

        editMenu = menu.addMenu('edit')
        editMenu.addAction(preferences)

    #     #layout
    #     layout = QHBoxLayout()
    #     self.comboBox.addItems(['Aktywny', 'Nieaktywny'])
    #     self.comboBox.currentIndexChanged.connect(self.selectChange)
    #     layout.addWidget(self.comboBox)
    #
    #     self.setLayout(layout)
    #     self.show()8
    #
    # def selectChange(self, status):
    #     print(f'Index: {status} | Text: {self.comboBox.currentText()}')

    def toggleButton(self, status):
        if status:
            print('Aktywny.')
        else:
            print('Nieaktywny.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icons/icon.png'))
    window = watchUnow()
    window.show()
    sys.exit(app.exec_())
