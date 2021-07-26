# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warn_mode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 780)
        Form.setMinimumSize(QtCore.QSize(960, 780))
        Form.setMaximumSize(QtCore.QSize(960, 780))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(320, 40, 261, 81))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 40, 61, 61))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border-radius:25px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:4px double rgb(85, 0, 127);\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.widget_2.setObjectName("widget_2")
        self.tuoyan_le = QtWidgets.QLineEdit(self.widget_2)
        self.tuoyan_le.setGeometry(QtCore.QRect(160, 170, 581, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.tuoyan_le.setFont(font)
        self.tuoyan_le.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.tuoyan_le.setClearButtonEnabled(True)
        self.tuoyan_le.setObjectName("tuoyan_le")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(160, 100, 161, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(160, 250, 161, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.neixin_le = QtWidgets.QLineEdit(self.widget_2)
        self.neixin_le.setGeometry(QtCore.QRect(160, 330, 581, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.neixin_le.setFont(font)
        self.neixin_le.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.neixin_le.setClearButtonEnabled(True)
        self.neixin_le.setObjectName("neixin_le")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(160, 400, 161, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.xingdong_le = QtWidgets.QLineEdit(self.widget_2)
        self.xingdong_le.setGeometry(QtCore.QRect(160, 460, 581, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.xingdong_le.setFont(font)
        self.xingdong_le.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.xingdong_le.setClearButtonEnabled(True)
        self.xingdong_le.setObjectName("xingdong_le")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(380, 550, 181, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.morn_noon_le = QtWidgets.QLineEdit(self.widget_2)
        self.morn_noon_le.setGeometry(QtCore.QRect(410, 20, 81, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.morn_noon_le.setFont(font)
        self.morn_noon_le.setClearButtonEnabled(True)
        self.morn_noon_le.setObjectName("morn_noon_le")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(320, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.submit_warn)
        self.pushButton_2.clicked.connect(Form.exit_warn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "注意告警"))
        self.pushButton_2.setText(_translate("Form", "exit"))
        self.label_2.setText(_translate("Form", "拖延阻碍"))
        self.label_3.setText(_translate("Form", "内心假设"))
        self.label_4.setText(_translate("Form", "行动指南"))
        self.pushButton.setText(_translate("Form", "Warn"))
        self.label_5.setText(_translate("Form", "上/下"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
