# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pic.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 50, 211, 141))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 321, 16))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 331, 16))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 10, 41, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        #self.label.setText(_translate("Form", "TextLabel"))
        pic = QPixmap('./new/1.jpg')
        self.label.setPixmap(pic)
        self.label.setScaledContents(True)  # 图片自适应LABEL大小
        self.label_2.setText(_translate("Form", "驾驶员疲劳图片集"))
        self.label_3.setText(_translate("Form", "驾驶员姓名：            李治江"))
        self.label_4.setText(_translate("Form", "拍摄时间：     2021年5月27日11点24分12秒"))
        self.pushButton.setText(_translate("Form", "X"))
        #self.pushButton.clicked()