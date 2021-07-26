__author__='Syd'

from PyQt5.Qt import *
from talk_solve_mode import Ui_Form
import sys
from datetime import datetime
import os

import main_gif_rc
class talk_solve_pane(QWidget,Ui_Form):
    exit_talk_solve_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def exit_talk_solve(self):
        self.exit_talk_solve_signal.emit()

    def Night(self):
        path = r'E:\document\Together\human\Juan\greet\image\Original'
        os.system('start " " '+path)

    def Amina(self):
        path = 'E:\document\Together\human\Juan\greet'
        os.system('start " " ' + path)

    def Greeting(self):
        path = 'E:\document\Together\human\Juan\greet\material\Loving_greeting.txt'
        path1 = 'E:\document\Together\human\Juan\greet\material'
        os.system('start "" '+path)
        os.system('start "" '+path1)


if __name__ == '__main__':

    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)

    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = talk_solve_pane()

    #2.2  展示控件
    window.show()

    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
