

__author__='Syd'

from PyQt5.Qt import *
import sys

from main_pane import Main_Pane
from program_pane import program_pane
from bat_pane import bat_pane
from paper_pane import paper_pane
from mind_pane import mind_pane
from plan_split_pane import plan_split_pane
from challenge_pane import challenge_pane
from paper_create_pane import paper_create_pane
from matrix_record_pane import matrix_record_pane
from talk_solve_pane import talk_solve_pane
from writing_pane import writing_pane

if __name__ == '__main__':

    #1 创建应用程序，接受命令行启动
    app = QApplication(sys.argv)

    #2 控件的操作
    #2.1 创建控件，设置控件(大小，位置，样式)
    #主界面到program界面
    main_pane = Main_Pane()
    program_pane = program_pane(main_pane)
    program_pane.move(0,main_pane.height())
    program_pane.show()

    talk_solve_pane = talk_solve_pane(main_pane)
    talk_solve_pane.move(0, main_pane.height())
    talk_solve_pane.show()

    mind_pane = mind_pane(main_pane)
    mind_pane.move(0,main_pane.height())
    mind_pane.show()

    matrix_record_pane = matrix_record_pane(mind_pane)
    matrix_record_pane.move(0, mind_pane.height())
    matrix_record_pane.show()

    paper_pane = paper_pane(main_pane)
    paper_pane.move(0,main_pane.height())
    paper_pane.show()

    writing_pane = writing_pane(paper_pane)
    writing_pane.move(0, paper_pane.height())
    writing_pane.show()

    paper_create_pane = paper_create_pane(paper_pane)
    paper_create_pane.move(0, paper_pane.height())
    paper_create_pane.show()

    #program界面到bat界面
    bat_pane = bat_pane(program_pane)
    bat_pane.move(0, program_pane.height())
    bat_pane.show()

    plan_split_pane = plan_split_pane(mind_pane)
    plan_split_pane.move(0,mind_pane.height())
    plan_split_pane.show()

    challenge_pane = challenge_pane(mind_pane)
    challenge_pane.move(0, mind_pane.height())
    challenge_pane.show()

    #2.2  展示控件
    main_pane.show()

    def show_program_pane():
        animation = QPropertyAnimation(program_pane)
        animation.setTargetObject(program_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(program_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_program_pane():
        animation = QPropertyAnimation(program_pane)
        animation.setTargetObject(program_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(main_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)


    def show_bat_pane():
        print("展示程序界面")
        animation = QPropertyAnimation(bat_pane)
        animation.setTargetObject(bat_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(bat_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_bat_pane():
        animation = QPropertyAnimation(bat_pane)
        animation.setTargetObject(bat_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(program_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)


    def show_paper_pane():
        print("展示程序界面")
        animation = QPropertyAnimation(paper_pane)
        animation.setTargetObject(paper_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(paper_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_paper_pane():
        animation = QPropertyAnimation(paper_pane)
        animation.setTargetObject(paper_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(main_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_mind_pane():
        animation = QPropertyAnimation(mind_pane)
        animation.setTargetObject(mind_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(mind_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_mind_pane():
        animation = QPropertyAnimation(mind_pane)
        animation.setTargetObject(mind_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(main_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_plan_split_pane():
        print("展示程序界面")
        animation = QPropertyAnimation(plan_split_pane)
        animation.setTargetObject(plan_split_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(plan_split_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_plan_split_pane():
        animation = QPropertyAnimation(plan_split_pane)
        animation.setTargetObject(plan_split_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(mind_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_warn_notice_pane():
        print("展示warn界面")
        animation = QPropertyAnimation(challenge_pane)
        animation.setTargetObject(challenge_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(challenge_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_warn_notice_pane():
        animation = QPropertyAnimation(challenge_pane)
        animation.setTargetObject(challenge_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(mind_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_paper_create_pane():
        print("展示warn界面")
        animation = QPropertyAnimation(paper_create_pane)
        animation.setTargetObject(paper_create_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(paper_create_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_paper_create_pane():
        animation = QPropertyAnimation(paper_create_pane)
        animation.setTargetObject(paper_create_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(paper_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_matrix_record_pane():
        animation = QPropertyAnimation(matrix_record_pane)
        animation.setTargetObject(matrix_record_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(matrix_record_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_writing_pane():
        animation = QPropertyAnimation(writing_pane)
        animation.setTargetObject(writing_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(writing_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_matrix_record_pane():
        animation = QPropertyAnimation(matrix_record_pane)
        animation.setTargetObject(matrix_record_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(mind_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_writing_pane():
        animation = QPropertyAnimation(writing_pane)
        animation.setTargetObject(writing_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(paper_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_talk_solve_pane():
        animation = QPropertyAnimation(talk_solve_pane)
        animation.setTargetObject(talk_solve_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(talk_solve_pane.pos())
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_talk_solve_pane():
        animation = QPropertyAnimation(talk_solve_pane)
        animation.setTargetObject(talk_solve_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(main_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    main_pane.show_mind_pane_signal.connect(show_mind_pane)
    mind_pane.exit_mind_signal.connect(exit_mind_pane)
    main_pane.show_paper_pane_signal.connect(show_paper_pane)
    paper_pane.exit_paper_signal.connect(exit_paper_pane)
    main_pane.show_program_pane_signal.connect(show_program_pane)
    program_pane.exit_program_signal.connect(exit_program_pane)
    bat_pane.exit_bat_signal.connect(exit_bat_pane)
    program_pane.show_bat_signal.connect(show_bat_pane)
    plan_split_pane.exit_plan_split_signal.connect(exit_plan_split_pane)
    mind_pane.show_plan_split_signal.connect(show_plan_split_pane)
    challenge_pane.exit_challenge_signal.connect(exit_warn_notice_pane)
    mind_pane.show_challenge_signal.connect(show_warn_notice_pane)
    paper_pane.show_create_pane_signal.connect(show_paper_create_pane)
    paper_create_pane.exit_create_signal.connect(exit_paper_create_pane)
    mind_pane.show_matrix_system_signal.connect(show_matrix_record_pane)
    matrix_record_pane.exit_matrix_signal.connect(exit_matrix_record_pane)
    talk_solve_pane.exit_talk_solve_signal.connect(exit_talk_solve_pane)
    main_pane.show_together_singnal.connect(show_talk_solve_pane)
    paper_pane.show_writing_signal.connect(show_writing_pane)
    writing_pane.exit_writing_signal.connect(exit_writing_pane)

    #3 app.exec_() 让整个程序开始执行，可以让窗口一直循环
    sys.exit(app.exec_())
