# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'escape_data_mode.ui'
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
        self.label.setGeometry(QtCore.QRect(360, 40, 201, 81))
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
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(300, 30, 101, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(130, 120, 111, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.event_le = QtWidgets.QLineEdit(self.widget_2)
        self.event_le.setGeometry(QtCore.QRect(260, 120, 581, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.event_le.setFont(font)
        self.event_le.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.event_le.setClearButtonEnabled(True)
        self.event_le.setObjectName("event_le")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(140, 200, 91, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.feel_le = QtWidgets.QLineEdit(self.widget_2)
        self.feel_le.setGeometry(QtCore.QRect(260, 200, 581, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.feel_le.setFont(font)
        self.feel_le.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.feel_le.setClearButtonEnabled(True)
        self.feel_le.setObjectName("feel_le")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 280, 171, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 280, 151, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(430, 30, 221, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser.setGeometry(QtCore.QRect(130, 350, 741, 261))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 248, 147);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(Form.exit_escape)
        self.pushButton_4.clicked.connect(Form.Record)
        self.pushButton_3.clicked.connect(Form.fig)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Elusion"))
        self.pushButton_5.setText(_translate("Form", "exit"))
        self.label_2.setText(_translate("Form", "Label："))
        self.label_3.setText(_translate("Form", "Event："))
        self.label_4.setText(_translate("Form", "Feel："))
        self.pushButton_3.setText(_translate("Form", "show"))
        self.pushButton_4.setText(_translate("Form", "Record"))
        self.comboBox.setItemText(0, _translate("Form", "pressure"))
        self.comboBox.setItemText(1, _translate("Form", "nprofit"))
        self.comboBox.setItemText(2, _translate("Form", "guilt"))
        self.comboBox.setItemText(3, _translate("Form", "rebellion"))
        self.comboBox.setItemText(4, _translate("Form", "nenergy"))
        self.comboBox.setItemText(5, _translate("Form", "mess"))
        self.comboBox.setItemText(6, _translate("Form", "confused"))
        self.comboBox.setItemText(7, _translate("Form", "fear"))
        self.comboBox.setItemText(8, _translate("Form", "defeat"))
        self.comboBox.setItemText(9, _translate("Form", "nrespond"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
