__author__='Syd'

from PyQt5.Qt import *
from challenge_mode import Ui_Form
import sys
import shutil
from datetime import datetime
import time
import os
from matplotlib import pyplot as plt
from collections import Counter
from operator import itemgetter

class challenge_pane(QWidget,Ui_Form):
    exit_challenge_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def challenge_info_input(self):
        list_challenge = []
        list_challenge.append('问题定义:'+self.Reason_le.text())
        list_challenge.append('原因探究:'+self.Necessity_le.text())
        list_challenge.append('解决方法:'+self.Action_le.text())
        list_challenge.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        for idx ,item in enumerate(list_challenge):
            list_challenge[idx] = item.strip()
        return list_challenge

    def exit_challenge(self):
        self.exit_challenge_signal .emit()

    def convert_to_stamp(self,time_str_list):
        time_stamp_list = []
        for time_str in time_str_list:
            time_str = time_str+' '+'00:00:00'
            time_array = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            time_stamp = time.mktime(time_array)
            time_stamp_list.append(time_stamp)
        return time_stamp_list

    def draw_line(self):
        path = 'E:\document\mind_data\challenge_log.txt'
        fr = open(path,'r')
        date_list = []
        for item in fr.readlines():
            if item.strip()[:2] == '20':
                date_list.append(item.strip().split(' ')[0])
        number_dict = Counter(date_list)
        X_set = set(date_list)
        X_list = list(X_set)
        X_stamp_list = self.convert_to_stamp(X_list)
        def make_dict(elem1, elem2):
            dict_ = {'time': elem1, 'stamp': elem2}
            return dict_
        time_order_list = []
        for idx in range(len(X_list)):
            time_order_list.append(make_dict(X_list[idx],X_stamp_list[idx]))
        order_dict_list = sorted(time_order_list, key=itemgetter('stamp'), reverse=False)
        X_time_list = []
        for elem in order_dict_list:
            X_time_list.append(elem['time'])
        Y_value_list = []
        for elem in X_time_list:
            Y_value_list.append(number_dict[elem])
        plt.plot(X_time_list, Y_value_list)
        plt.show()

    def log(self):
        path = 'E:\document\mind_data\challenge_log.txt'
        os.system('start " " '+path)
        # self.draw_line()

    def Record(self):
        path = r'E:\document\mind_data\challenge_log.txt'
        log_list = []
        fr = open(path,'r')
        for item in fr.readlines():
            if len(item.strip()) != 0 :
                log_list.append(item.strip())
        fr.close()
        write_log_list = self.challenge_info_input()
        log_list = log_list + write_log_list
        fw = open(path,'w')
        for item in log_list:
            fw.write(item)
            fw.write('\n')
        fw.close()







if __name__ == '__main__':

    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)

    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = challenge_pane()

    #2.2  展示控件
    window.show()

    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
