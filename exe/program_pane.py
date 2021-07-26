__author__='Syd'


from PyQt5.Qt import *
from program_mode import Ui_Form
import sys
import os

import main_gif_rc
class program_pane(QWidget,Ui_Form):
    exit_program_signal = pyqtSignal()
    show_bat_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def exit_program(self):
        self.exit_program_signal.emit()

    def show_bat_pane(self):
        self.show_bat_signal.emit()

    def show_torch(self):
        path = 'D:\python_program\pytorch'
        os.system('start "" '+ path)

    def show_pygame(self):
        path= 'D:\python_program\pygame\Official_course'
        os.system('start "" ' + path)

    def show_python(self):
        path = 'D:\python_program\python'
        os.system('start "" '+ path)





if __name__ == '__main__':
    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)
    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = program_pane()
    #2.2  展示控件
    window.show()
    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
