__author__='Syd'

from PyQt5.Qt import *
from warn_mode import Ui_Form
import sys
import shutil


class warn_pane(QWidget,Ui_Form):
    exit_warn_signal = pyqtSignal()


    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def write_txt(self,list_input):
        path_file1 = r'E:\document\mind_data\plan_dist.txt'
        path_file2 = r'E:\document\mind_data\plan_dist_warn.txt'
        shutil.copyfile(path_file1 , path_file2)
        list_read = []
        morn_idx = 0
        after_idx = 0
        with open(path_file2,'r') as f_r:
            for line in f_r.readlines():
                list_read.append(line.strip())
            for idx,line in enumerate(list_read):
                if '上午=' in line:
                    morn_idx = idx + 1
                elif '下午=' in line:
                    after_idx = idx + 1

        if list_input[0].strip() == '上':
            list_read.insert(morn_idx, '行动指南#'+list_input[3])
            list_read.insert(morn_idx, '行动指南#'+list_input[2])
            list_read.insert(morn_idx, '拖延阻碍#'+list_input[1])
            list_read.insert(morn_idx, '----------------------')
        elif list_input[0].strip() == '下':
            list_read.insert(after_idx, '行动指南#'+list_input[3])
            list_read.insert(after_idx, '行动指南#'+list_input[2])
            list_read.insert(after_idx, '拖延阻碍#'+list_input[1])
            list_read.insert(after_idx, '----------------------')

        with open(path_file2,'w') as f_w:
            for line in list_read:
                f_w.write(line)
                f_w.write('\n')

    def warn_info_input(self):
        list_warn = []
        list_warn.append(self.morn_noon_le.text())
        list_warn.append(self.tuoyan_le.text())
        list_warn.append(self.neixin_le.text())
        list_warn.append(self.xingdong_le.text())
        return list_warn

    def submit_warn(self):
        input_list = self.warn_info_input()
        self.write_txt(input_list)

    def exit_warn(self):
        self.exit_warn_signal.emit()


if __name__ == '__main__':

    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)

    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = warn_pane()

    #2.2  展示控件
    window.show()

    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
