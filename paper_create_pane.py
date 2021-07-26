__author__='Syd'

from PyQt5.Qt import *
from paper_create_mode import Ui_Form
import sys
import os


class paper_create_pane(QWidget,Ui_Form):
    exit_create_signal = pyqtSignal()


    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def paper_program(self):
        path = r'E:\program\cmd\program\paper_deal\Region_Emotion_Program.bat'
        os.system(path)
        path1 = r'E:\program\cmd\program\paper_deal'
        os.system('start "" '+ path1)

    def paper_create(self):
        path = r'E:\program\cmd\program\paper_deal\Region_Emotion_Writing.bat'
        os.system(path)

    def exit_create_pane(self):
        self.exit_create_signal.emit()

if __name__ == '__main__':

    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)

    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = paper_create_pane()

    #2.2  展示控件
    window.show()

    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
