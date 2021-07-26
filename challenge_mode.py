# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'challenge_mode.ui'
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
        self.label.setGeometry(QtCore.QRect(320, 40, 311, 81))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 50, 61, 61))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border-radius:25px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:4px double rgb(85, 0, 127);\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.widget_2.setObjectName("widget_2")
        self.Reason_le = QtWidgets.QLineEdit(self.widget_2)
        self.Reason_le.setGeometry(QtCore.QRect(150, 130, 581, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.Reason_le.setFont(font)
        self.Reason_le.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.Reason_le.setClearButtonEnabled(True)
        self.Reason_le.setObjectName("Reason_le")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(150, 50, 301, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(160, 220, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Necessity_le = QtWidgets.QLineEdit(self.widget_2)
        self.Necessity_le.setGeometry(QtCore.QRect(160, 290, 581, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.Necessity_le.setFont(font)
        self.Necessity_le.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.Necessity_le.setClearButtonEnabled(True)
        self.Necessity_le.setObjectName("Necessity_le")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(160, 370, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Action_le = QtWidgets.QLineEdit(self.widget_2)
        self.Action_le.setGeometry(QtCore.QRect(160, 440, 581, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.Action_le.setFont(font)
        self.Action_le.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Action_le.setClearButtonEnabled(True)
        self.Action_le.setObjectName("Action_le")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 550, 181, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 550, 181, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.log)
        self.pushButton_4.clicked.connect(Form.Record)
        self.pushButton_5.clicked.connect(Form.exit_challenge)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Growing"))
        self.pushButton_5.setText(_translate("Form", "exit"))
        self.label_2.setText(_translate("Form", "Defination"))
        self.label_3.setText(_translate("Form", "Analysis"))
        self.label_4.setText(_translate("Form", "Solution"))
        self.pushButton_3.setText(_translate("Form", "Log"))
        self.pushButton_4.setText(_translate("Form", "Record"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
