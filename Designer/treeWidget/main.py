import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton
from PyQt5.QtWidgets import QBoxLayout,QTreeWidget,QTreeWidgetItem

class my_app_class(QWidget):
    def __init__(self):
        super().__init__()

        self.add_button=QPushButton('Add item here')
        self.remove_button=QPushButton('Remove item')
        self.wishlist=QTreeWidget(self)
        self.tree_list=QTreeWidget(self)
        # init the UI
        self.initUI()

    def initUI(self):
        # set title of window
        self.setWindowTitle('add and remove items from QTreeWidget!')

        self.init_tree()

        self.resize(800, 480)
        self.center()
        self.show()

    def center(self):
        geometry_frame = self.frameGeometry()
        center_pos = QDesktopWidget().availableGeometry().center()
        geometry_frame.moveCenter(center_pos)
        self.move(geometry_frame.topLeft())


    def init_tree(self):
        headers = ['A','B','C','D']

        self.tree_list.setColumnCount(len(headers))
        self.tree_list.setHeaderLabels(headers)

        self.wishlist.setColumnCount(len(headers))
        self.wishlist.setHeaderLabels(headers)


        list_layout = QBoxLayout(QBoxLayout.LeftToRight)
        list_layout.addWidget(self.tree_list)
        list_layout.addWidget(self.wishlist)

        tree_root = QTreeWidget.invisibleRootItem(self.tree_list)
        # add data to QTreeWidget with QTreeWidgetItem
        my_data = ['1','2','3','4']
        item = QTreeWidgetItem()
        for idx, data in enumerate(my_data):
            item.setText(idx, data)

        tree_root.addChild(item)

        my_data = ['11','10','01','D']
        item = QTreeWidgetItem()
        for idx, data in enumerate(my_data):
            item.setText(idx, data)

        tree_root.addChild(item)

        my_data = ['s', 'c', 'c', 'c']
        item = QTreeWidgetItem()
        for idx, data in enumerate(my_data):
            item.setText(idx, data)

        tree_root.addChild(item)

        btn_layout = QBoxLayout(QBoxLayout.RightToLeft)
        btn_layout.addWidget(self.add_button)
        btn_layout.addWidget(self.remove_button)

        main_layout = QBoxLayout(QBoxLayout.TopToBottom)
        main_layout.addLayout(list_layout)
        main_layout.addLayout(btn_layout)

        self.add_button.clicked.connect(self.move_item)
        self.remove_button.clicked.connect(self.move_item)

        self.setLayout(main_layout)
        return main_layout


    def move_item(self):
        sender = self.sender()

        if self.add_button == sender:
            source = self.tree_list
            target = self.wishlist
        else:
            source = self.wishlist
            target = self.tree_list

        item = QTreeWidget.invisibleRootItem(source).takeChild(source.currentIndex().row())
        QTreeWidget.invisibleRootItem(target).addChild(item)

if __name__=='__main__':
    # start the QApplication
    my_application = QApplication(sys.argv)
    # create aplication with the class
    example = my_app_class()
    # use exit for QApplication
    sys.exit(my_application.exec_())