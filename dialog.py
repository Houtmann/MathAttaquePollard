# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Pollard2
import Pollard3
import Pollard1
import cProfile


class MyDialog(object):

    def btnPollard3(self):
        if self.pushButton_3.isChecked():
            n = self.lineEdit.text()
            p = Pollard3.pollard3(int(n))
            print(p)


    def btnPollard2(self):
        if self.pushButton_2.isChecked():
            n = self.lineEdit.text()

            print(Pollard2.pollard2(int(n)))

    def btnPollard1(self):
        if self.pushButton_1.isChecked():
            n = self.lineEdit.text()

            print(Pollard1.pollard1(int(n)))


    def setupUi(self, MyDialog):
        MyDialog.setObjectName("MyDialog")
        MyDialog.resize(1513, 1230)
        self.centralwidget = QtWidgets.QWidget(MyDialog)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 130, 187, 57))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 230, 187, 57))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCheckable(True)



        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 330, 187, 57))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setCheckable(True)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(900, 140, 521, 39))
        self.lineEdit.setObjectName("lineEdit")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 140, 114, 33))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(780, 340, 114, 33))
        self.label_2.setObjectName("label_2")




        self.statusbar = QtWidgets.QStatusBar(MyDialog)
        self.statusbar.setObjectName("statusbar")


        self.retranslateUi(MyDialog)
        QtCore.QMetaObject.connectSlotsByName(MyDialog)

        self.pushButton.clicked.connect(self.btnPollard1)
        self.pushButton_2.clicked.connect(self.btnPollard2)

        self.pushButton_3.clicked.connect(self.btnPollard3)


    def retranslateUi(self, MyDialog):
        _translate = QtCore.QCoreApplication.translate
        MyDialog.setWindowTitle(_translate("MyDialog", "MyDialog"))
        self.pushButton.setText(_translate("MyDialog", "Pollard 1"))
        self.pushButton_2.setText(_translate("MyDialog", "Pollard 2"))
        self.pushButton_3.setText(_translate("MyDialog", "Pollard 3"))

        self.label.setText(_translate("MyDialog", "Nombre :"))

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from dialog import MyDialog

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = MyDialog()
        self.ui.setupUi(self)
        self.show()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())