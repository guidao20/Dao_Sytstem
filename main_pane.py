__author__='Syd'

from PyQt5.Qt import *
from main_mode import Ui_Form
import sys

import main_gif_rc
class Main_Pane(QWidget,Ui_Form):
    show_program_pane_signal = pyqtSignal()
    show_paper_pane_signal = pyqtSignal()
    show_mind_pane_signal = pyqtSignal()
    show_together_singnal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.movie_action()


    def movie_action(self):
        movie_paper = QMovie(":/gif/picture/paper.gif")
        movie_paper.setScaledSize(QSize(480,390))
        self.paper_l.setMovie(movie_paper)
        movie_paper.start()

        movie_program = QMovie(":/gif/picture/program.gif")
        movie_paper.setScaledSize(QSize(480, 390))
        self.program_l.setMovie(movie_program)
        movie_program.start()

        movie_mindself = QMovie(":/gif/picture/mind.gif")
        movie_mindself.setScaledSize(QSize(480, 390))
        self.mindself_l.setMovie(movie_mindself)
        movie_mindself.start()

        movie_work = QMovie(":/gif/picture/work.gif")
        movie_work.setScaledSize(QSize(480, 390))
        self.working_l.setMovie(movie_work)
        movie_work.start()

    def paper_pane_show(self):
        self.show_paper_pane_signal.emit()

    def program_pane_show(self):
        self.show_program_pane_signal.emit()

    def mind_pane_show(self):
        self.show_mind_pane_signal.emit()

    def work_pane_show(self):
        self.show_together_singnal.emit()









if __name__ == '__main__':

    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)

    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = Main_Pane()

    #2.2  展示控件
    window.show()

    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
