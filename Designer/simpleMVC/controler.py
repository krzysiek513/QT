import sys

from PyQt5.QtWidgets import QDialog, QApplication

from view import *
from model import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.mod = model1()
        self.ui.setupUi(self)
        self.ui.list.addItem(self.mod.list1[0].getNick())
        self.ui.list.addItem(self.mod.list1[1].getNick())
        self.ui.Bshow.clicked.connect(self.showUser)
        self.ui.Badd.clicked.connect(self.addUser)
        self.ui.Bdel.clicked.connect(self.delUser)
        self.show()
        #Bshow Badd Bdel nick LELname LEname list

    def addUser(self):
        studentObj = Student(self.ui.LELname.text(), self.ui.LEname.text(), self.ui.nick.text())
        self.mod.list1.append(studentObj)
        self.ui.list.addItem(studentObj.getNick())

    def delUser(self):
        if self.ui.list.currentItem() != None:
            dele = self.ui.list.takeItem(self.ui.list.currentRow())
            print(dele.text())
            print(self.mod.list1)
            print(self.ui.list.count())
            print(self.ui.list.currentRow())
            for c in self.mod.list1:
                if c.getNick() == dele.text():
                    self.mod.list1.remove(c)
 # nick LELname LEname
    def showUser(self):
        if self.ui.list.currentItem() != None:
            dele = self.ui.list.currentItem()
            print(dele.text())
            print(type(self.mod.list1))
            print(self.ui.list.count())
            print(self.ui.list.currentRow())
            print(self.ui.list.currentItem())
            for c in self.mod.list1:
                print(c.getLastname())
                print(c.getName())
                print(c.getNick())
                if c.getNick() == dele.text():
                    name = c.getName()
                    lastname = c.getLastname()
                    nick = c.getNick()
                    self.ui.LEname.setText(name)
                    self.ui.LELname.setText(lastname)
                    self.ui.nick.setText(nick)
                #     self.ui.LELname.setText(c.getLastName()) ?
                #     self.ui.LEname.setText(c.getName()) ?
                #     self.ui.nick.setText(c.getNick()) ?

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
