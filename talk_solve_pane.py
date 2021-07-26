__author__='Syd'

from PyQt5.Qt import *
from talk_solve_mode import Ui_Form
import sys
from datetime import datetime
import os
import pymysql
import numpy as np
from aip import AipNlp

import main_gif_rc
class talk_solve_pane(QWidget,Ui_Form):
    exit_talk_solve_signal = pyqtSignal()
    enter_writedata_signal = pyqtSignal()
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def exit_talk_solve(self):
        self.exit_talk_solve_signal.emit()

    def enter_datawrite(self):
        self.enter_writedata_signal.emit()

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

    def search_what_list(self,column_name,table_name):
        what_list = []
        db = pymysql.connect('localhost', 'root', '', 'experience')
        cursor = db.cursor()
        sql = 'SELECT {column} FROM {table_name}'.format(column=column_name,table_name=table_name)
        cursor.execute(sql)
        alldata = cursor.fetchall()
        for item in alldata:
            what_list.append(item[0])
        db.commit()
        db.close()
        cursor.close()
        return what_list


    def Write_into_databases(self,question,answer,analysis,table_name):
        db = pymysql.connect('localhost', 'root', '','experience')
        cursor = db.cursor()
        question_str = question
        answer_str = answer
        analysis_str = analysis
        time_str = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        columns =  ['question','answer','analysis','timepoint']
        keys_ = ','.join(columns)
        table_ = table_name
        values_ = ','.join(['%s'] * 4)
        sql_insert = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table_, keys=keys_, values=values_)
        input_list = [question_str,answer_str,analysis_str,time_str]
        input_tuple = tuple(input_list)
        cursor.execute(sql_insert, input_tuple)
        db.commit()
        db.close()
        cursor.close()




    def Similarity(self,text1,text2):
        APP_ID = '22771618'
        API_KEY = 'Qoet0c81cYxUGaq09U04CnnN'
        SECRET_KEY = '6C52Vz9q7naDSn5e0kQQ3l69jCXt9lGQ'
        client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
        options = {}
        options['model'] = 'CNN'
        score = client.simnet(text1,text2,options)['score']
        return score

    def Similarity_T(self,text1,text2):
        try:
            score =self.Similarity(text1,text2)
            return score
        except:
            if text1.strip()== text2.strip():
                score = 1
            else:
                score = 0
            return score


    def find_id(self):
        text_list = self.search_what_list('what',self.comboBox.currentText().strip())
        text = self.Qle.text().strip()
        score_list = []
        for item in text_list:
            score_list.append(self.Similarity_T(text,item))
            print(score_list)
        max_index = score_list.index(max(score_list))
        return max_index

    def search(self):
        if self.radioButton.isChecked():
            text_list = self.search_what_list('what', self.comboBox.currentText().strip())
            text = self.Qle.text().strip()
            for idx, item in enumerate(text_list):
                if text in item:
                    self.textBrowser_sub.append('ID:' + str(idx + 1) + '   ' + item)
        else:
            text_list = self.search_what_list('what',self.comboBox.currentText().strip())
            max_index = self.find_id()
            print(max_index)
            question = text_list[max_index]
            self.textBrowser_anwser.append('ID:'+str(max_index+1)+'      '+'WHAT:'+question)


    def show_answer(self):
        text_list = self.search_what_list('how', self.comboBox.currentText().strip())
        max_index = self.find_id()
        answer_list = text_list[max_index].split('#')
        answer_str = '\n'.join(answer_list)
        self.textBrowser_anwser.append('HOW: \n'+answer_str)

    def show_analysis(self):
        text_list = self.search_what_list('why', self.comboBox.currentText().strip())
        max_index = self.find_id()
        answer_list = text_list[max_index].split('#')
        answer_str = '\n'.join(answer_list)
        self.textBrowser_analysis.append('WHY: \n' + answer_str)


    def clear_answer(self):
        self.textBrowser_anwser.clear()

    def clear_analysis(self):
        self.textBrowser_analysis.clear()

    def clear_sub(self):
        self.textBrowser_sub.clear()

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
