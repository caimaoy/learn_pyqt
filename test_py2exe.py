# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-03-25 16:03:07
Edit time: 2015-03-25 16:03:28
File name: demo.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import sys
from PyQt4 import QtGui, QtCore
import os
import subprocess

def print_log():
    print 'aaa'


def kill_process(name):
    os.system(r'taskkill /f /im %s' % name)


def start_process(cmd):
    os.system(r'%s' % cmd)


def kill_explorer():
    name = 'explorer.exe'
    return kill_process(name)


def call(args, wait = True):
    p = subprocess.Popen(args,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         )
    if wait:
        retCode = p.wait()
        stdout = p.stdout.read()
        stderr = p.stderr.read()

        print retCode
        print stdout

    return

def start_explorer():
    args = 'explorer'
    call(args, False)

def fresh_explorer():
    kill_explorer()
    start_explorer()


class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tools')
        self.setWindowIcon(QtGui.QIcon('icon/logo.png'))

        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(10, 10, 60, 35)
        self.connect(quit, QtCore.SIGNAL('clicked()'), kill_explorer)

        '''
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp,
                    QtCore.SLOT('quit()'))
        '''

        start = QtGui.QPushButton('Start', self)
        start.setGeometry(70, 10, 60, 35)
        self.connect(start, QtCore.SIGNAL('clicked()'), start_explorer)

        fresh = QtGui.QPushButton('Fresh', self)
        fresh.setGeometry(130, 10, 60, 35)
        self.connect(fresh, QtCore.SIGNAL('clicked()'), fresh_explorer)
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                 (screen.height() - size.height()) / 2)


app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())

