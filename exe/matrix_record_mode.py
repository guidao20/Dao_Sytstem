
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
        self.widget.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(200, 40, 591, 81))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 30, 61, 61))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border-radius:25px;\n"
"    color:rgb(255, 255, 255);\n"
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
        self.widget_2.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.widget_3.setFont(font)
        self.widget_3.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(160, 70, 201, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.system_le1 = QtWidgets.QLineEdit(self.widget_3)
        self.system_le1.setGeometry(QtCore.QRect(110, 180, 281, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.system_le1.setFont(font)
        self.system_le1.setStyleSheet("color: rgb(255, 255, 255);")
        self.system_le1.setClearButtonEnabled(True)
        self.system_le1.setObjectName("system_le1")
        self.system_le2 = QtWidgets.QLineEdit(self.widget_3)
        self.system_le2.setGeometry(QtCore.QRect(110, 310, 281, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.system_le2.setFont(font)
        self.system_le2.setStyleSheet("color: rgb(255, 255, 255);")
        self.system_le2.setClearButtonEnabled(True)
        self.system_le2.setObjectName("system_le2")
        self.system_le3 = QtWidgets.QLineEdit(self.widget_3)
        self.system_le3.setGeometry(QtCore.QRect(110, 440, 281, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.system_le3.setFont(font)
        self.system_le3.setStyleSheet("color: rgb(255, 255, 255);")
        self.system_le3.setClearButtonEnabled(True)
        self.system_le3.setObjectName("system_le3")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 530, 141, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 530, 141, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.widget_4.setObjectName("widget_4")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 201, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.function_le1 = QtWidgets.QLineEdit(self.widget_4)
        self.function_le1.setGeometry(QtCore.QRect(110, 180, 281, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.function_le1.setFont(font)
        self.function_le1.setStyleSheet("color: rgb(255, 255, 255);")
        self.function_le1.setClearButtonEnabled(True)
        self.function_le1.setObjectName("function_le1")
        self.function_le2 = QtWidgets.QLineEdit(self.widget_4)
        self.function_le2.setGeometry(QtCore.QRect(110, 310, 281, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.function_le2.setFont(font)
        self.function_le2.setStyleSheet("color: rgb(255, 255, 255);")
        self.function_le2.setClearButtonEnabled(True)
        self.function_le2.setObjectName("function_le2")
        self.function_le3 = QtWidgets.QLineEdit(self.widget_4)
        self.function_le3.setGeometry(QtCore.QRect(110, 440, 281, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.function_le3.setFont(font)
        self.function_le3.setStyleSheet("color: rgb(255, 255, 255);")
        self.function_le3.setClearButtonEnabled(True)
        self.function_le3.setObjectName("function_le3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 530, 141, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.widget_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(Form.exit_matrix_record)
        self.pushButton_3.clicked.connect(Form.submit_system)
        self.pushButton_4.clicked.connect(Form.submit_function)
        self.pushButton_6.clicked.connect(Form.explosion)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Matrix 辅助系统日志"))
        self.pushButton_5.setText(_translate("Form", "exit"))
        self.label_2.setText(_translate("Form", "系统升级"))
        self.pushButton_3.setText(_translate("Form", "提交"))
        self.pushButton_6.setText(_translate("Form", "炸裂"))
        self.label_3.setText(_translate("Form", "功能完善"))
        self.pushButton_4.setText(_translate("Form", "提交"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
