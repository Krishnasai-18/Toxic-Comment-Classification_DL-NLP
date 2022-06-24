# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 11:58:23 2020

@author: User-Pc
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuestionPair.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 463)
        
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(240, 60, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 160, 175, 16))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        font = QtGui.QFont()
        font.setPointSize(10)
       
        self.lineEdit1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit1.setGeometry(QtCore.QRect(310, 160, 300, 20))
        self.lineEdit1.setObjectName("lineEdit1")
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 225, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 275, 210, 50))
        self.label_3.setFont(font) 
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 300, 210, 50))
        self.label_4.setFont(font) 
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(200, 325, 210, 50))
        self.label_5.setFont(font)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(15, 380, 700, 50))
        self.label_6.setFont(font)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "Toxic Comment Classfication"))
        self.label_2.setText(_translate("Dialog", "Enter the comment"))
        self.label_3.setText(_translate("Dialog", ""))
        self.label_4.setText(_translate("Dialog", ""))
        self.label_5.setText(_translate("Dialog", ""))
        self.label_6.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "Classify"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

