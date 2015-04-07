# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-03-25 16:05:47
Edit time: 2015-03-25 16:06:36
File name: tooltip.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import sys
from PyQt4 import QtGui, QtCore

class Tooltip(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltip')
        self.setToolTip('This is a <b>QWidget</b> widget')
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))

app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())

# 没有tooltip

'''
if __name__ == '__main__':
    pass
'''
