__author__='Syd'

from PyQt5.Qt import *
from plan_split_mode import Ui_Form
import sys
import os


class plan_split_pane(QWidget,Ui_Form):
    exit_plan_split_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def write_plan_split(self,input_content):
        path = r'E:\document\mind_data\plan_split.txt'
        idx = 0
        with open(path, 'w') as f:
            for elem in input_content:
                if  '目标' in elem:
                    idx = 0
                    f.write(elem)
                    f.write('\n')
                else:
                    idx += 1
                    f.write('{}.'.format(idx)+elem)
                    f.write('\n')

    def input_info(self):
        input_list = []
        input_list.append(self.name_le.text())
        input_list.append(self.type_le.text())
        input_list.append(self.event1_le.text())
        input_list.append(self.event2_le.text())
        input_list.append(self.event3_le.text())
        input_list.append(self.event4_le.text())
        input_list.append(self.event5_le.text())
        return input_list

    def insert_dict_make(self,list_, condition):
        list_record = []
        list_name = []
        for idx, elem in enumerate(list_):
            if elem.strip().split('  ')[0].split(':')[0] == condition:
                list_name.append(elem.strip())
                list_record.append(idx)
        list_record1 = list_record[1:]
        list_record1.append(len(list_))
        nvs = zip(list_name, list_record1)
        insert_dict = dict((name, value) for name, value in nvs)
        return insert_dict,list_name

    def deal_input_info(self,input_list):
        input_deal_list1 = []
        for idx,i in enumerate(input_list):
            if i.strip() == '' or idx == 1:
                pass
            elif idx==0:
                i_deal = '目标:' + i +'  '+ '等级:'+ input_list[idx+1]
                input_deal_list1.append(i_deal)
            else:
                input_deal_list1.append(i)
        path = r'E:\document\mind_data\plan_split.txt'
        f_list = []
        with open(path, 'r') as f:
            for line in f.readlines():
                if '目标' in line:
                    f_list.append(line.strip())
                else:
                    try:
                        f_list.append(line.strip().split('.')[1])
                    except:
                        pass

        inset_dict_check ,list_name = self.insert_dict_make(f_list,'目标')

        if len(input_deal_list1)>0:
            if input_deal_list1[0] in list_name:
                idx_record = inset_dict_check[input_deal_list1[0]]
                for line in input_deal_list1[1:]:
                    f_list.insert(idx_record,line)
                    idx_record += 1
            elif 'A' in input_deal_list1[0] and 'B' not in input_deal_list1[0]:
                idx_record = inset_dict_check[list_name[-2]]
                for line in input_deal_list1:
                    f_list.insert(idx_record,line)
                    idx_record += 1
        else:
            pass
        return f_list

    def submit_plan(self):
        input_list = self.input_info()
        input_list1 = self.deal_input_info(input_list)
        self.write_plan_split(input_list1)

    def exit_plan_split(self):
        self.exit_plan_split_signal.emit()




if __name__ == '__main__':

    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)

    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = plan_split_pane()

    #2.2  展示控件
    window.show()

    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
