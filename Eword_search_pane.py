__author__='Syd'

from PyQt5.Qt import *
from Eword_search_mode import Ui_Form
import sys
import pymysql


class Eword_search_pane(QWidget,Ui_Form):

    exit_search_signal = pyqtSignal()
    enter_into_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def exit_search_word(self):
        self.exit_search_signal.emit()

    def enter_into(self):
        self.enter_into_signal.emit()

    def Content_list(self):
        word_list = []
        transation_list = []
        examples_list = []
        db = pymysql.connect('localhost', 'root', '', 'experience')
        cursor = db.cursor()
        sql = 'SELECT words,translations,examples FROM enwords'
        cursor.execute(sql)
        alldata = cursor.fetchall()
        for item in alldata:
            word_list.append(item[0])
            transation_list.append(item[1])
            examples_list.append(item[2])
        db.commit()
        db.close()
        cursor.close()
        return word_list,transation_list,examples_list

    def show_translation(self):
        if self.radioButton.isChecked():
            text = self.Qle.text().strip()
            word_list, translation_list, _ = self.Content_list()
            for idx,item in enumerate(word_list):
                if text.strip() == item:
                    self.textBrowser_trans.append(word_list[idx]+': '+str(translation_list[idx]))
        else:
            searching_list = []
            text = self.Qle.text().strip()
            word_list,translation_list,_ = self.Content_list()
            for idx,item in enumerate(translation_list):
                if item != None:
                    if text in item.strip():
                        searching_list.append(word_list[idx].strip()+':   '+translation_list[idx].strip())
            searched_str = '\n'.join(searching_list)
            self.textBrowser_trans.append('查询结果共{}条'.format(len(searching_list)))
            self.textBrowser_trans.append(searched_str)


    def show_example(self):
        if self.radioButton.isChecked():
            text = self.Qle.text().strip()
            word_list,_, examples_list = self.Content_list()
            for idx, item in enumerate(word_list):
                if text.strip() == item:
                    self.textBrowser_senten.append(word_list[idx].strip()+':\n   '+'\n'.join(str(examples_list[idx]).split('#')))
        else:
                searching_list = []
                text = self.Qle.text().strip()
                word_list,translation_list,examples_list = self.Content_list()
                for idx,item in enumerate(translation_list):
                    if item != None:
                        if text in item.strip():
                            searching_list.append(word_list[idx].strip()+':\n   '+'\n'.join(str(examples_list[idx]).split('#')))
                searched_str = '\n'.join(searching_list)
                self.textBrowser_senten.append('查询结果共{}条'.format(len(searching_list)))
                self.textBrowser_senten.append(searched_str)

    def clear_translation(self):
        self.textBrowser_trans.clear()

    def clear_example(self):
        self.textBrowser_senten.clear()





if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 2 控件的操作
    # 2.1 创建控件，设置控件(大小，位置，样式)
    window = Eword_search_pane()

    # 2.2  展示控件
    window.show()

    # 3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())








