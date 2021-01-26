import sys

from PyQt5.QtGui import QContextMenuEvent
from PyQt5.QtWidgets import *

class ContextMenu(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction('New print')
        quitAction = cmenu.addAction('Quit')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAction:
            qApp.quit()

        if action == newAct:
            print('Wcisnąłem przycisk New print')