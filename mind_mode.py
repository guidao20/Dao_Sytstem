# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mind_mode.ui'
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
        self.widget.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(370, 30, 191, 81))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(48)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 0, 255);")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 30, 61, 61))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border-radius:25px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:4px double rgb(85, 0, 127);\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.widget_2.setObjectName("widget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 470, 131, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(26)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.want_le = QtWidgets.QLineEdit(self.widget_2)
        self.want_le.setGeometry(QtCore.QRect(170, 410, 561, 61))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(18)
        self.want_le.setFont(font)
        self.want_le.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color:rgb(255, 0, 0);")
        self.want_le.setClearButtonEnabled(True)
        self.want_le.setObjectName("want_le")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 480, 111, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(26)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(310, 10, 431, 111))
        self.widget_3.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.widget_3.setObjectName("widget_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 30, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(24)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 30, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(24)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(140, 40, 161, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(140, 170, 161, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setGeometry(QtCore.QRect(310, 140, 431, 111))
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.widget_4.setObjectName("widget_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 30, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(24)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 30, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(24)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setGeometry(QtCore.QRect(310, 270, 431, 111))
        self.widget_5.setStyleSheet("background-color:rgb(170, 170, 255)")
        self.widget_5.setObjectName("widget_5")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_13.setGeometry(QtCore.QRect(60, 30, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(24)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_14.setGeometry(QtCore.QRect(240, 30, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(24)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(140, 300, 161, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_12.setGeometry(QtCore.QRect(20, 550, 141, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"    border-radius:25px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:4px double rgb(85, 0, 127);\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_15.setGeometry(QtCore.QRect(800, 550, 141, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton {\n"
"    border-radius:25px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:4px double rgb(85, 0, 127);\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.exit_mind)
        self.pushButton_2.clicked.connect(Form.submit_want)
        self.pushButton_4.clicked.connect(Form.show_want)
        self.pushButton_5.clicked.connect(Form.life_run)
        self.pushButton_6.clicked.connect(Form.life_reset)
        self.pushButton_9.clicked.connect(Form.life_list)
        self.pushButton_10.clicked.connect(Form.life_list_show)
        self.pushButton_13.clicked.connect(Form.long_plan)
        self.pushButton_14.clicked.connect(Form.long_show)
        self.pushButton_12.clicked.connect(Form.enter_escape)
        self.pushButton_15.clicked.connect(Form.think_life)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Mind"))
        self.pushButton_3.setText(_translate("Form", "exit"))
        self.pushButton_2.setText(_translate("Form", "要去做"))
        self.pushButton_4.setText(_translate("Form", "show"))
        self.pushButton_5.setText(_translate("Form", "DUTY"))
        self.pushButton_6.setText(_translate("Form", "RESET"))
        self.label.setText(_translate("Form", "主要任务："))
        self.label_2.setText(_translate("Form", "生活清单："))
        self.pushButton_9.setText(_translate("Form", "MERGE"))
        self.pushButton_10.setText(_translate("Form", "SHOW"))
        self.pushButton_13.setText(_translate("Form", "Plan"))
        self.pushButton_14.setText(_translate("Form", "SHOW"))
        self.label_3.setText(_translate("Form", "长期安排："))
        self.pushButton_12.setText(_translate("Form", "escape"))
        self.pushButton_15.setText(_translate("Form", "think"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
