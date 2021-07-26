# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Eword_into_mode.ui'
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
        self.label.setGeometry(QtCore.QRect(340, 40, 271, 71))
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
        self.label_2.setGeometry(QtCore.QRect(110, 140, 71, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(110, 390, 71, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.examplele = QtWidgets.QLineEdit(self.widget_2)
        self.examplele.setGeometry(QtCore.QRect(200, 380, 641, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.examplele.setFont(font)
        self.examplele.setStyleSheet("background-color: rgb(170, 208, 255);")
        self.examplele.setObjectName("examplele")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(410, 510, 161, 71))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.transle = QtWidgets.QLineEdit(self.widget_2)
        self.transle.setGeometry(QtCore.QRect(200, 260, 641, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.transle.setFont(font)
        self.transle.setStyleSheet("background-color: rgb(170, 208, 255);")
        self.transle.setObjectName("transle")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(110, 270, 71, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Wordle = QtWidgets.QLineEdit(self.widget_2)
        self.Wordle.setGeometry(QtCore.QRect(200, 130, 641, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.Wordle.setFont(font)
        self.Wordle.setStyleSheet("background-color: rgb(170, 208, 255);")
        self.Wordle.setObjectName("Wordle")
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.submit)
        self.pushButton_5.clicked.connect(Form.exit_wordbase)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", "exit"))
        self.label.setText(_translate("Form", "Wordbase"))
        self.comboBox.setItemText(0, _translate("Form", "write"))
        self.comboBox.setItemText(1, _translate("Form", "delete"))
        self.comboBox.setItemText(2, _translate("Form", "fix"))
        self.label_2.setText(_translate("Form", "单词："))
        self.label_3.setText(_translate("Form", "实例："))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.label_4.setText(_translate("Form", "注解："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
