# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1182, 576)
        MainWindow.setStyleSheet(_fromUtf8("background-color: #263238;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 110, 1101, 421))
        self.frame.setStyleSheet(_fromUtf8("border: 2px solid #78909c ;\n"
"border-radius: 2px;"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.button_coma = QtGui.QPushButton(self.frame)
        self.button_coma.setGeometry(QtCore.QRect(810, 190, 81, 71))
        self.button_coma.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #455a64;\n"
"color: #455a64;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_coma.setObjectName(_fromUtf8("button_coma"))
        self.button_v = QtGui.QPushButton(self.frame)
        self.button_v.setGeometry(QtCore.QRect(410, 190, 81, 71))
        self.button_v.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #455a64;\n"
"color: #455a64;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
"\n"
""))
        self.button_v.setObjectName(_fromUtf8("button_v"))
        self.button_x = QtGui.QPushButton(self.frame)
        self.button_x.setGeometry(QtCore.QRect(210, 190, 81, 71))
        self.button_x.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_x.setObjectName(_fromUtf8("button_x"))
        self.button_a = QtGui.QPushButton(self.frame)
        self.button_a.setGeometry(QtCore.QRect(60, 110, 81, 71))
        self.button_a.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_a.setObjectName(_fromUtf8("button_a"))
        self.button_n = QtGui.QPushButton(self.frame)
        self.button_n.setGeometry(QtCore.QRect(610, 190, 81, 71))
        self.button_n.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_n.setObjectName(_fromUtf8("button_n"))
        self.button_b = QtGui.QPushButton(self.frame)
        self.button_b.setGeometry(QtCore.QRect(510, 190, 81, 71))
        self.button_b.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #455a64;\n"
"color: #455a64;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_b.setObjectName(_fromUtf8("button_b"))
        self.button_z = QtGui.QPushButton(self.frame)
        self.button_z.setGeometry(QtCore.QRect(110, 190, 81, 71))
        self.button_z.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_z.setObjectName(_fromUtf8("button_z"))
        self.button_i = QtGui.QPushButton(self.frame)
        self.button_i.setGeometry(QtCore.QRect(740, 30, 81, 71))
        self.button_i.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_i.setObjectName(_fromUtf8("button_i"))
        self.button_j = QtGui.QPushButton(self.frame)
        self.button_j.setGeometry(QtCore.QRect(660, 110, 81, 71))
        self.button_j.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_j.setObjectName(_fromUtf8("button_j"))
        self.button_punto_coma = QtGui.QPushButton(self.frame)
        self.button_punto_coma.setGeometry(QtCore.QRect(960, 110, 81, 71))
        self.button_punto_coma.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_punto_coma.setObjectName(_fromUtf8("button_punto_coma"))
        self.button_c = QtGui.QPushButton(self.frame)
        self.button_c.setGeometry(QtCore.QRect(310, 190, 81, 71))
        self.button_c.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #455a64;\n"
"color: #455a64;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_c.setObjectName(_fromUtf8("button_c"))
        self.button_p = QtGui.QPushButton(self.frame)
        self.button_p.setGeometry(QtCore.QRect(940, 30, 81, 71))
        self.button_p.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_p.setObjectName(_fromUtf8("button_p"))
        self.button_s = QtGui.QPushButton(self.frame)
        self.button_s.setGeometry(QtCore.QRect(160, 110, 81, 71))
        self.button_s.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_s.setObjectName(_fromUtf8("button_s"))
        self.button_y = QtGui.QPushButton(self.frame)
        self.button_y.setGeometry(QtCore.QRect(540, 30, 81, 71))
        self.button_y.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #455a64;\n"
"color: #455a64;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_y.setObjectName(_fromUtf8("button_y"))
        self.button_u = QtGui.QPushButton(self.frame)
        self.button_u.setGeometry(QtCore.QRect(640, 30, 81, 71))
        self.button_u.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_u.setObjectName(_fromUtf8("button_u"))
        self.button_g = QtGui.QPushButton(self.frame)
        self.button_g.setGeometry(QtCore.QRect(460, 110, 81, 71))
        self.button_g.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #455a64;\n"
"color: #455a64;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_g.setObjectName(_fromUtf8("button_g"))
        self.button_k = QtGui.QPushButton(self.frame)
        self.button_k.setGeometry(QtCore.QRect(760, 110, 81, 71))
        self.button_k.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_k.setObjectName(_fromUtf8("button_k"))
        self.button_l = QtGui.QPushButton(self.frame)
        self.button_l.setGeometry(QtCore.QRect(860, 110, 81, 71))
        self.button_l.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_l.setObjectName(_fromUtf8("button_l"))
        self.button_d = QtGui.QPushButton(self.frame)
        self.button_d.setGeometry(QtCore.QRect(260, 110, 81, 71))
        self.button_d.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_d.setObjectName(_fromUtf8("button_d"))
        self.button_f = QtGui.QPushButton(self.frame)
        self.button_f.setGeometry(QtCore.QRect(360, 110, 81, 71))
        self.button_f.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_f.setObjectName(_fromUtf8("button_f"))
        self.button_o = QtGui.QPushButton(self.frame)
        self.button_o.setGeometry(QtCore.QRect(840, 30, 81, 71))
        self.button_o.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_o.setObjectName(_fromUtf8("button_o"))
        self.button_q = QtGui.QPushButton(self.frame)
        self.button_q.setGeometry(QtCore.QRect(40, 30, 81, 71))
        self.button_q.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_q.setObjectName(_fromUtf8("button_q"))
        self.button_h = QtGui.QPushButton(self.frame)
        self.button_h.setGeometry(QtCore.QRect(560, 110, 81, 71))
        self.button_h.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #455a64;\n"
"color: #455a64;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_h.setObjectName(_fromUtf8("button_h"))
        self.button_e = QtGui.QPushButton(self.frame)
        self.button_e.setGeometry(QtCore.QRect(240, 30, 81, 71))
        self.button_e.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_e.setObjectName(_fromUtf8("button_e"))
        self.button_m = QtGui.QPushButton(self.frame)
        self.button_m.setGeometry(QtCore.QRect(710, 190, 81, 71))
        self.button_m.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #455a64;\n"
"color: #455a64;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_m.setObjectName(_fromUtf8("button_m"))
        self.button_space = QtGui.QPushButton(self.frame)
        self.button_space.setGeometry(QtCore.QRect(240, 320, 611, 71))
        self.button_space.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
"cursor: pointer;"))
        self.button_space.setObjectName(_fromUtf8("button_space"))
        self.button_r = QtGui.QPushButton(self.frame)
        self.button_r.setGeometry(QtCore.QRect(340, 30, 81, 71))
        self.button_r.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_r.setObjectName(_fromUtf8("button_r"))
        self.button_w = QtGui.QPushButton(self.frame)
        self.button_w.setGeometry(QtCore.QRect(140, 30, 81, 71))
        self.button_w.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_w.setObjectName(_fromUtf8("button_w"))
        self.button_t = QtGui.QPushButton(self.frame)
        self.button_t.setGeometry(QtCore.QRect(440, 30, 81, 71))
        self.button_t.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #455a64;\n"
"color: #455a64;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_t.setObjectName(_fromUtf8("button_t"))
        self.label_workit = QtGui.QLabel(self.frame)
        self.label_workit.setGeometry(QtCore.QRect(50, 40, 51, 16))
        self.label_workit.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_workit.setObjectName(_fromUtf8("label_workit"))
        self.label_makeit = QtGui.QLabel(self.frame)
        self.label_makeit.setGeometry(QtCore.QRect(150, 40, 51, 16))
        self.label_makeit.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_makeit.setObjectName(_fromUtf8("label_makeit"))
        self.label_doit = QtGui.QLabel(self.frame)
        self.label_doit.setGeometry(QtCore.QRect(260, 40, 41, 16))
        self.label_doit.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_doit.setObjectName(_fromUtf8("label_doit"))
        self.label_makeus = QtGui.QLabel(self.frame)
        self.label_makeus.setGeometry(QtCore.QRect(350, 40, 51, 16))
        self.label_makeus.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_makeus.setObjectName(_fromUtf8("label_makeus"))
        self.label_morethan = QtGui.QLabel(self.frame)
        self.label_morethan.setGeometry(QtCore.QRect(650, 40, 61, 20))
        self.label_morethan.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_morethan.setObjectName(_fromUtf8("label_morethan"))
        self.label_hour = QtGui.QLabel(self.frame)
        self.label_hour.setGeometry(QtCore.QRect(760, 40, 41, 16))
        self.label_hour.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_hour.setObjectName(_fromUtf8("label_hour"))
        self.label_our = QtGui.QLabel(self.frame)
        self.label_our.setGeometry(QtCore.QRect(860, 40, 41, 16))
        self.label_our.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_our.setObjectName(_fromUtf8("label_our"))
        self.label_never = QtGui.QLabel(self.frame)
        self.label_never.setGeometry(QtCore.QRect(960, 40, 51, 16))
        self.label_never.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_never.setObjectName(_fromUtf8("label_never"))
        self.label_normal = QtGui.QLabel(self.frame)
        self.label_normal.setGeometry(QtCore.QRect(120, 200, 51, 16))
        self.label_normal.setStyleSheet(_fromUtf8("border-radius: 5px;\n"
"background-color: #78909c;\n"
"border: 1px solid #263238;\n"
"color: #263238;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;\n"
""))
        self.label_normal.setObjectName(_fromUtf8("label_normal"))
        self.label_better = QtGui.QLabel(self.frame)
        self.label_better.setGeometry(QtCore.QRect(170, 120, 51, 16))
        self.label_better.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_better.setObjectName(_fromUtf8("label_better"))
        self.label_faster = QtGui.QLabel(self.frame)
        self.label_faster.setGeometry(QtCore.QRect(270, 120, 51, 16))
        self.label_faster.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_faster.setObjectName(_fromUtf8("label_faster"))
        self.label_stronger = QtGui.QLabel(self.frame)
        self.label_stronger.setGeometry(QtCore.QRect(370, 120, 61, 16))
        self.label_stronger.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_stronger.setObjectName(_fromUtf8("label_stronger"))
        self.label_ever = QtGui.QLabel(self.frame)
        self.label_ever.setGeometry(QtCore.QRect(680, 120, 31, 16))
        self.label_ever.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_ever.setObjectName(_fromUtf8("label_ever"))
        self.label_workits = QtGui.QLabel(self.frame)
        self.label_workits.setGeometry(QtCore.QRect(870, 120, 51, 20))
        self.label_workits.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_workits.setObjectName(_fromUtf8("label_workits"))
        self.label_after = QtGui.QLabel(self.frame)
        self.label_after.setGeometry(QtCore.QRect(780, 120, 41, 16))
        self.label_after.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_after.setObjectName(_fromUtf8("label_after"))
        self.label_over = QtGui.QLabel(self.frame)
        self.label_over.setGeometry(QtCore.QRect(980, 120, 41, 20))
        self.label_over.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_over.setObjectName(_fromUtf8("label_over"))
        self.label_hight = QtGui.QLabel(self.frame)
        self.label_hight.setGeometry(QtCore.QRect(230, 200, 41, 16))
        self.label_hight.setStyleSheet(_fromUtf8("border-radius: 5px;\n"
"background-color: #78909c;\n"
"border: 1px solid #263238;\n"
"color: #263238;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;\n"
""))
        self.label_hight.setObjectName(_fromUtf8("label_hight"))
        self.label_low = QtGui.QLabel(self.frame)
        self.label_low.setGeometry(QtCore.QRect(630, 200, 31, 16))
        self.label_low.setStyleSheet(_fromUtf8("border-radius: 5px;\n"
"background-color: #78909c;\n"
"border: 1px solid #263238;\n"
"color: #263238;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;\n"
""))
        self.label_low.setObjectName(_fromUtf8("label_low"))
        self.label_harder = QtGui.QLabel(self.frame)
        self.label_harder.setGeometry(QtCore.QRect(70, 120, 51, 16))
        self.label_harder.setStyleSheet(_fromUtf8("background-color: #263238;\n"
"border: 1px solid #263238;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 11px;"))
        self.label_harder.setObjectName(_fromUtf8("label_harder"))
        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(340, 30, 491, 41))
        self.titulo.setStyleSheet(_fromUtf8("color: #78909c;\n"
"font-family: Verdana;\n"
"font-size: 35px;\n"
""))
        self.titulo.setObjectName(_fromUtf8("titulo"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Launchpy by Carmoreno", None))
        self.button_coma.setText(_translate("MainWindow", ",", None))
        self.button_v.setText(_translate("MainWindow", "V", None))
        self.button_x.setText(_translate("MainWindow", "X", None))
        self.button_a.setText(_translate("MainWindow", "A", None))
        self.button_n.setText(_translate("MainWindow", "N", None))
        self.button_b.setText(_translate("MainWindow", "B", None))
        self.button_z.setText(_translate("MainWindow", "Z", None))
        self.button_i.setText(_translate("MainWindow", "I", None))
        self.button_j.setText(_translate("MainWindow", "J", None))
        self.button_punto_coma.setText(_translate("MainWindow", ";", None))
        self.button_c.setText(_translate("MainWindow", "C", None))
        self.button_p.setText(_translate("MainWindow", "P", None))
        self.button_s.setText(_translate("MainWindow", "S", None))
        self.button_y.setText(_translate("MainWindow", "Y", None))
        self.button_u.setText(_translate("MainWindow", "U", None))
        self.button_g.setText(_translate("MainWindow", "G", None))
        self.button_k.setText(_translate("MainWindow", "K", None))
        self.button_l.setText(_translate("MainWindow", "L", None))
        self.button_d.setText(_translate("MainWindow", "D", None))
        self.button_f.setText(_translate("MainWindow", "F", None))
        self.button_o.setText(_translate("MainWindow", "O", None))
        self.button_q.setText(_translate("MainWindow", "Q", None))
        self.button_h.setText(_translate("MainWindow", "H", None))
        self.button_e.setText(_translate("MainWindow", "E", None))
        self.button_m.setText(_translate("MainWindow", "M", None))
        self.button_space.setText(_translate("MainWindow", "Instrumental ♪", None))
        self.button_r.setText(_translate("MainWindow", "R", None))
        self.button_w.setText(_translate("MainWindow", "W", None))
        self.button_t.setText(_translate("MainWindow", "T", None))
        self.label_workit.setText(_translate("MainWindow", "Work it", None))
        self.label_makeit.setText(_translate("MainWindow", "Make it", None))
        self.label_doit.setText(_translate("MainWindow", "Do it", None))
        self.label_makeus.setText(_translate("MainWindow", "Make us", None))
        self.label_morethan.setText(_translate("MainWindow", "More than", None))
        self.label_hour.setText(_translate("MainWindow", "Hour", None))
        self.label_our.setText(_translate("MainWindow", "Our", None))
        self.label_never.setText(_translate("MainWindow", "Never", None))
        self.label_normal.setText(_translate("MainWindow", "Normal", None))
        self.label_better.setText(_translate("MainWindow", "Better", None))
        self.label_faster.setText(_translate("MainWindow", "Faster", None))
        self.label_stronger.setText(_translate("MainWindow", "Stronger", None))
        self.label_ever.setText(_translate("MainWindow", "Ever", None))
        self.label_workits.setText(_translate("MainWindow", "Work its", None))
        self.label_after.setText(_translate("MainWindow", "After", None))
        self.label_over.setText(_translate("MainWindow", "Over", None))
        self.label_hight.setText(_translate("MainWindow", "Hight", None))
        self.label_low.setText(_translate("MainWindow", "Low", None))
        self.label_harder.setText(_translate("MainWindow", "Harder", None))
        self.titulo.setText(_translate("MainWindow", "Harder Better Faster ... ♪♫", None))

