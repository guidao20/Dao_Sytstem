# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledge_search_mode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 777)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.widget.setObjectName("widget")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 20, 51, 51))
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
        self.label.setGeometry(QtCore.QRect(300, 20, 371, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(880, 30, 51, 51))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    border-radius:25px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:4px double rgb(85, 0, 127);\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_8 = QtWidgets.QWidget(self.widget_5)
        self.widget_8.setStyleSheet("background-color: rgb(170, 195, 167);")
        self.widget_8.setObjectName("widget_8")
        self.label_2 = QtWidgets.QLabel(self.widget_8)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 101, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Qle = QtWidgets.QLineEdit(self.widget_8)
        self.Qle.setGeometry(QtCore.QRect(140, 90, 581, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.Qle.setFont(font)
        self.Qle.setStyleSheet("background-color: rgb(170, 208, 255);")
        self.Qle.setClearButtonEnabled(True)
        self.Qle.setObjectName("Qle")
        self.label_3 = QtWidgets.QLabel(self.widget_8)
        self.label_3.setGeometry(QtCore.QRect(40, 360, 71, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser_trans = QtWidgets.QTextBrowser(self.widget_8)
        self.textBrowser_trans.setGeometry(QtCore.QRect(140, 210, 641, 411))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.textBrowser_trans.setFont(font)
        self.textBrowser_trans.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.textBrowser_trans.setObjectName("textBrowser_trans")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 90, 91, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_4.setGeometry(QtCore.QRect(840, 310, 91, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_7.setGeometry(QtCore.QRect(840, 460, 91, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.radioButton = QtWidgets.QRadioButton(self.widget_8)
        self.radioButton.setGeometry(QtCore.QRect(730, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(20)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_3.addWidget(self.widget_8)
        self.horizontalLayout.addWidget(self.widget_5)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.verticalLayout_2.setStretch(0, 7)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 13)

        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(Form.exit_search_know)
        self.pushButton_6.clicked.connect(Form.enter_into_know)
        self.pushButton_2.clicked.connect(Form.search_result)
        self.pushButton_4.clicked.connect(Form.show_result)
        self.pushButton_7.clicked.connect(Form.clear_box)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", "exit"))
        self.label.setText(_translate("Form", "Search Knowledge"))
        self.pushButton_6.setText(_translate("Form", "into"))
        self.label_2.setText(_translate("Form", "输入："))
        self.label_3.setText(_translate("Form", "知识："))
        self.pushButton_2.setText(_translate("Form", "查询"))
        self.pushButton_4.setText(_translate("Form", "显示"))
        self.pushButton_7.setText(_translate("Form", "清除"))
        self.radioButton.setText(_translate("Form", "all"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
