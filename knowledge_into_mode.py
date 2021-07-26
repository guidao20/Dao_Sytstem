# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledge_into_mode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 780)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(145, 240, 158);")
        self.widget.setObjectName("widget")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 50, 51, 51))
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
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(320, 40, 271, 71))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(650, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: rgb(170, 135, 245);")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 111, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(410, 510, 161, 71))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.transle = QtWidgets.QLineEdit(self.widget_2)
        self.transle.setGeometry(QtCore.QRect(190, 230, 641, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.transle.setFont(font)
        self.transle.setStyleSheet("background-color: rgb(170, 208, 255);")
        self.transle.setObjectName("transle")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(70, 240, 71, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(70, 390, 71, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 380, 651, 71))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.Woldle = QtWidgets.QLineEdit(self.widget_2)
        self.Woldle.setGeometry(QtCore.QRect(190, 90, 641, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.Woldle.setFont(font)
        self.Woldle.setStyleSheet("background-color: rgb(170, 208, 255);")
        self.Woldle.setObjectName("Woldle")
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(Form.exit_knowbase)
        self.pushButton.clicked.connect(Form.submit)
        self.pushButton_2.clicked.connect(Form.open_img)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", "exit"))
        self.label.setText(_translate("Form", "Knowbase"))
        self.comboBox.setItemText(0, _translate("Form", "write"))
        self.comboBox.setItemText(1, _translate("Form", "delete"))
        self.comboBox.setItemText(2, _translate("Form", "fix"))
        self.label_2.setText(_translate("Form", "知识点："))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.label_4.setText(_translate("Form", "注解："))
        self.label_5.setText(_translate("Form", "图解："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
