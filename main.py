# coding:utf-8

import re
import os
import sys
import json
import socket
import logging
import getpass
import tempfile
import traceback

# env_config_path = os.environ.get('ENV_CONFIG_PATH') or r'D:/code/git/pipe_config/configuration/env_config'
# if env_config_path not in sys.path:
#     sys.path.insert(0, env_config_path)
# import ff_env
# ff_env.set_environ()

from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

from widgets import proj_combox
from widgets import x_list_widget
import utils

__version__ = 'v0.0.1'


class MainUI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)

        self.setWindowTitle(u'ElementFinder-{}'.format(__version__))
        self.resize(1100, 700)

        # self.ui = Ui_Dialog()
        # self.ui.setupUi(self)

        self.set_ui()

    def set_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.tabs = QtWidgets.QTabWidget()
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)

        self.seq_list_widget = x_list_widget.ListWithSearch(label='Sequences')
        self.splitter.addWidget(self.seq_list_widget)
        self.seq_fill_data(utils.seqs())
        self.seq_list_widget.clicked.connect(self.refresh)

        self.shot_list_widget = x_list_widget.ListWithSearch(label='Shots')
        self.splitter.addWidget(self.shot_list_widget)
        self.shot_list_widget.clicked.connect(self.refresh)

        self.step_list_widget = x_list_widget.ListWithSearch(label='Step')
        self.splitter.addWidget(self.step_list_widget)
        self.step_list_widget.clicked.connect(self.refresh)

        self.splitter.addWidget(x_list_widget.ListWithSearch(label='Elements'))
        self.splitter.addWidget(x_list_widget.ListWithSearch(label='Paths'))

        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 1)
        self.splitter.setStretchFactor(2, 1)
        self.splitter.setStretchFactor(3, 1)
        self.splitter.setStretchFactor(4, 5)

        self.tabs.addTab(self.splitter, u"Shot")
        self.tabs.addTab(QtWidgets.QTextEdit(), u"Asset")

        proj_layout = QtWidgets.QHBoxLayout()
        projs = utils.projs()
        self.projs_combo = proj_combox.ExtendedComboBox()
        self.projs_combo.setMinimumWidth(150)

        proj_layout.addWidget(self.projs_combo)
        proj_layout.addStretch()
        # either fill the standard model of the combobox
        self.projs_combo.addItems(projs)

        self.main_layout.addLayout(proj_layout)
        self.main_layout.addWidget(self.tabs)

        self.style_sheet()

    def shot_fill_data(self, seq):
        # if not data:
        self.shot_list_widget.fill_data(['0010', '0020'])

    def seq_fill_data(self, data):
        self.seq_list_widget.fill_data(data)

    def style_sheet(self):
        path = r"./flatwhite/Style.qss".replace('\\', '/')
        with open(path, 'r') as file:
            self.setStyleSheet(file.read().decode('utf8'))

    def refresh(self, text):
        proj = self.projs_combo.currentText()
        print(proj.split(' ')[0], '<<projs_combo')
        title = text.split(' ')[0]
        key = text.split(' ')[1]
        print(title, '<<title')
        print(key, '<<key')
        if title == 'Sequences':
            self.shot_fill_data(seq=key)


if __name__ == '__main__':
    app = None
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication([])

    dlg = MainUI()
    dlg.show()

    if app:
        app.exec_()
