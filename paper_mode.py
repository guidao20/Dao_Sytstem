# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paper_mode.ui'
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
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(12)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(350, 20, 221, 91))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 30, 61, 61))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border-radius:25px;\n"
"    color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:4px double rgb(85, 0, 127);\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(890, 40, 61, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(36)
        self.widget_3.setFont(font)
        self.widget_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.widget_3.setObjectName("widget_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 20, 191, 71))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setGeometry(QtCore.QRect(20, 100, 431, 111))
        self.widget_5.setObjectName("widget_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_8.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_9.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setGeometry(QtCore.QRect(330, 110, 431, 111))
        self.widget_7.setObjectName("widget_7")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_14.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_15.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_16.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.widget_8 = QtWidgets.QWidget(self.widget_7)
        self.widget_8.setGeometry(QtCore.QRect(370, 100, 431, 111))
        self.widget_8.setObjectName("widget_8")
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_17.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_18.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_19.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setGeometry(QtCore.QRect(430, 60, 431, 111))
        self.widget_6.setObjectName("widget_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_11.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_13.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.widget_10 = QtWidgets.QWidget(self.widget_6)
        self.widget_10.setGeometry(QtCore.QRect(330, 110, 431, 111))
        self.widget_10.setObjectName("widget_10")
        self.pushButton_23 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_23.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_24.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_25.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setObjectName("pushButton_25")
        self.widget_13 = QtWidgets.QWidget(self.widget_10)
        self.widget_13.setGeometry(QtCore.QRect(370, 100, 431, 111))
        self.widget_13.setObjectName("widget_13")
        self.pushButton_32 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_32.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_34 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_34.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_35.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setObjectName("pushButton_35")
        self.widget_9 = QtWidgets.QWidget(self.widget_3)
        self.widget_9.setGeometry(QtCore.QRect(50, 490, 401, 91))
        self.widget_9.setObjectName("widget_9")
        self.pushButton_20 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_20.setGeometry(QtCore.QRect(0, 20, 61, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("color: rgb(0, 0, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_21.setGeometry(QtCore.QRect(100, 20, 61, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("color: rgb(0, 0, 255);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_22.setGeometry(QtCore.QRect(190, 20, 81, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("color: rgb(0, 0, 255);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.widget_11 = QtWidgets.QWidget(self.widget_9)
        self.widget_11.setGeometry(QtCore.QRect(330, 110, 431, 111))
        self.widget_11.setObjectName("widget_11")
        self.pushButton_26 = QtWidgets.QPushButton(self.widget_11)
        self.pushButton_26.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.widget_11)
        self.pushButton_27.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.widget_11)
        self.pushButton_28.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setObjectName("pushButton_28")
        self.widget_12 = QtWidgets.QWidget(self.widget_11)
        self.widget_12.setGeometry(QtCore.QRect(370, 100, 431, 111))
        self.widget_12.setObjectName("widget_12")
        self.pushButton_29 = QtWidgets.QPushButton(self.widget_12)
        self.pushButton_29.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.widget_12)
        self.pushButton_30.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.widget_12)
        self.pushButton_31.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_33 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_33.setGeometry(QtCore.QRect(300, 20, 91, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("color: rgb(170, 0, 255);")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 220, 191, 71))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 255);")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget_14 = QtWidgets.QWidget(self.widget_3)
        self.widget_14.setGeometry(QtCore.QRect(30, 290, 431, 111))
        self.widget_14.setObjectName("widget_14")
        self.pushButton_36 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_36.setGeometry(QtCore.QRect(10, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("color: rgb(0, 0, 255);")
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_37.setGeometry(QtCore.QRect(150, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet("color: rgb(0, 0, 255);")
        self.pushButton_37.setObjectName("pushButton_37")
        self.widget_15 = QtWidgets.QWidget(self.widget_14)
        self.widget_15.setGeometry(QtCore.QRect(330, 110, 431, 111))
        self.widget_15.setObjectName("widget_15")
        self.pushButton_39 = QtWidgets.QPushButton(self.widget_15)
        self.pushButton_39.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.widget_15)
        self.pushButton_40.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.widget_15)
        self.pushButton_41.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setObjectName("pushButton_41")
        self.widget_16 = QtWidgets.QWidget(self.widget_15)
        self.widget_16.setGeometry(QtCore.QRect(370, 100, 431, 111))
        self.widget_16.setObjectName("widget_16")
        self.pushButton_42 = QtWidgets.QPushButton(self.widget_16)
        self.pushButton_42.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.widget_16)
        self.pushButton_43.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.widget_16)
        self.pushButton_44.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setObjectName("pushButton_44")
        self.widget_17 = QtWidgets.QWidget(self.widget_14)
        self.widget_17.setGeometry(QtCore.QRect(430, 60, 431, 111))
        self.widget_17.setObjectName("widget_17")
        self.pushButton_52 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton_52.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_54 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton_54.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_55 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton_55.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_55.setObjectName("pushButton_55")
        self.widget_18 = QtWidgets.QWidget(self.widget_17)
        self.widget_18.setGeometry(QtCore.QRect(330, 110, 431, 111))
        self.widget_18.setObjectName("widget_18")
        self.pushButton_56 = QtWidgets.QPushButton(self.widget_18)
        self.pushButton_56.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.widget_18)
        self.pushButton_57.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_57.setFont(font)
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.widget_18)
        self.pushButton_58.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setObjectName("pushButton_58")
        self.widget_19 = QtWidgets.QWidget(self.widget_18)
        self.widget_19.setGeometry(QtCore.QRect(370, 100, 431, 111))
        self.widget_19.setObjectName("widget_19")
        self.pushButton_59 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_59.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_59.setFont(font)
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_60 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_60.setGeometry(QtCore.QRect(160, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_60.setFont(font)
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_61 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_61.setGeometry(QtCore.QRect(300, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_61.setFont(font)
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_38 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_38.setGeometry(QtCore.QRect(290, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setStyleSheet("color: rgb(0, 0, 255);")
        self.pushButton_38.setObjectName("pushButton_38")
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.widget_4.setObjectName("widget_4")
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 624))
        self.label.setStyleSheet("border-image: url(:/program_img/picture/Paper_timeline.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_12.setGeometry(QtCore.QRect(186, 148, 118, 118))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(18)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"    border-radius:50px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_45 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_45.setGeometry(QtCore.QRect(186, 474, 121, 121))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(18)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setStyleSheet("QPushButton {\n"
"    border-radius:50px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_46.setGeometry(QtCore.QRect(337, 148, 118, 118))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(18)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setStyleSheet("QPushButton {\n"
"    border-radius:50px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_48 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_48.setGeometry(QtCore.QRect(35, 148, 118, 118))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(18)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setStyleSheet("QPushButton {\n"
"    border-radius:50px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_48.setFlat(False)
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_49.setGeometry(QtCore.QRect(186, 309, 118, 118))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(18)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setStyleSheet("QPushButton {\n"
"    border-radius:50px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_50.setGeometry(QtCore.QRect(34, 309, 118, 118))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(18)
        self.pushButton_50.setFont(font)
        self.pushButton_50.setStyleSheet("QPushButton {\n"
"    border-radius:50px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_51.setGeometry(QtCore.QRect(337, 309, 118, 118))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(18)
        self.pushButton_51.setFont(font)
        self.pushButton_51.setStyleSheet("QPushButton {\n"
"    border-radius:50px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_53 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_53.setGeometry(QtCore.QRect(34, 474, 118, 118))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(18)
        self.pushButton_53.setFont(font)
        self.pushButton_53.setStyleSheet("QPushButton {\n"
"    border-radius:50px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 20, 191, 71))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_47 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_47.setGeometry(QtCore.QRect(337, 474, 121, 121))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(18)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setStyleSheet("QPushButton {\n"
"    border-radius:50px;\n"
"    color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_47.setObjectName("pushButton_47")
        self.number_le = QtWidgets.QLineEdit(self.widget_4)
        self.number_le.setGeometry(QtCore.QRect(200, 90, 31, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.number_le.setFont(font)
        self.number_le.setStyleSheet("background-color: rgb(251, 229, 214);")
        self.number_le.setObjectName("number_le")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setGeometry(QtCore.QRect(160, 90, 31, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgb(251, 229, 224);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setGeometry(QtCore.QRect(240, 90, 91, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(251, 229, 214);")
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.pushButton_48.raise_()
        self.pushButton_12.raise_()
        self.pushButton_45.raise_()
        self.pushButton_46.raise_()
        self.pushButton_49.raise_()
        self.pushButton_50.raise_()
        self.pushButton_51.raise_()
        self.pushButton_53.raise_()
        self.pushButton_4.raise_()
        self.pushButton_47.raise_()
        self.number_le.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.horizontalLayout.addWidget(self.widget_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(Form.paper_exit)
        self.pushButton_7.clicked.connect(Form.collection)
        self.pushButton_8.clicked.connect(Form.lookup)
        self.pushButton_48.clicked.connect(Form.preparation)
        self.pushButton_12.clicked.connect(Form.idea_generation)
        self.pushButton_46.clicked.connect(Form.technical_proposal)
        self.pushButton_50.clicked.connect(Form.fix_error)
        self.pushButton_49.clicked.connect(Form.paper_writing)
        self.pushButton_51.clicked.connect(Form.paper_program)
        self.pushButton_53.clicked.connect(Form.journal_contribution)
        self.pushButton_45.clicked.connect(Form.review_interaction)
        self.pushButton_47.clicked.connect(Form.aftertreatment)
        self.pushButton_9.clicked.connect(Form.Contribute)
        self.pushButton_36.clicked.connect(Form.support_writing)
        self.pushButton_37.clicked.connect(Form.support_English)
        self.pushButton_6.clicked.connect(Form.show_progressbar)
        self.pushButton_20.clicked.connect(Form.AI_math)
        self.pushButton_21.clicked.connect(Form.Life_math)
        self.pushButton_22.clicked.connect(Form.Model_math)
        self.pushButton_33.clicked.connect(Form.English_Friends)
        self.pushButton_37.clicked.connect(Form.show_english)
        self.pushButton_38.clicked.connect(Form.knowledge)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "论文世界"))
        self.pushButton_5.setText(_translate("Form", "exit"))
        self.pushButton_6.setText(_translate("Form", "bar"))
        self.pushButton_2.setText(_translate("Form", "论文查阅"))
        self.pushButton_7.setText(_translate("Form", "收藏"))
        self.pushButton_8.setText(_translate("Form", "浏览"))
        self.pushButton_9.setText(_translate("Form", "整理"))
        self.pushButton_14.setText(_translate("Form", "收藏"))
        self.pushButton_15.setText(_translate("Form", "浏览"))
        self.pushButton_16.setText(_translate("Form", "整理"))
        self.pushButton_17.setText(_translate("Form", "收藏"))
        self.pushButton_18.setText(_translate("Form", "浏览"))
        self.pushButton_19.setText(_translate("Form", "整理"))
        self.pushButton_10.setText(_translate("Form", "收藏"))
        self.pushButton_11.setText(_translate("Form", "浏览"))
        self.pushButton_13.setText(_translate("Form", "整理"))
        self.pushButton_23.setText(_translate("Form", "收藏"))
        self.pushButton_24.setText(_translate("Form", "浏览"))
        self.pushButton_25.setText(_translate("Form", "整理"))
        self.pushButton_32.setText(_translate("Form", "收藏"))
        self.pushButton_34.setText(_translate("Form", "浏览"))
        self.pushButton_35.setText(_translate("Form", "整理"))
        self.pushButton_20.setText(_translate("Form", "AI"))
        self.pushButton_21.setText(_translate("Form", "Life"))
        self.pushButton_22.setText(_translate("Form", "Model"))
        self.pushButton_26.setText(_translate("Form", "收藏"))
        self.pushButton_27.setText(_translate("Form", "浏览"))
        self.pushButton_28.setText(_translate("Form", "整理"))
        self.pushButton_29.setText(_translate("Form", "收藏"))
        self.pushButton_30.setText(_translate("Form", "浏览"))
        self.pushButton_31.setText(_translate("Form", "整理"))
        self.pushButton_33.setText(_translate("Form", "Friends"))
        self.pushButton_3.setText(_translate("Form", "论文支撑"))
        self.pushButton_36.setText(_translate("Form", "写作"))
        self.pushButton_37.setText(_translate("Form", "英语"))
        self.pushButton_39.setText(_translate("Form", "收藏"))
        self.pushButton_40.setText(_translate("Form", "浏览"))
        self.pushButton_41.setText(_translate("Form", "整理"))
        self.pushButton_42.setText(_translate("Form", "收藏"))
        self.pushButton_43.setText(_translate("Form", "浏览"))
        self.pushButton_44.setText(_translate("Form", "整理"))
        self.pushButton_52.setText(_translate("Form", "收藏"))
        self.pushButton_54.setText(_translate("Form", "浏览"))
        self.pushButton_55.setText(_translate("Form", "整理"))
        self.pushButton_56.setText(_translate("Form", "收藏"))
        self.pushButton_57.setText(_translate("Form", "浏览"))
        self.pushButton_58.setText(_translate("Form", "整理"))
        self.pushButton_59.setText(_translate("Form", "收藏"))
        self.pushButton_60.setText(_translate("Form", "浏览"))
        self.pushButton_61.setText(_translate("Form", "整理"))
        self.pushButton_38.setText(_translate("Form", "知识"))
        self.pushButton_12.setText(_translate("Form", "想法锻造"))
        self.pushButton_45.setText(_translate("Form", "评审交互"))
        self.pushButton_46.setText(_translate("Form", "技术方案"))
        self.pushButton_48.setText(_translate("Form", "前期准备"))
        self.pushButton_49.setText(_translate("Form", "论文写作"))
        self.pushButton_50.setText(_translate("Form", "修正错误"))
        self.pushButton_51.setText(_translate("Form", "编程实验"))
        self.pushButton_53.setText(_translate("Form", "期刊投稿"))
        self.pushButton_4.setText(_translate("Form", "论文创作"))
        self.pushButton_47.setText(_translate("Form", "善后处理"))
        self.label_2.setText(_translate("Form", "第"))
        self.label_3.setText(_translate("Form", "篇论文"))
import program_images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
