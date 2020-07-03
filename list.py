# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_list(object):
    def setupUi(self, Dialog, list_id, list_id_time, list_id_status):
        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 315)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 471, 191))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 191, 17))
        self.label.setObjectName("label")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        i = 0
        for item, item_time, item_status in zip(list_id, list_id_time, list_id_status):
            self.listWidget.insertItem(i + 1, str(item) + " " + str(item_time) + " " + str(item_status) )
            i+=1

        f_maSV = open("student_list.txt")
        f_maSVs = f_maSV.read().splitlines()

        f_nameSV = open("student_list_name.txt")
        f_nameSVs = f_nameSV.read().splitlines()
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Attended Students"))


