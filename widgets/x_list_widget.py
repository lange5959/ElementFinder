# coding=utf8

from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore


class ListWithSearch(QtWidgets.QWidget):
    clicked = QtCore.Signal(str)

    def __init__(self, parent=None, data=[], label=''):
        super(ListWithSearch, self).__init__(parent)

        self.resize(520, 360)

        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel(label)
        self.lineedit = QtWidgets.QLineEdit()
        self.lineedit.setPlaceholderText('Search')
        self.listwidget = QtWidgets.QListWidget()

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.lineedit)
        self.main_layout.addWidget(self.listwidget)

        self.data = data

        self.listwidget.addItems(self.data)
        self.lineedit.setCompleter(QtWidgets.QCompleter(self.data))

        self.lineedit.returnPressed.connect(self.search)
        self.listwidget.doubleClicked.connect(self.double_clicked)
        self.listwidget.clicked.connect(self.list_clicked)

        self.add_menu()

    def add_menu(self):
        self.listwidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        open_ = QtWidgets.QAction("menu1", self.listwidget)
        self.listwidget.addAction(open_)
        open_.triggered.connect(self.run)

    def run(self):
        items = self.listwidget.selectedItems()
        item = next(iter(items), None)
        if not item:
            return
        print(item.text())

    def double_clicked(self):
        item = self.listwidget.selectedItems()[0]
        print(item.text())

    def list_clicked(self):
        item = self.listwidget.selectedItems()[0]
        print(item.text())

        text = ' '.join([self.label.text(), item.text()])
        # self.clicked.emit(item.text())
        self.clicked.emit(text)

    def item_wanted(self, text):
        items_wanted = []

        for i in self.data:
            if text in i:
                items_wanted.append(i)

        return items_wanted

    def search(self):
        text = self.lineedit.text()
        items_wanted = self.item_wanted(text)
        self.listwidget.clear()
        self.listwidget.addItems(items_wanted)

    def fill_data(self, data):
        self.data = data
        self.listwidget.clear()
        self.listwidget.addItems(data)
        self.lineedit.setCompleter(QtWidgets.QCompleter(self.data))


if __name__ == '__main__':
    app = None
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication([])

    dlg = ListWithSearch()
    dlg.show()

    if app:
        app.exec_()
