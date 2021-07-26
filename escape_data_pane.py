__author__='Syd'

from PyQt5.Qt import *
from escape_data_mode import Ui_Form
import sys
import pymysql
from datetime import datetime
from collections import Counter

class escape_data_pane(QWidget,Ui_Form):

    exit_elution_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def Write_into_databases(self,label,event,feel,timepoint):
        db = pymysql.connect('localhost', 'root', '','lifedata')
        cursor = db.cursor()
        columns =  ['label','event','feel','timepoint']
        keys_ = ','.join(columns)
        values_ = ','.join(['%s'] * 4)
        sql_insert = 'INSERT INTO escapedata({keys}) VALUES({values})'.format(keys=keys_, values=values_)
        input_list = [label,event,feel,timepoint]
        input_tuple = tuple(input_list)
        cursor.execute(sql_insert, input_tuple)
        db.commit()
        db.close()
        cursor.close()

    def Content_list(self):
        label_list = []
        timepoint_list = []
        db = pymysql.connect('localhost', 'root', '', 'lifedata')
        cursor = db.cursor()
        sql = 'SELECT label,timepoint FROM escapedata'
        cursor.execute(sql)
        alldata = cursor.fetchall()
        for item in alldata:
            label_list.append(item[0])
            timepoint_list.append(item[1])
        db.commit()
        db.close()
        cursor.close()
        return label_list,timepoint_list

    def exit_escape(self):
        self.exit_elution_signal.emit()

    def Record(self):
        label = self.comboBox.currentText().strip()
        event = self.event_le.text().strip()
        feel = self.feel_le.text().strip()
        timepoint = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.Write_into_databases(label,event,feel,timepoint)

    def fig(self):
        label_list = self.Content_list()[0]
        Result= Counter(label_list)
        labelname_list = list(Result.keys())
        labelvalue_list = list(Result.values())
        print(labelvalue_list)
        show_str = ''
        for idx,item in enumerate(labelname_list):
            show_str += item + ':    ' +str(labelvalue_list[idx]) + '\n'
        print(show_str)
        self.textBrowser.append(show_str)

        # self.textBrowser.append(label_list)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 2 控件的操作
    # 2.1 创建控件，设置控件(大小，位置，样式)
    window = escape_data_pane()

    # 2.2  展示控件
    window.show()

    # 3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())








