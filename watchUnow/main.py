import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QApplication, QPushButton

class ListaDemo(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ListaDemo()
    window.show()
    sys.exit(app.exec_())
