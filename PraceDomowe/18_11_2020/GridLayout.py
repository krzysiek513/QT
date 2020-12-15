import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'GridLayout'
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 300)
        self.setGeometry(0, 0, 300, 300)

        # 0,0 0,1 0,2
        # 1,0 1,1 1,2
        # 2,0 2,1 2,2

        gridLayout = QGridLayout(self)

        for x in range(3):
            for y in range(3):
                button = QPushButton(str(x)+', '+str(y), self)
                button.clicked.connect(self.press)
                gridLayout.addWidget(button, x, y)

        self.show()

    def press(self):
        button = self.sender()
        print(button.text(), ":", button.pos(), button.geometry())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())