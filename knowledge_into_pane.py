__author__='Syd'

from PyQt5.Qt import *
from knowledge_into_mode import Ui_Form
import sys
import pymysql
from datetime import datetime
import os

class knowledge_into_pane(QWidget,Ui_Form):

    exit_knowbase_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def exit_knowbase(self):
        self.exit_knowbase_signal.emit()

    def get_img(self):
        path= r'F:\Desktop\mysql\img\1.png'
        fp = open(path, 'rb')
        img = fp.read()
        fp.close()
        return img

    def Write_into_databases(self,what_c,explain_c):
        img = self.get_img()
        timepoint = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = pymysql.connect('localhost', 'root', '', 'experience')
        cursor = conn.cursor()
        columns = ['what', 'explaination', 'figure', 'timepoint']
        keys_ = ','.join(columns)
        values_ = ','.join(['%s', '%s', '_binary %s', '%s'])
        sql_insert = 'INSERT INTO knowledge({keys}) VALUES({values})'.format(keys=keys_, values=values_)
        input_list = [what_c, explain_c, img, timepoint]
        print(input_list)
        input_tuple = tuple(input_list)
        cursor.execute(sql_insert, input_tuple)
        conn.commit()
        cursor.close()
        conn.close()


    def update_content(self,word,column,content):
        db = pymysql.connect('localhost', 'root', '', 'experience')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = 'update knowledge set %s=\'%s\' WHERE words =\'%s\'' % (column,content, word)
        # 执行SQL语句
        cursor.execute(sql)
        db.commit()
        # 关闭数据库连接
        db.close()


    def delete_word(self,word):
        db = pymysql.connect('localhost', 'root', '', 'experience')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = 'delete from knowledge WHERE what =\'%s\'' % (word)
        # 执行SQL语句
        cursor.execute(sql)
        db.commit()
        # 关闭数据库连接
        db.close()


    def submit(self):
        if  self.comboBox.currentText().strip() == 'write':
            if len(self.Woldle.text().strip()) > 0:
                self.Write_into_databases(self.Woldle.text().strip(),self.transle.text().strip())
        elif self.comboBox.currentText().strip() == 'fix':
            if len(self.transle.text().strip()) > 0:
                self.update_content(self.Woldle.text().strip(),'explaination',self.transle.text().strip())
        else:
            if len(self.Woldle.text()) >= 0:
                self.delete_word(self.Woldle.text().strip())

    def open_img(self):
        path = r'F:\Desktop\mysql\img'
        os.system('start " " '+path)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 2 控件的操作
    # 2.1 创建控件，设置控件(大小，位置，样式)
    window = knowledge_into_pane()

    # 2.2  展示控件
    window.show()

    # 3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())








