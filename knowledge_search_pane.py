__author__='Syd'

from PyQt5.Qt import *
from knowledge_search_mode import Ui_Form
import sys
import pymysql
import os


class knowledge_search_pane(QWidget,Ui_Form):

    exit_search_signal = pyqtSignal()
    enter_into_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def exit_search_know(self):
        self.exit_search_signal.emit()

    def enter_into_know(self):
        self.enter_into_signal.emit()

    def Content_list(self):
        what_list = []
        explain_list = []
        img_list = []
        db = pymysql.connect('localhost', 'root', '', 'experience')
        cursor = db.cursor()
        sql = 'SELECT what,explaination,figure FROM knowledge'
        cursor.execute(sql)
        alldata = cursor.fetchall()
        for item in alldata:
            what_list.append(item[0])
            explain_list.append(item[1])
            img_list.append(item[2])
        db.commit()
        db.close()
        cursor.close()
        return what_list, explain_list,img_list

    def search_result(self):
        searching_list = []
        text = self.Qle.text().strip()
        what_list, explain_list, _ = self.Content_list()
        if not self.radioButton.isChecked():
            for idx, item in enumerate(explain_list):
                if item != None:
                    if text in item.strip():
                        searching_list.append('第'+str(idx)+'条'+'\n'+'知识点：'+what_list[idx].strip() + '\n' +'知识点解析： ' + explain_list[idx].strip())
        else:
            for idx, item in enumerate(explain_list):
                searching_list.append('第'+str(idx)+'条'+'\n'+'知识点：'+what_list[idx].strip() + '\n' +'知识点解析： ' + explain_list[idx].strip())
        searched_str = '\n'.join(searching_list)
        self.textBrowser_trans.append('查询结果共{}条'.format(len(searching_list)))
        self.textBrowser_trans.append(searched_str)


    def show_img(self,img):
        path_read = r'F:\Desktop\mysql\img\show.png'
        fout = open(path_read,'wb')
        fout.write(img)
        fout.close()
        path_read = r'F:\Desktop\mysql\img\show.png'
        os.system('start " " ' + path_read)

    def clear_box(self):
        self.textBrowser_trans.clear()

    def show_result(self):
        text = self.Qle.text().strip()
        what_list, explain_list, img_list = self.Content_list()
        for idx, item in enumerate(what_list):
            if item != None:
                if text == item.strip():
                    self.textBrowser_trans.append(' 知识点解析： '+explain_list[idx])
                    self.show_img(img_list[idx])




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 2 控件的操作
    # 2.1 创建控件，设置控件(大小，位置，样式)
    window = knowledge_search_pane()

    # 2.2  展示控件
    window.show()

    # 3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())








