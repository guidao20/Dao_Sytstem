__author__='Syd'

from PyQt5.Qt import *
from writing_mode import Ui_Form
import sys
import os
from datetime import datetime

import main_gif_rc
class writing_pane(QWidget,Ui_Form):
    exit_writing_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def writing_exit(self):
        self.exit_writing_signal.emit()

    def paper_interpreter(self):
        path = r'E:\document\Writing\Interpret_paper'
        os.system('start " " ' + path)

    def projection_document(self):
        path = r'E:\document\Writing\Project_documentation'
        os.system('start " " ' + path)

    def email_communication(self):
        path = r'E:\document\Writing\Email_communication'
        os.system('start " " '+path)

    def progress_report(self):
        path = r'E:\document\Writing\Work_report'
        os.system('start " " ' + path)





if __name__ == '__main__':
    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)
    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = writing_pane()
    #2.2  展示控件
    window.show()
    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
