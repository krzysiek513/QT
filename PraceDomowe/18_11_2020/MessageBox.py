import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QWidget

from PyQt5.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'Quit'
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 300)
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle(self.name)

        buttonMsg = QPushButton('Quit', self)
        buttonMsg.resize(150, 25)
        buttonMsg.move(100, 150)
        buttonMsg.clicked.connect(self.showMsg)

        self.show()

    def closeEvent(self, event):
        """Generate 'question' dialog on clicking 'X' button in title bar.

        Reimplement the closeEvent() event handler to include a 'Question'
        dialog with options on how to proceed - Save, Close, Cancel buttons
        """
        choice = QMessageBox.question(
            self, "Quit",
            "Czy aby na pewno?",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore,
            QMessageBox.Ignore)

        if choice == QMessageBox.Yes:
            event.accept()
            print('do zobaczenia')
        else:
            event.ignore()
            print('inaczej')

    def keyPressEvent(self, event):
        """Close application from escape key.

        results in QMessageBox dialog from closeEvent, good but how/why?
        """
        if event.key() == Qt.Key_Escape:
            # QMessageBox kan bi tu
            self.close()

    def showMsg(self):
        choice = QMessageBox.question(self, 'Quit1', 'Czy na pewno chciałeś wyjść',
                                      QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore, QMessageBox.No)

        if choice == QMessageBox.Yes:
            print('To było zamierzone.')
            sys.exit()
        elif choice == QMessageBox.No:
            print('Nie wiem czemu to zrobiłem.')
        else:
            print('Coś się ewidentnie popsuło')

    def showStatus(self, status):
            print('Status przycisku:', status.text())


if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyWindow()
        sys.exit(app.exec_())