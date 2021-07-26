# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_mode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 780)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.program = QtWidgets.QWidget(Form)
        self.program.setStyleSheet("")
        self.program.setObjectName("program")
        self.program_btn = QtWidgets.QPushButton(self.program)
        self.program_btn.setEnabled(True)
        self.program_btn.setGeometry(QtCore.QRect(140, 140, 221, 100))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(36)
        self.program_btn.setFont(font)
        self.program_btn.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    color: rgb(0, 170, 0);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 163, 200);\n"
"}")
        self.program_btn.setFlat(True)
        self.program_btn.setObjectName("program_btn")
        self.program_l = QtWidgets.QLabel(self.program)
        self.program_l.setGeometry(QtCore.QRect(0, 0, 480, 390))
        self.program_l.setStyleSheet("color: rgb(0, 255, 0);")
        self.program_l.setText("")
        self.program_l.setObjectName("program_l")
        self.program_l.raise_()
        self.program_btn.raise_()
        self.gridLayout.addWidget(self.program, 0, 1, 1, 1)
        self.mindself = QtWidgets.QWidget(Form)
        self.mindself.setStyleSheet("")
        self.mindself.setObjectName("mindself")
        self.mindself_btn = QtWidgets.QPushButton(self.mindself)
        self.mindself_btn.setGeometry(QtCore.QRect(100, 140, 271, 100))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(36)
        self.mindself_btn.setFont(font)
        self.mindself_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 170, 0);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 127);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 163, 200);\n"
"}")
        self.mindself_btn.setFlat(True)
        self.mindself_btn.setObjectName("mindself_btn")
        self.mindself_l = QtWidgets.QLabel(self.mindself)
        self.mindself_l.setGeometry(QtCore.QRect(0, 0, 480, 390))
        self.mindself_l.setText("")
        self.mindself_l.setObjectName("mindself_l")
        self.mindself_l.raise_()
        self.mindself_btn.raise_()
        self.gridLayout.addWidget(self.mindself, 1, 0, 1, 1)
        self.working = QtWidgets.QWidget(Form)
        self.working.setStyleSheet("")
        self.working.setObjectName("working")
        self.working_btn = QtWidgets.QPushButton(self.working)
        self.working_btn.setGeometry(QtCore.QRect(110, 150, 251, 100))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(36)
        self.working_btn.setFont(font)
        self.working_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(225, 225, 225);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 163, 200);\n"
"}")
        self.working_btn.setFlat(True)
        self.working_btn.setObjectName("working_btn")
        self.working_l = QtWidgets.QLabel(self.working)
        self.working_l.setGeometry(QtCore.QRect(0, 0, 480, 390))
        self.working_l.setText("")
        self.working_l.setObjectName("working_l")
        self.working_l.raise_()
        self.working_btn.raise_()
        self.gridLayout.addWidget(self.working, 1, 1, 1, 1)
        self.paper = QtWidgets.QWidget(Form)
        self.paper.setStyleSheet("")
        self.paper.setObjectName("paper")
        self.paper_btn = QtWidgets.QPushButton(self.paper)
        self.paper_btn.setEnabled(True)
        self.paper_btn.setGeometry(QtCore.QRect(150, 150, 160, 100))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(36)
        self.paper_btn.setFont(font)
        self.paper_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 0, 127);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(153, 80, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 163, 200);\n"
"}")
        self.paper_btn.setFlat(True)
        self.paper_btn.setObjectName("paper_btn")
        self.paper_l = QtWidgets.QLabel(self.paper)
        self.paper_l.setGeometry(QtCore.QRect(0, 0, 480, 390))
        self.paper_l.setText("")
        self.paper_l.setObjectName("paper_l")
        self.paper_l.raise_()
        self.paper_btn.raise_()
        self.gridLayout.addWidget(self.paper, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(Form)
        self.paper_btn.clicked.connect(Form.paper_pane_show)
        self.program_btn.clicked.connect(Form.program_pane_show)
        self.mindself_btn.clicked.connect(Form.mind_pane_show)
        self.working_btn.clicked.connect(Form.work_pane_show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.program_btn.setText(_translate("Form", "Program"))
        self.mindself_btn.setText(_translate("Form", "Introspection"))
        self.working_btn.setText(_translate("Form", "Harmonious"))
        self.paper_btn.setText(_translate("Form", "Paper"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
