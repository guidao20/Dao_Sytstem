__author__='Syd'

from PyQt5.Qt import *
from Eword_into_mode import Ui_Form
import sys
import pymysql


class Eword_into_pane(QWidget,Ui_Form):

    exit_wordbase_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def exit_wordbase(self):
        self.exit_wordbase_signal.emit()

    def Write_into_databases(self,word,translation,example):
        db = pymysql.connect('localhost', 'root', '','experience')
        cursor = db.cursor()
        columns =  ['words','translations','examples']
        keys_ = ','.join(columns)
        values_ = ','.join(['%s'] * 3)
        sql_insert = 'INSERT INTO enwords({keys}) VALUES({values})'.format(keys=keys_, values=values_)
        print(sql_insert)
        input_list = [word,translation,example]
        input_tuple = tuple(input_list)
        cursor.execute(sql_insert, input_tuple)
        db.commit()
        db.close()
        cursor.close()

    def update_content(self,word,column,content):
        db = pymysql.connect('localhost', 'root', '', 'experience')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = 'update enwords set %s=\'%s\' WHERE words =\'%s\'' % (column,content, word)
        print(sql)
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
        sql = 'delete from enwords WHERE words =\'%s\'' % (word)
        # 执行SQL语句
        cursor.execute(sql)
        db.commit()
        # 关闭数据库连接
        db.close()



    def submit(self):
        if  self.comboBox.currentText().strip() == 'write':
            self.Write_into_databases(self.Wordle.text().strip(),self.transle.text().strip(),self.examplele.text().strip())
        elif self.comboBox.currentText().strip() == 'fix':
            if len(self.examplele.text()):
                self.update_content(self.Wordle.text().strip(),'examples',self.examplele.text().strip())
            elif len(self.transle.text()):
                self.update_content(self.Wordle.text().strip(),'translations',self.transle.text().strip())
        else:
            if len(self.Wordle.text()) > 0:
                self.delete_word(self.Wordle.text().strip())




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 2 控件的操作
    # 2.1 创建控件，设置控件(大小，位置，样式)
    window = Eword_into_pane()

    # 2.2  展示控件
    window.show()

    # 3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())








