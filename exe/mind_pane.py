__author__='Syd'

from PyQt5.Qt import *
from mind_mode import Ui_Form
import sys
import smtplib
from email.mime.text import MIMEText
import os,shutil
from datetime import datetime


import main_gif_rc
class mind_pane(QWidget,Ui_Form):
    exit_mind_signal = pyqtSignal()
    show_plan_split_signal = pyqtSignal()
    show_challenge_signal = pyqtSignal()
    show_matrix_system_signal = pyqtSignal()


    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)


    def life_run(self):
        path = r'E:\document\mind_data\Answer\Life_mode\record'
        os.system('start " " '+path)


    def life_reset(self):
        path = r'E:\document\mind_data\Answer\Life_mode\record\High_Score.txt'
        f1 = open(path,'r')
        read_list = f1.readlines()
        path0 =  r'E:\document\mind_data\Answer\Life_mode\record\log_score.txt'
        f0 = open(path0,'a')
        writelog = read_list[0].strip() + '\n'
        f0.write(writelog)
        f0.close()
        read_list[0] = str(0)+'\n'
        f1.close()
        f2 = open(path,'w')
        for elem in read_list:
            f2.write(elem)
        f2.close()
        path3 = r'E:\document\mind_data\Answer\Life_mode\record\log.txt'
        f3 = open(path3,'r')
        log_list = f3.readlines()
        f3.close()
        path4 = r'E:\document\mind_data\Answer\Life_mode\record\log_restore.txt'
        f4 = open(path4,'a')
        for elem in log_list:
            f4.write(elem)
        f4.close()


    def exit_mind(self):
        self.exit_mind_signal.emit()

    def submit_want(self):
        path = r'E:\document\mind_data\want_to_do.txt'
        self.save_txt(path)

    def save_txt(self,path):
        fw = open(path,'a')
        fw.write(self.want_le.text().strip())
        fw.write('\n')
        fw.close()



    def show_want(self):
        path = r'E:\program\cmd\program\want_to_do.bat'
        os.system(path)

    def Matrix_show(self):
        self.show_matrix_system_signal.emit()

    def make_habit(self):
        self.show_challenge_signal.emit()

    def clear_headed(self):
        path_del = r'E:\document\mind_data\clear_headed\del.bat'
        os.system(path_del)
        path = r'E:\document\mind_data\clear_headed'
        os.system('start "" '+path)

    def life_list(self):
        path = r'E:\document\mind_data\Answer\Life_mode\merge_lifelist.bat'
        os.system(path)

    def life_list_show(self):
        path = 'E:\document\mind_data\Answer\Life_mode\lifelist'
        os.system('start " " '+path)

    def wrong_log(self):
        path = r'E:\document\mind_data\wrong_log.txt'
        text_str = ''
        record_time = '时间:' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Things = '焦虑事件:'
        Feelings = '情绪感受:'
        text_str = text_str + record_time + '\n' + Things + '\n' + Feelings + '\n'
        fa = open(path, 'a')
        fa.write(text_str)
        fa.close()
        os.system('start " " ' + path)

    def long_plan(self):
        path = r'E:\document\mind_data\Answer\Life_mode\longduty\File'
        os.system('start " " ' + path)
        path1 = r'E:\document\mind_data\Answer\Life_mode\longduty\Dutyorder.bat'
        os.system(path1)

    def long_show(self):
        path = 'E:\document\mind_data\Answer\Life_mode\longduty'
        os.system('start " " ' + path)

if __name__ == '__main__':
    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)
    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = mind_pane()
    #2.2  展示控件
    window.show()
    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
