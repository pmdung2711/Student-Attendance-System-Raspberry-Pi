# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        Form.setSizeIncrement(QtCore.QSize(1024, 600))
        Form.setStyleSheet("color: rgb(42, 63, 74);\n"
"background-color: rgb(238, 238, 236);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(620, 410, 361, 41))
        self.label_2.setStyleSheet("color: rgb(42, 63, 74);")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(690, 420, 291, 21))
        self.label_5.setStyleSheet("color: rgb(42, 63, 74);\n"
"font: 57 14pt \"Ubuntu\";")
        self.label_5.setObjectName("label_5")
        self.result_bt = QtWidgets.QPushButton(Form)
        self.result_bt.setGeometry(QtCore.QRect(800, 480, 191, 41))
        self.result_bt.setStyleSheet("font: 11pt \"Ubuntu\";\n"
"color: rgb(85, 87, 83)")
        self.result_bt.setObjectName("result_bt")
        self.label_history = QtWidgets.QLabel(Form)
        self.label_history.setGeometry(QtCore.QRect(610, 90, 381, 31))
        self.label_history.setStyleSheet("font: 57 16pt \"Ubuntu\";\n"
"background-color: rgb(42, 63, 74);\n"
"color: rgb(238, 238, 236);")
        self.label_history.setAlignment(QtCore.Qt.AlignCenter)
        self.label_history.setObjectName("label_history")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(610, 110, 381, 391))
        self.listView.setStyleSheet("")
        self.listView.setObjectName("listView")
        self.result_bt_2 = QtWidgets.QPushButton(Form)
        self.result_bt_2.setGeometry(QtCore.QRect(610, 480, 191, 41))
        self.result_bt_2.setStyleSheet("font: 11pt \"Ubuntu\";\n"
"color: rgb(85, 87, 83)")
        self.result_bt_2.setObjectName("result_bt_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(620, 440, 361, 41))
        self.label_3.setStyleSheet("color: rgb(42, 63, 74);")
        self.label_3.setObjectName("label_3")
        self.label_class_info = QtWidgets.QLabel(Form)
        self.label_class_info.setGeometry(QtCore.QRect(610, 50, 381, 31))
        self.label_class_info.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-color: rgb(46, 52, 54);")
        self.label_class_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_class_info.setObjectName("label_class_info")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 561, 51))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(42, 63, 74);\n"
"color: rgb(238, 238, 236);\n"
"font: 18pt \"Ubuntu\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setGeometry(QtCore.QRect(140, 480, 321, 41))
        self.control_bt.setStyleSheet("font: 11pt \"Ubuntu\";\n"
"font: 17pt \"Ubuntu\";\n"
"color: rgb(42, 63, 74);")
        self.control_bt.setObjectName("control_bt")
        self.exit_bt = QtWidgets.QPushButton(Form)
        self.exit_bt.setGeometry(QtCore.QRect(780, 20, 211, 25))
        self.exit_bt.setStyleSheet("color: rgb(85, 87, 83)")
        self.exit_bt.setObjectName("exit_bt")
        self.teacher_bt = QtWidgets.QPushButton(Form)
        self.teacher_bt.setGeometry(QtCore.QRect(420, 530, 141, 41))
        self.teacher_bt.setStyleSheet("font: 11pt \"Ubuntu\";\n"
"color: rgb(85, 87, 83)")
        self.teacher_bt.setObjectName("teacher_bt")
        self.system_status = QtWidgets.QLabel(Form)
        self.system_status.setGeometry(QtCore.QRect(120, 10, 171, 31))
        self.system_status.setStyleSheet("color: rgb(42, 63, 74);\n"
"font: 16pt \"Ubuntu\";")
        self.system_status.setObjectName("system_status")
        self.label_info = QtWidgets.QLabel(Form)
        self.label_info.setGeometry(QtCore.QRect(610, 20, 161, 31))
        self.label_info.setStyleSheet("font: 57 16pt \"Ubuntu\";\n"
"color: rgb(85, 87, 83);")
        self.label_info.setObjectName("label_info")
        self.class_bt = QtWidgets.QPushButton(Form)
        self.class_bt.setGeometry(QtCore.QRect(240, 530, 141, 41))
        self.class_bt.setStyleSheet("font: 11pt \"Ubuntu\";\n"
"color: rgb(85, 87, 83)")
        self.class_bt.setObjectName("class_bt")
        self.import_bt = QtWidgets.QPushButton(Form)
        self.import_bt.setGeometry(QtCore.QRect(50, 530, 141, 41))
        self.import_bt.setStyleSheet("font: 11pt \"Ubuntu\";\n"
"color: rgb(85, 87, 83)")
        self.import_bt.setObjectName("import_bt")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(20, 60, 561, 441))
        self.image_label.setStyleSheet("border-color: rgb(42, 63, 74);\n"
"background-color: rgb(211, 215, 207);")
        self.image_label.setObjectName("image_label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(690, 450, 201, 16))
        self.label_4.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font: 57 16pt \"Ubuntu\";\n"
"color: rgb(42, 63, 74);\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(620, 130, 351, 281))
        self.label_6.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.label_6.setObjectName("label_6")
        self.labelx = QtWidgets.QLabel(Form)
        self.labelx.setGeometry(QtCore.QRect(280, 10, 161, 31))
        self.labelx.setStyleSheet("background-color: rgb(211, 215, 207);\n"
"border-color: rgb(32, 74, 135);\n"
"font: 19pt \"Ubuntu\";")
        self.labelx.setAlignment(QtCore.Qt.AlignCenter)
        self.labelx.setObjectName("labelx")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(590, 530, 611, 61))
        self.label_8.setStyleSheet("color: rgb(42, 63, 74);")
        self.label_8.setObjectName("label_8")
        self.listView.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_class_info.raise_()
        self.label_8.raise_()
        self.image_label.raise_()
        self.result_bt.raise_()
        self.label_history.raise_()
        self.result_bt_2.raise_()
        self.label.raise_()
        self.control_bt.raise_()
        self.exit_bt.raise_()
        self.teacher_bt.raise_()
        self.system_status.raise_()
        self.label_info.raise_()
        self.class_bt.raise_()
        self.import_bt.raise_()
        self.label_6.raise_()
        self.labelx.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Project: Student Attendance System"))
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "  MSSV:"))
        self.result_bt.setText(_translate("Form", "View History"))
        self.label_history.setText(_translate("Form", "<html><head/><body><p>Result</p></body></html>"))
        self.result_bt_2.setText(_translate("Form", "Delete"))
        self.label_3.setText(_translate("Form", "  NAME:"))
        self.label_class_info.setText(_translate("Form", "Đồ án LTHT & VDK"))
        self.control_bt.setText(_translate("Form", "Start Recognition"))
        self.exit_bt.setText(_translate("Form", "End System"))
        self.teacher_bt.setText(_translate("Form", "Teacher"))
        self.system_status.setText(_translate("Form", "<html><head/><body><p>Remaining Time</p></body></html>"))
        self.label_info.setText(_translate("Form", "<html><head/><body><p>Class Information</p></body></html>"))
        self.class_bt.setText(_translate("Form", "Class Info"))
        self.import_bt.setText(_translate("Form", "Import"))
        self.image_label.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.labelx.setText(_translate("Form", "TIME"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">Group 34:</span><span style=\" font-size:14pt; vertical-align:sub;\"> Ho Duy Long - Pham Thi Nguyet - Ngo Thi Canh - Pham Manh Dung</span></p><p><span style=\" font-size:14pt; vertical-align:sub;\"/><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">Teacher: </span><span style=\" font-size:14pt; vertical-align:sub;\">Ninh Khanh Duy</span></p></body></html>"))
