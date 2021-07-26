__author__='Syd'

from PyQt5.Qt import *
from matrix_record_mode import Ui_Form
import sys
import os
from datetime import datetime
import time


class matrix_record_pane(QWidget,Ui_Form):
    exit_matrix_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

    def section(self,gene_number,time_content,theme_content):
        generation_str = '\\section{Matrix '+ str(gene_number) + 'th generation}\n'
        update_time = '\\noindent \\textcolor{blue}{\\fontsize{12}{0}{一.系统更新时间:' + time_content +  '}}\\\\\n '
        theme = '\\noindent \\textcolor{red}{\\fontsize{12}{0}{二.系统新增主题:'+ theme_content +'}}\\\\\n'
        pattem_str = generation_str + update_time + theme
        return pattem_str

    def subsection(self,version_number,time_content,fun_list):
        number = len(fun_list)
        pattern_1 = '\\subsection{Matrix '+str(version_number) + ' version}\n'
        pattern_2 = '\\noindent \\textcolor{blue}{\\fontsize{12}{0}{1.功能完善时间:' + time_content + '}}\\\\\n'
        pattern_3 = '\\noindent \\textcolor{magenta}{\\fontsize{12}{0}{2.系统新增功能:}}\n'
        pattern_4 = '\\begin{itemize}\n'
        pattern_5_list = ['  \\item {}\n'] * number
        pattern_5 = ''
        for idx , line in enumerate(pattern_5_list):
            pattern_5 += line.format(fun_list[idx])
        pattern_6 = '\\end{itemize}\n'
        pattern = pattern_1 + pattern_2 + pattern_3 + pattern_4 + pattern_5 + pattern_6
        return pattern

    def deal_section(self):
        update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        section_list = []
        section_list.append(self.system_le1.text())
        section_list.append(self.system_le2.text())
        section_list.append(self.system_le3.text())
        section_list_deal = []
        section_content = ''
        for line in section_list:
            if line.strip():
                section_list_deal.append(line)
        if len(section_list_deal) > 0 :
            section_content = ','.join(section_list_deal)
        return update_time,section_content

    def deal_subsection(self):
        update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        section_list = []
        section_list.append(self.function_le1.text())
        section_list.append(self.function_le2.text())
        section_list.append(self.function_le3.text())
        section_list_deal = []
        for line in section_list:
            if line.strip():
                section_list_deal.append(line)
        return update_time, section_list_deal

    def write_tex(self,insert_content):
        path = r'E:\document\mind_data\Matrix_system\Matrix_system.tex'
        f_tex = open(path, 'r')
        tex_list = []
        for line in f_tex.readlines():
            tex_list.append(line)
        f_tex.close()
        tex_list.insert(-2, insert_content)
        f_wtex = open(path, 'w')
        for line in tex_list:
            f_wtex.write(line)
        f_wtex.close()


    def generation_number(self):
        path = r'E:\document\mind_data\Matrix_system\Matrix_system.tex'
        f_tex = open(path, 'r')
        tex_list = []
        for line in f_tex.readlines():
            if 'generation' in line:
                deal_line = line.strip().split(' ')
                tex_list.append(deal_line[1])
        generation_number = int(tex_list[-1][0])
        next_nubmer = generation_number + 1
        return generation_number, next_nubmer

    def version_number(self):
        path = r'E:\document\mind_data\Matrix_system\Matrix_system.tex'
        f_tex = open(path, 'r')
        tex_list = []
        for line in f_tex.readlines():
            if 'version' in line:
                deal_line = line.strip().split(' ')
                tex_list.append(deal_line[1])
        generation_number , _ = self.generation_number()
        if generation_number == int(float(tex_list[-1])):
            version_number = float(tex_list[-1]) + 0.1
            version_number = round(version_number,2)
        else:
            version_number = round(float(generation_number),2)
        return version_number

    def write_log(self,starttime,crashtime,normal_hours,normal_minutes,justify_hours,justify_minutes):
        fr = open(r'E:\document\mind_data\Matrix_system\timetable.txt')
        record = 0
        for idx, line in enumerate(fr.readlines()):
            record = idx
        str_template = 'Matrix {}th generation'
        number = (record + 1) / 5 + 1
        list_1 = [str_template.format(int(number)), '起始时间:'+starttime, '崩溃时间:'+crashtime]
        list_2 = ['正常运行:{}小时 {}分钟'.format(normal_hours,normal_minutes),'恢复调整:{}小时 {}分钟'.format(justify_hours,justify_minutes)]
        list_total = list_1 + list_2
        f_w = open(r'E:\document\mind_data\Matrix_system\timetable.txt', 'a')
        for line in list_total:
            f_w.write(line)
            f_w.write('\n')
        f_w.close()

    def submit_system(self):
        if self.system_le1.text().strip() or self.system_le2.text().strip() or self.system_le3.text().strip():
            #写入latex文档中
            update_time ,section_content = self.deal_section()
            _ , next_number = self.generation_number()
            pattern_str = self.section(next_number,update_time,section_content)
            self.write_tex(pattern_str)
            #计算系统的巡行时间和调整时间
            start_time = self.system_timetable()[-2]
            path_crash = r'E:\document\mind_data\Matrix_system\crash_timepoint.txt'
            f_crash = open(path_crash,'r')
            crash_list = []
            for line in f_crash.readlines():
                if len(line.strip().split('#'))>1:
                    crash_list.append(line.strip().split('#')[1])
            crash_time = crash_list[-1]
            normal_hours,normal_minutes = self.calcu_runtime(start_time,crash_time)
            justify_hours,justify_minutes = self.calcu_runtime(crash_time,update_time)
            self.write_log(start_time,crash_time,normal_hours,normal_minutes,justify_hours,justify_minutes)
            time.sleep(1)
            cmd_tex_path = r'E:\program\cmd\program\Matrix_system.bat'
            os.system(cmd_tex_path)
            cmd_txt_path = r'E:\program\cmd\program\timelog.bat'
            os.system(cmd_txt_path)
        else:
            pass

    def submit_function(self):
        if self.function_le1.text().strip() or self.function_le2.text().strip() or self.function_le3.text().strip():
            cmd_path = r'E:\program\cmd\program\Matrix_system.bat'
            update_time, section_list_deal = self.deal_subsection()
            version_number = self.version_number()
            pattern_str = self.subsection(version_number,update_time,section_list_deal)
            self.write_tex(pattern_str)
            time.sleep(1)
            os.system(cmd_path)
        else:
            pass

    def calcu_runtime(self,start, end):
        start_datetime = datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
        end_datetime = datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
        runtime = str(end_datetime - start_datetime)
        if len(runtime.strip().split(' '))>2:
            day = runtime.strip().split(' ')[0]
            hour = runtime.strip().split(' ')[2][0]
            minute = runtime.strip().split(':')[1]
        else:
            day = 0
            hour = runtime.strip().split(':')[0]
            minute = runtime.strip().split(':')[1]
        hours = int(day) * 24 + int(hour) + float(minute) / 60.0
        minutes = int(day) * 24 * 60 + int(hour) * 60 + int(minute)
        hours = round(hours, 2)
        return hours, minutes

    def system_timetable(self):
        path = r'E:\document\mind_data\Matrix_system\Matrix_system.tex'
        f_tex = open(path, 'r')
        time_list = []
        for line in f_tex.readlines():
            if '系统更新时间' in line:
                deal_line = line.strip().split('间:')[1].split('}')[0]
                time_list.append(deal_line)
        return time_list

    def exit_matrix_record(self):
        self.exit_matrix_signal.emit()

    #计算系统正常运行的时间
    def explosion(self):
        explosion_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        path_timepoint = r'E:\document\mind_data\Matrix_system\crash_timepoint.txt'
        f_r = open(path_timepoint, 'r')
        record_idx = 0
        for line in f_r.readlines():
            record_idx += 1
        f_r.close()
        f_point = open(path_timepoint,'a')
        f_point.write('{}th#'.format(record_idx+1)+explosion_time)
        f_point.write('\n')
        f_point.close()
        path_think = r'E:\document\mind_data\Solving_idea.txt'
        os.system('start "" '+path_think)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 2 控件的操作
    # 2.1 创建控件，设置控件(大小，位置，样式)
    window = matrix_record_pane()

    # 2.2  展示控件
    window.show()

    # 3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())








