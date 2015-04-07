# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-03-25 16:03:07
Edit time: 2015-03-25 16:03:28
File name: demo.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(u'中文Icon')
        self.setWindowIcon(QtGui.QIcon('icon/logo.png'))

app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())

