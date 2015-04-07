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


def print_log():
    print 'aaa'


# class MessageBox(QtGui.QWidget):
class MessageBox(QtGui.QMainWindow):
    def __init__(self, parent=None):
        # QtGui.QWidget.__init__(self, parent)
        super(MessageBox, self).__init__(parent)

        # self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('quitbutton')
        self.setWindowIcon(QtGui.QIcon('icon/logo.png'))
        self.statusBar().showMessage('statusBar')
        self.resize(250, 150)
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                 (screen.height() - size.height()) / 2)


    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, u'MessageBox中文',
                                           "Quit?",
                                           QtGui.QMessageBox.Yes,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QtGui.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())
