# coding=utf8

"""

https://www.cnblogs.com/6min/articles/10751959.html
pyQt5 QcomboBox 下拉选项模糊搜索

"""

import os
import sys
import platform
import getpass
import tempfile
import traceback

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QSortFilterProxyModel
from PySide2.QtWidgets import QCompleter, QComboBox


class ExtendedComboBox(QComboBox):
    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)

    # on selection of an item from the completer, select the corresponding item from combobox
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))

    # on model change, update the models of the filter and completer as well
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)

    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)


if __name__ == "__main__":
    import sys
    from PySide2.QtWidgets import QApplication
    from PySide2.QtCore import QStringListModel

    app = QApplication(sys.argv)

    string_list = ['语文 Chinese', '数学 Mathematics', '英语 English']

    combo = ExtendedComboBox()

    # either fill the standard model of the combobox
    combo.addItems(string_list)

    # or use another model
    # combo.setModel(QStringListModel(string_list))

    combo.resize(300, 40)
    combo.show()

    sys.exit(app.exec_())
