# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paper_create_mode.ui'
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
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 960, 780))
        self.widget.setMinimumSize(QtCore.QSize(960, 780))
        self.widget.setMaximumSize(QtCore.QSize(960, 780))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(350, 30, 241, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 127);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(50, 30, 61, 61))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-radius:25px;\n"
"    color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:4px double rgb(85, 0, 127);\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 0, 0, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setStyleSheet("background-color: rgb(244, 188, 255);")
        self.widget_7.setObjectName("widget_7")
        self.gridLayout.addWidget(self.widget_7, 1, 1, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setStyleSheet("background-color: rgb(255, 254, 199);")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout.addWidget(self.widget_6, 1, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.widget_5.setObjectName("widget_5")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 271, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 100, 181, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 0, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 100, 181, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 0, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.widget_5, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.verticalLayout.addWidget(self.widget_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.paper_program)
        self.pushButton_3.clicked.connect(Form.paper_create)
        self.pushButton.clicked.connect(Form.exit_create_pane)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "论文创作中"))
        self.pushButton.setText(_translate("Form", "exit"))
        self.label_2.setText(_translate("Form", "Region_Emotion"))
        self.pushButton_2.setText(_translate("Form", " 程序编写"))
        self.pushButton_3.setText(_translate("Form", "论文创作"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
