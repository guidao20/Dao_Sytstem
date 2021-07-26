# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bat_mode.ui'
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
        self.widget.setStyleSheet("background-color: rgb(255, 217, 239);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(340, 20, 271, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 831, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(85, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.exit_bat_btn = QtWidgets.QPushButton(self.widget)
        self.exit_bat_btn.setGeometry(QtCore.QRect(20, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(16)
        self.exit_bat_btn.setFont(font)
        self.exit_bat_btn.setStyleSheet("QPushButton {\n"
"    border-radius:25px;\n"
"    color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:4px double rgb(85, 0, 127);\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"")
        self.exit_bat_btn.setObjectName("exit_bat_btn")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: rgb(252, 255, 221);")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setStyleSheet("background-color: rgb(217, 252, 255);")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(100, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setGeometry(QtCore.QRect(30, 70, 101, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 170, 127);\n"
"    color:rgb(37, 59, 255);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 70, 101, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 170, 127);\n"
"    color:rgb(37, 59, 255);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 150, 101, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 170, 127);\n"
"    color:rgb(37, 59, 255);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 150, 101, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 170, 127);\n"
"    color:rgb(37, 59, 255);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 230, 171, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 170, 127);\n"
"    color:rgb(37, 59, 255);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 300, 101, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 170, 127);\n"
"    color:rgb(37, 59, 255);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_18 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_18.setGeometry(QtCore.QRect(30, 380, 101, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 170, 127);\n"
"    color:rgb(37, 59, 255);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_19.setGeometry(QtCore.QRect(180, 300, 101, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 170, 127);\n"
"    color:rgb(37, 59, 255);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_23 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_23.setGeometry(QtCore.QRect(180, 380, 101, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 170, 127);\n"
"    color:rgb(37, 59, 255);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(24)
        self.widget_4.setFont(font)
        self.widget_4.setStyleSheet("background-color: rgb(232, 255, 222);")
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(90, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setGeometry(QtCore.QRect(90, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 70, 121, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color:rgb(176, 215, 255);\n"
"    color: rgb(255, 0, 127);;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 70, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color:rgb(176, 215, 255);\n"
"    color: rgb(255, 0, 127);;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 150, 191, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    background-color:rgb(176, 215, 255);\n"
"    color: rgb(255, 0, 127);;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_20 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_20.setGeometry(QtCore.QRect(10, 240, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton {\n"
"    background-color:rgb(176, 215, 255);\n"
"    color: rgb(255, 0, 127);;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_21.setGeometry(QtCore.QRect(170, 240, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton {\n"
"    background-color:rgb(176, 215, 255);\n"
"    color: rgb(255, 0, 127);;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_22.setGeometry(QtCore.QRect(10, 310, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("QPushButton {\n"
"    background-color:rgb(176, 215, 255);\n"
"    color: rgb(255, 0, 127);;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_24 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_24.setGeometry(QtCore.QRect(170, 310, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(18)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("QPushButton {\n"
"    background-color:rgb(176, 215, 255);\n"
"    color: rgb(255, 0, 127);;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:rgb(182, 182, 182)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 148, 105);\n"
"}")
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setStyleSheet("background-color: rgb(195, 193, 255);")
        self.widget_5.setObjectName("widget_5")
        self.label_6 = QtWidgets.QLabel(self.widget_5)
        self.label_6.setGeometry(QtCore.QRect(110, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.widget_5)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.exit_bat_btn.clicked.connect(Form.exit_bat_show)
        self.pushButton.clicked.connect(Form.run_pycharm)
        self.pushButton_2.clicked.connect(Form.run_v2rayn)
        self.pushButton_3.clicked.connect(Form.run_VMware)
        self.pushButton_4.clicked.connect(Form.run_auto)
        self.pushButton_5.clicked.connect(Form.run_anjian)
        self.pushButton_8.clicked.connect(Form.run_worldplay)
        self.pushButton_7.clicked.connect(Form.run_advemotion)
        self.pushButton_6.clicked.connect(Form.run_habit)
        self.pushButton_9.clicked.connect(Form.run_wechat)
        self.pushButton_18.clicked.connect(Form.run_google)
        self.pushButton_19.clicked.connect(Form.run_music)
        self.pushButton_20.clicked.connect(Form.run_dao)
        self.pushButton_21.clicked.connect(Form.run_make)
        self.pushButton_22.clicked.connect(Form.run_reguplan)
        self.pushButton_23.clicked.connect(Form.run_youdao)
        self.pushButton_24.clicked.connect(Form.deal_system_rabbit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "BAT批处理命令"))
        self.label_2.setText(_translate("Form", "bat文件是dos下的批处理文件,dos是磁盘操作系统的缩写，是个人计算机上的一类操作系统"))
        self.exit_bat_btn.setText(_translate("Form", "exit"))
        self.label_3.setText(_translate("Form", "启动软件"))
        self.pushButton.setText(_translate("Form", "Pycharm"))
        self.pushButton_2.setText(_translate("Form", "V2rayN"))
        self.pushButton_3.setText(_translate("Form", "VMware"))
        self.pushButton_4.setText(_translate("Form", "Auto.js"))
        self.pushButton_5.setText(_translate("Form", "按键精灵"))
        self.pushButton_9.setText(_translate("Form", "腾讯"))
        self.pushButton_18.setText(_translate("Form", "Google"))
        self.pushButton_19.setText(_translate("Form", "QQ音乐"))
        self.pushButton_23.setText(_translate("Form", "有道云"))
        self.label_5.setText(_translate("Form", "打开程序"))
        self.pushButton_6.setText(_translate("Form", "Habit"))
        self.pushButton_7.setText(_translate("Form", "AdvEmotion"))
        self.pushButton_8.setText(_translate("Form", "Wordplay_pygame"))
        self.pushButton_20.setText(_translate("Form", "Dao_System"))
        self.pushButton_21.setText(_translate("Form", "Make_System"))
        self.pushButton_22.setText(_translate("Form", "Reguplan"))
        self.pushButton_24.setText(_translate("Form", "Garbage"))
        self.label_6.setText(_translate("Form", "命令学习"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
