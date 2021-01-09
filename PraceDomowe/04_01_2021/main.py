import PyQt5.QtWidgets
import sys


class WatchUnow(QMainWindow):
    def __init__(self):
        super().__init__()


def main():
    app = QApplication(sys.argv)
    window = watchUnow()
    window.show()
    sys.exit(app.exec_())
