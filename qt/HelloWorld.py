# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelloWorld.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 421, 101))
        font = QtGui.QFont()
        font.setFamily("Roughwork Demo")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuQT = QtWidgets.QMenu(self.menubar)
        self.menuQT.setObjectName("menuQT")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menuPT = QtWidgets.QMenu(self.menubar)
        self.menuPT.setObjectName("menuPT")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsyx = QtWidgets.QAction(MainWindow)
        self.actionsyx.setObjectName("actionsyx")
        self.menu.addAction(self.actionsyx)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuQT.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menuPT.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HelloWorld"))
        self.label.setText(_translate("MainWindow", "HELLO PYQT"))
        self.menu.setTitle(_translate("MainWindow", "傻逼"))
        self.menuQT.setTitle(_translate("MainWindow", "QT"))
        self.menu_2.setTitle(_translate("MainWindow", "真难装"))
        self.menu_3.setTitle(_translate("MainWindow", "还是"))
        self.menuPT.setTitle(_translate("MainWindow", "PY"))
        self.menu_4.setTitle(_translate("MainWindow", "省头发"))
        self.actionsyx.setText(_translate("MainWindow", "syx"))

