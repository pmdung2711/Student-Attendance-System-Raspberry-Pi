# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_update(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(812, 461)
        Form.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 80, 461, 361))
        self.label.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineID = QtWidgets.QLineEdit(Form)
        self.lineID.setGeometry(QtCore.QRect(500, 200, 291, 41))
        self.lineID.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"font: 15pt \"Ubuntu\";")
        self.lineID.setObjectName("lineID")
        self.line_Name = QtWidgets.QLineEdit(Form)
        self.line_Name.setGeometry(QtCore.QRect(500, 290, 291, 41))
        self.line_Name.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"font: 15pt \"Ubuntu\";")
        self.line_Name.setObjectName("line_Name")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(500, 160, 67, 17))
        self.label_2.setStyleSheet("color: rgb(238, 238, 236);\n"
"font: 16pt \"Ubuntu\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(500, 260, 67, 17))
        self.label_3.setStyleSheet("color: rgb(238, 238, 236);\n"
"font: 16pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.import_bt = QtWidgets.QPushButton(Form)
        self.import_bt.setGeometry(QtCore.QRect(500, 370, 291, 31))
        self.import_bt.setStyleSheet("color: rgb(238, 238, 236);\n"
"font: 19pt \"Ubuntu\";")
        self.import_bt.setObjectName("import_bt")
        self.line_status = QtWidgets.QLineEdit(Form)
        self.line_status.setGeometry(QtCore.QRect(500, 110, 291, 41))
        self.line_status.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"font: 75 20pt \"Uroob\";\n"
"color: rgb(238, 238, 236);\n"
"background-color: rgb(46, 52, 54);\n"
"")
        self.line_status.setObjectName("line_status")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(500, 80, 91, 17))
        self.label_4.setStyleSheet("color: rgb(238, 238, 236);\n"
"font: 16pt \"Ubuntu\";")
        self.label_4.setObjectName("label_4")
        self.lineID_4 = QtWidgets.QLineEdit(Form)
        self.lineID_4.setGeometry(QtCore.QRect(20, 30, 461, 61))
        self.lineID_4.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"background-color: rgb(42, 63, 74);\n"
"font: 15pt \"Ubuntu\";\n"
"color:rgb(238, 238, 236)")
        self.lineID_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineID_4.setObjectName("lineID_4")
        self.exit_bt = QtWidgets.QPushButton(Form)
        self.exit_bt.setGeometry(QtCore.QRect(640, 30, 151, 31))
        self.exit_bt.setStyleSheet("color: rgb(238, 238, 236);\n"
"font: 19pt \"Ubuntu\";")
        self.exit_bt.setObjectName("exit_bt")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineID.setText(_translate("Form", "0"))
        self.line_Name.setText(_translate("Form", "0"))
        self.label_2.setText(_translate("Form", "ID"))
        self.label_3.setText(_translate("Form", "NAME"))
        self.import_bt.setText(_translate("Form", "IMPORT FACE"))
        self.line_status.setText(_translate("Form", " SYSTEM STATUS"))
        self.label_4.setText(_translate("Form", "STATUS"))
        self.lineID_4.setText(_translate("Form", "CAMERA "))
        self.exit_bt.setText(_translate("Form", "EXIT"))
