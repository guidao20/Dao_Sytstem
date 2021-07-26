__author__='Syd'

from PyQt5.Qt import *
from bat_mode import Ui_Form
import sys
import os


class bat_pane(QWidget,Ui_Form):
    exit_bat_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def exit_bat_show(self):
        self.exit_bat_signal.emit()

    def run_pycharm(self):
        bat_path = r'E:\program\cmd\run_program\pycharm.bat'
        os.system(bat_path)

    def run_VMware(self):
        VM_path = r'E:\program\cmd\run_program\VM.bat'
        os.system(VM_path)

    def run_auto(self):
        auto_path = r'E:\program\cmd\run_program\auto.bat'
        os.system(auto_path)

    def run_anjian(self):
        anjian_path = r'E:\program\cmd\run_program\anjian.bat'
        os.system(anjian_path)

    def run_v2rayn(self):
        v2_path = r'E:\program\cmd\run_program\v2ray.bat'
        os.system(v2_path)

    def run_worldplay(self):
        wordplay_path = r'E:\program\cmd\program\word_play.bat'
        os.system(wordplay_path)

    def run_advemotion(self):
        path = r'E:\program\cmd\latex\Adv_emotion.bat'
        os.system(path)

    def run_habit(self):
        path = r'E:\program\cmd\latex\Habit.bat'
        os.system(path)

    def run_wechat(self):
        path = r'E:\program\cmd\run_program\Tencent.bat'
        os.system(path)

    def run_google(self):
        path = r'E:\program\cmd\run_program\liu.bat'
        os.system(path)

    def run_music(self):
        path = r'E:\program\cmd\run_program\qqmusic.bat'
        os.system(path)

    def run_dao(self):
        path = r'E:\program\cmd\program\Main_window.bat'
        os.system(path)

    def run_make(self):
        path = r'D:\python_program\pyqt5\Dao_system\exe\w_make_exe.bat'
        os.system(path)

    def run_reguplan(self):
        path = r'E:\program\cmd\program\plan.bat'
        os.system(path)

    def run_youdao(self):
        path = r'E:\program\cmd\run_program\youdao.bat'
        os.system(path)

    def deal_system_rabbit(self):
        path = r'E:\program\cmd\program\Del_system_files.bat'
        os.system(path)

if __name__ == '__main__':

    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)

    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = bat_pane()

    #2.2  展示控件
    window.show()

    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
