__author__='Syd'


from PyQt5.Qt import *
from write_database_mode import Ui_Form
import sys
from datetime import datetime
import pymysql

class write_database_pane(QWidget,Ui_Form):
    exit_database_signal = pyqtSignal()
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def exit_database(self):
        self.exit_database_signal.emit()

    def Write_into_databases(self,question,answer,analysis,table_name):
        db = pymysql.connect('localhost', 'root', '','experience')
        cursor = db.cursor()
        question_str = question
        answer_str = answer
        analysis_str = analysis
        time_str = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        columns =  ['what','how','why','timepoint']
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

    def update_content(self,table,key,content,id_content):
        db = pymysql.connect('localhost', 'root', '', 'experience')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = 'update {table} set {key}=\'%s\' WHERE {id}=%d'.format(table=table, key=key, id='id') % (content, id_content)
        # 执行SQL语句
        cursor.execute(sql)
        db.commit()
        # 关闭数据库连接
        db.close()

    def delete_content(self, table, id):
        db = pymysql.connect('localhost', 'root', '', 'experience')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = 'delete from %s WHERE id =%d' % (table,id)
        # 执行SQL语句
        cursor.execute(sql)
        db.commit()
        # 关闭数据库连接
        db.close()

    def rerank(self,table):
        db = pymysql.connect('localhost', 'root', '', 'experience')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql_drop = 'alter table %s drop id' % (table)
        # 执行SQL语句
        cursor.execute(sql_drop)
        sql_column = 'alter table %s add id int not null PRIMARY KEY AUTO_INCREMENT FIRST ' %(table)
        cursor.execute(sql_column)
        db.commit()
        # 关闭数据库连接
        db.close()

    def submit(self):
        if self.comboBox_2.currentText().strip() == 'write':
            question_str = self.Qle.text().strip()
            anwser_str = self.Asle.text().strip()
            analysis_str = self.Ayle.text().strip()
            table_name = self.comboBox.currentText().strip()
            if len(question_str) > 0 :
                self.Write_into_databases(question_str,anwser_str,analysis_str,table_name)
        elif self.comboBox_2.currentText().strip() == 'fix':
            id = int(self.IDle.text().strip())
            table_name = self.comboBox.currentText().strip()
            if len(self.Asle.text().strip()) > 0:
                key = 'how'
                content = self.Asle.text().strip()
            elif len(self.Ayle.text().strip()):
                key = 'why'
                content = self.Ayle.text().strip()
            else:
                key = 'what'
                content = self.Qle.text().strip()
            self.update_content(table_name,key,content,id)
        else:
            id = int(self.IDle.text().strip())
            table_name = self.comboBox.currentText().strip()
            if len(self.IDle.text().strip()):
                self.delete_content(table_name,id)
                self.rerank(table_name)





if __name__ == '__main__':

    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)

    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = write_database_pane()

    #2.2  展示控件
    window.show()

    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
