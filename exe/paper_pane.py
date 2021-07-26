__author__='Syd'

from PyQt5.Qt import *
from paper_mode import Ui_Form
import sys
import os
import shutil
from datetime import datetime
import program_images_rc

import main_gif_rc
class paper_pane(QWidget,Ui_Form):
    exit_paper_signal = pyqtSignal()
    show_create_pane_signal = pyqtSignal()
    show_writing_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def paper_exit(self):
        self.exit_paper_signal.emit()

    def run_check_see(self):
        print('enter')

    def writing_show(self):
        self.show_create_pane_signal.emit()

    def collection(self):
        path_conference = r'E:\document\PAPER\paper_read\Conferences'
        path_journal = r'E:\document\PAPER\paper_read\Journals'
        os.system('start " " ' + path_conference)
        os.system('start " " ' + path_journal)


    def lookup(self):
        pass

    def Contribute(self):
        path_tex = r'E:\document\PAPER\paper_read\Writing\document'
        path_paper =r'E:\document\PAPER\paper_read\Writing\paper'
        os.system('start " " '+path_tex)
        os.system('start " " '+path_paper)

    def AI_math(self):
        path_deal = r'E:\document\PAPER\Support\Math\Tex_Deal.bat'
        os.system(path_deal)
        path = r'E:\document\PAPER\Support\Math\AI.tex'
        os.system('start "" '+path)

    def Life_math(self):
        path_deal = r'E:\document\PAPER\Support\Math\Tex_Deal.bat'
        os.system(path_deal)
        path = r'E:\document\PAPER\Support\Math\Life.tex'
        os.system('start "" ' + path)

    def Model_math(self):
        path_deal = r'E:\document\PAPER\Support\Math\Tex_Deal.bat'
        os.system(path_deal)
        path = r'E:\document\PAPER\Support\Math\Model.tex'
        os.system('start "" ' + path)

    def English_Friends(self):
        path = 'E:\document\English\Friends'
        os.system('start "" '+path)

    def copy_preparation(self):
        if len(self.number_le.text().strip()) > 0 :
            root_dir = r'E:\document\PAPER\My_papering\{}'.format(int(self.number_le.text()))
            if not os.path.isdir(root_dir):
                os.makedirs(root_dir)
            source_path = r'E:\document\PAPER\My_papering\common\preparation.txt'
            target_dir = r'E:\document\PAPER\My_papering\{}\1_preparation'.format(int(self.number_le.text()))
            if not os.path.isdir(target_dir):
                os.makedirs(target_dir)
            target_path = r'E:\document\PAPER\My_papering\{}\1_preparation\preparation.txt'.format(int(self.number_le.text()))
            if not os.path.exists(target_path):
                shutil.copy(source_path,target_path)

    def open_preparation(self):
        if len(self.number_le.text().strip()) > 0:
            path_root =  r'E:\document\PAPER\My_papering\{}\1_preparation'.format(int(self.number_le.text()))
            path_txt = r'E:\document\PAPER\My_papering\{}\1_preparation\preparation.txt'.format(int(self.number_le.text()))
            os.system('start " " '+path_root)
            os.system('start " " '+path_txt)

    def copy_idea(self):
        if len(self.number_le.text().strip()) > 0 :
            target_dir = r'E:\document\PAPER\My_papering\{}\2_idea'.format(int(self.number_le.text()))
            if not os.path.isdir(target_dir):
                os.makedirs(target_dir)
            source_idea_tex = r'E:\document\PAPER\My_papering\common\idea_generation.tex'
            target_idea_tex = r'E:\document\PAPER\My_papering\{}\2_idea\idea_generation.tex'.format(int(self.number_le.text()))
            if not os.path.exists(target_idea_tex):
                shutil.copy(source_idea_tex,target_idea_tex)
            source_tex_bat = r'E:\document\PAPER\My_papering\common\del.bat'
            target_tex_bat = r'E:\document\PAPER\My_papering\{}\2_idea\del.bat'.format(int(self.number_le.text()))
            if not os.path.exists(target_tex_bat):
                shutil.copy(source_tex_bat, target_tex_bat)
            source_tex_log = r'E:\document\PAPER\My_papering\common\idea_log.tex'
            target_tex_log = r'E:\document\PAPER\My_papering\{}\2_idea\idea_log.tex'.format(int(self.number_le.text()))
            if not os.path.exists(target_tex_log):
                shutil.copy(source_tex_log, target_tex_log)

    def open_idea(self):
        if len(self.number_le.text().strip()) > 0:
            path_root =  r'E:\document\PAPER\My_papering\{}\2_idea'.format(int(self.number_le.text()))
            os.system('start " " '+path_root)
            path_tex1 = r'E:\document\PAPER\My_papering\{}\2_idea\idea_generation.tex'.format(int(self.number_le.text()))
            path_tex2 = r'E:\document\PAPER\My_papering\{}\2_idea\idea_log.tex'.format(int(self.number_le.text()))
            os.system('start " " ' + path_tex1)
            os.system('start " " ' + path_tex2)

    def copy_technology(self):
        if len(self.number_le.text().strip()) > 0 :
            target_dir = r'E:\document\PAPER\My_papering\{}\3_technology'.format(int(self.number_le.text()))
            if not os.path.isdir(target_dir):
                os.makedirs(target_dir)
            source_idea_tex = r'E:\document\PAPER\My_papering\common\technical_plan.tex'
            target_idea_tex = r'E:\document\PAPER\My_papering\{}\3_technology\technical_plan.tex'.format(int(self.number_le.text()))
            if not os.path.exists(target_idea_tex):
                shutil.copy(source_idea_tex,target_idea_tex)
            source_tex_bat = r'E:\document\PAPER\My_papering\common\del.bat'
            target_tex_bat = r'E:\document\PAPER\My_papering\{}\3_technology\del.bat'.format(int(self.number_le.text()))
            if not os.path.exists(target_tex_bat):
                shutil.copy(source_tex_bat, target_tex_bat)
            source_tex_log = r'E:\document\PAPER\My_papering\common\design_flow_chart.pptx'
            target_tex_log = r'E:\document\PAPER\My_papering\{}\3_technology\design_flow_chart.pptx'.format(int(self.number_le.text()))
            if not os.path.exists(target_tex_log):
                shutil.copy(source_tex_log, target_tex_log)

    def open_technology(self):
        if len(self.number_le.text().strip()) > 0:
            path_root =  r'E:\document\PAPER\My_papering\{}\3_technology'.format(int(self.number_le.text()))
            os.system('start " " '+path_root)
            path_ppt = r'E:\document\PAPER\My_papering\{}\3_technology\design_flow_chart.pptx'
            path_tex = r'E:\document\PAPER\My_papering\{}\3_technology\technical_plan.tex'
            os.system('start " " ' + path_ppt)
            os.system('start " " ' + path_tex)

    def copy_experiment(self):
        if len(self.number_le.text().strip()) > 0 :
            target_dir = r'E:\document\PAPER\My_papering\{}\4_experiment'.format(int(self.number_le.text()))
            if not os.path.isdir(target_dir):
                os.makedirs(target_dir)
            source_idea_tex = r'E:\document\PAPER\My_papering\common\analysis_result.tex'
            target_idea_tex = r'E:\document\PAPER\My_papering\{}\4_experiment\analysis_result.tex'.format(int(self.number_le.text()))
            if not os.path.exists(target_idea_tex):
                shutil.copy(source_idea_tex,target_idea_tex)
            source_tex_bat = r'E:\document\PAPER\My_papering\common\del.bat'
            target_tex_bat = r'E:\document\PAPER\My_papering\{}\4_experiment\del.bat'.format(int(self.number_le.text()))
            if not os.path.exists(target_tex_bat):
                shutil.copy(source_tex_bat, target_tex_bat)
            source_dir = r'E:\document\PAPER\My_papering\common\code'
            target_dir = r'E:\document\PAPER\My_papering\{}\4_experiment\code'.format(int(self.number_le.text()))
            if not os.path.isdir(target_dir):
                 shutil.copytree(source_dir, target_dir)

    def open_experiment(self):
        if len(self.number_le.text().strip()) > 0:
            path_root =  r'E:\document\PAPER\My_papering\{}\4_experiment'.format(int(self.number_le.text()))
            os.system('start " " '+path_root)

    def copy_writing(self):
        if len(self.number_le.text().strip()) > 0 :
            source_dir = r'E:\document\PAPER\My_papering\common\writing'
            target_dir = r'E:\document\PAPER\My_papering\{}\5_writing'.format(int(self.number_le.text()))
            if not os.path.isdir(target_dir):
                 shutil.copytree(source_dir, target_dir)

    def open_writing(self):
        if len(self.number_le.text().strip()) > 0:
            path_root = r'E:\document\PAPER\My_papering\{}\5_writing'.format(int(self.number_le.text()))
            os.system('start " " ' + path_root)

    def copy_fix_error(self):
        if len(self.number_le.text().strip()) > 0:
            source_dir = r'E:\document\PAPER\My_papering\common\fix_error'
            target_dir = r'E:\document\PAPER\My_papering\{}\6_fix_error'.format(int(self.number_le.text()))
            if not os.path.isdir(target_dir):
                shutil.copytree(source_dir, target_dir)

    def open_fix_error(self):
        if len(self.number_le.text().strip()) > 0:
            path_root = r'E:\document\PAPER\My_papering\{}\6_fix_error'.format(int(self.number_le.text()))
            os.system('start " " ' + path_root)

    def copy_contribution(self):
        if len(self.number_le.text().strip()) > 0:
            source_dir = r'E:\document\PAPER\My_papering\common\contribute'
            target_dir = r'E:\document\PAPER\My_papering\{}\7_contribute'.format(int(self.number_le.text()))
            if not os.path.isdir(target_dir):
                shutil.copytree(source_dir, target_dir)

    def open_contribution(self):
        if len(self.number_le.text().strip()) > 0:
            path_root = r'E:\document\PAPER\My_papering\{}\7_contribute'.format(int(self.number_le.text()))
            os.system('start " " ' + path_root)

    def copy_interaction(self):
        if len(self.number_le.text().strip()) > 0:
            source_dir = r'E:\document\PAPER\My_papering\common\interaction'
            target_dir = r'E:\document\PAPER\My_papering\{}\8_interaction'.format(int(self.number_le.text()))
            if not os.path.isdir(target_dir):
                shutil.copytree(source_dir, target_dir)

    def open_interaction(self):
        if len(self.number_le.text().strip()) > 0:
            path_root = r'E:\document\PAPER\My_papering\{}\8_interaction'.format(int(self.number_le.text()))
            os.system('start " " ' + path_root)

    def copy_end(self):
        if len(self.number_le.text().strip()) > 0:
            source_dir = r'E:\document\PAPER\My_papering\common\end'
            target_dir = r'E:\document\PAPER\My_papering\{}\9_end'.format(int(self.number_le.text()))
            if not os.path.isdir(target_dir):
                shutil.copytree(source_dir, target_dir)

    def open_end(self):
        if len(self.number_le.text().strip()) > 0:
            path_root = r'E:\document\PAPER\My_papering\{}\9_end'.format(int(self.number_le.text()))
            os.system('start " " ' + path_root)



    def preparation(self):
        self.copy_preparation()
        self.open_preparation()

    def idea_generation(self):
        self.copy_idea()
        self.open_idea()

    def technical_proposal(self):
        self.copy_technology()
        self.open_technology()

    def paper_program(self):
        self.copy_experiment()
        self.open_experiment()

    def paper_writing(self):
        self.copy_writing()
        self.open_writing()

    def fix_error(self):
        self.copy_fix_error()
        self.open_fix_error()

    def journal_contribution(self):
        self.copy_contribution()
        self.open_contribution()

    def review_interaction(self):
        self.copy_interaction()
        self.open_interaction()


    def aftertreatment(self):
        self.copy_end()
        self.open_end()

    def support_writing(self):
        self.show_writing_signal.emit()

    def support_English(self):
        pass

    def support_math(self):
        pass

if __name__ == '__main__':

    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)

    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    window = paper_pane()

    #2.2  展示控件
    window.show()

    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
