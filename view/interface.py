# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'console.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from styles import estilos
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
        MainWindow.setFixedSize(1260, 575)
        MainWindow.setStyleSheet(_fromUtf8(estilos))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frameButtons = QtGui.QFrame(self.centralwidget)
        self.frameButtons.setGeometry(QtCore.QRect(30, 110, 1201, 421))
        self.frameButtons.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frameButtons.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameButtons.setFrameShadow(QtGui.QFrame.Raised)
        self.frameButtons.setObjectName(_fromUtf8("frameButtons"))
        self.button_w = QtGui.QPushButton(self.frameButtons)
        self.button_w.setGeometry(QtCore.QRect(160, 30, 91, 71))
        self.button_w.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_w.setObjectName(_fromUtf8("button_w"))
        self.button_o = QtGui.QPushButton(self.frameButtons)
        self.button_o.setGeometry(QtCore.QRect(930, 30, 91, 71))
        self.button_o.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_o.setObjectName(_fromUtf8("button_o"))
        self.button_i = QtGui.QPushButton(self.frameButtons)
        self.button_i.setGeometry(QtCore.QRect(820, 30, 91, 71))
        self.button_i.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_i.setObjectName(_fromUtf8("button_i"))
        self.button_u = QtGui.QPushButton(self.frameButtons)
        self.button_u.setGeometry(QtCore.QRect(710, 30, 91, 71))
        self.button_u.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_u.setObjectName(_fromUtf8("button_u"))
        self.button_y = QtGui.QPushButton(self.frameButtons)
        self.button_y.setGeometry(QtCore.QRect(600, 30, 91, 71))
        self.button_y.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_y.setObjectName(_fromUtf8("button_y"))
        self.button_t = QtGui.QPushButton(self.frameButtons)
        self.button_t.setGeometry(QtCore.QRect(490, 30, 91, 71))
        self.button_t.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_t.setObjectName(_fromUtf8("button_t"))
        self.button_r = QtGui.QPushButton(self.frameButtons)
        self.button_r.setGeometry(QtCore.QRect(380, 30, 91, 71))
        self.button_r.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_r.setObjectName(_fromUtf8("button_r"))
        self.button_e = QtGui.QPushButton(self.frameButtons)
        self.button_e.setGeometry(QtCore.QRect(270, 30, 91, 71))
        self.button_e.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_e.setObjectName(_fromUtf8("button_e"))
        self.button_p = QtGui.QPushButton(self.frameButtons)
        self.button_p.setGeometry(QtCore.QRect(1040, 30, 91, 71))
        self.button_p.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_p.setObjectName(_fromUtf8("button_p"))
        self.button_a = QtGui.QPushButton(self.frameButtons)
        self.button_a.setGeometry(QtCore.QRect(80, 120, 91, 71))
        self.button_a.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_a.setObjectName(_fromUtf8("button_a"))
        self.button_g = QtGui.QPushButton(self.frameButtons)
        self.button_g.setGeometry(QtCore.QRect(520, 120, 91, 71))
        self.button_g.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_g.setObjectName(_fromUtf8("button_g"))
        self.button_f = QtGui.QPushButton(self.frameButtons)
        self.button_f.setGeometry(QtCore.QRect(410, 120, 91, 71))
        self.button_f.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_f.setObjectName(_fromUtf8("button_f"))
        self.button_d = QtGui.QPushButton(self.frameButtons)
        self.button_d.setGeometry(QtCore.QRect(300, 120, 91, 71))
        self.button_d.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_d.setObjectName(_fromUtf8("button_d"))
        self.button_s = QtGui.QPushButton(self.frameButtons)
        self.button_s.setGeometry(QtCore.QRect(190, 120, 91, 71))
        self.button_s.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_s.setObjectName(_fromUtf8("button_s"))
        self.button_z = QtGui.QPushButton(self.frameButtons)
        self.button_z.setGeometry(QtCore.QRect(110, 210, 91, 71))
        self.button_z.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_z.setObjectName(_fromUtf8("button_z"))
        self.button_punto_coma = QtGui.QPushButton(self.frameButtons)
        self.button_punto_coma.setGeometry(QtCore.QRect(1070, 120, 91, 71))
        self.button_punto_coma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_punto_coma.setObjectName(_fromUtf8("button_punto_coma"))
        self.button_l = QtGui.QPushButton(self.frameButtons)
        self.button_l.setGeometry(QtCore.QRect(960, 120, 91, 71))
        self.button_l.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_l.setObjectName(_fromUtf8("button_l"))
        self.button_k = QtGui.QPushButton(self.frameButtons)
        self.button_k.setGeometry(QtCore.QRect(850, 120, 91, 71))
        self.button_k.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_k.setObjectName(_fromUtf8("button_k"))
        self.button_j = QtGui.QPushButton(self.frameButtons)
        self.button_j.setGeometry(QtCore.QRect(740, 120, 91, 71))
        self.button_j.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_j.setObjectName(_fromUtf8("button_j"))
        self.button_h = QtGui.QPushButton(self.frameButtons)
        self.button_h.setGeometry(QtCore.QRect(630, 120, 91, 71))
        self.button_h.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_h.setObjectName(_fromUtf8("button_h"))
        self.button_x = QtGui.QPushButton(self.frameButtons)
        self.button_x.setGeometry(QtCore.QRect(220, 210, 91, 71))
        self.button_x.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_x.setObjectName(_fromUtf8("button_x"))
        self.button_c = QtGui.QPushButton(self.frameButtons)
        self.button_c.setGeometry(QtCore.QRect(330, 210, 91, 71))
        self.button_c.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_c.setObjectName(_fromUtf8("button_c"))
        self.button_v = QtGui.QPushButton(self.frameButtons)
        self.button_v.setGeometry(QtCore.QRect(440, 210, 91, 71))
        self.button_v.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_v.setObjectName(_fromUtf8("button_v"))
        self.button_b = QtGui.QPushButton(self.frameButtons)
        self.button_b.setGeometry(QtCore.QRect(550, 210, 91, 71))
        self.button_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_b.setObjectName(_fromUtf8("button_b"))
        self.button_n = QtGui.QPushButton(self.frameButtons)
        self.button_n.setGeometry(QtCore.QRect(660, 210, 91, 71))
        self.button_n.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_n.setObjectName(_fromUtf8("button_n"))
        self.button_m = QtGui.QPushButton(self.frameButtons)
        self.button_m.setGeometry(QtCore.QRect(770, 210, 91, 71))
        self.button_m.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_m.setObjectName(_fromUtf8("button_m"))
        self.button_coma = QtGui.QPushButton(self.frameButtons)
        self.button_coma.setGeometry(QtCore.QRect(880, 210, 91, 71))
        self.button_coma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_coma.setObjectName(_fromUtf8("button_coma"))
        self.button_space = QtGui.QPushButton(self.frameButtons)
        self.button_space.setGeometry(QtCore.QRect(300, 320, 591, 71))
        self.button_space.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_space.setObjectName(_fromUtf8("button_space"))
        self.label_makeit = QtGui.QLabel(self.frameButtons)
        self.label_makeit.setGeometry(QtCore.QRect(180, 40, 41, 16))
        self.label_makeit.setStyleSheet(_fromUtf8(""))
        self.label_makeit.setObjectName(_fromUtf8("label_makeit"))
        self.label_doit = QtGui.QLabel(self.frameButtons)
        self.label_doit.setGeometry(QtCore.QRect(300, 40, 41, 16))
        self.label_doit.setStyleSheet(_fromUtf8(""))
        self.label_doit.setObjectName(_fromUtf8("label_doit"))
        self.label_makeus = QtGui.QLabel(self.frameButtons)
        self.label_makeus.setGeometry(QtCore.QRect(400, 40, 51, 16))
        self.label_makeus.setStyleSheet(_fromUtf8(""))
        self.label_makeus.setObjectName(_fromUtf8("label_makeus"))
        self.label_morethan = QtGui.QLabel(self.frameButtons)
        self.label_morethan.setGeometry(QtCore.QRect(720, 40, 61, 16))
        self.label_morethan.setStyleSheet(_fromUtf8(""))
        self.label_morethan.setObjectName(_fromUtf8("label_morethan"))
        self.label_hour = QtGui.QLabel(self.frameButtons)
        self.label_hour.setGeometry(QtCore.QRect(850, 40, 31, 16))
        self.label_hour.setStyleSheet(_fromUtf8(""))
        self.label_hour.setObjectName(_fromUtf8("label_hour"))
        self.label_our = QtGui.QLabel(self.frameButtons)
        self.label_our.setGeometry(QtCore.QRect(960, 40, 31, 16))
        self.label_our.setStyleSheet(_fromUtf8(""))
        self.label_our.setObjectName(_fromUtf8("label_our"))
        self.label_never = QtGui.QLabel(self.frameButtons)
        self.label_never.setGeometry(QtCore.QRect(1060, 40, 41, 16))
        self.label_never.setStyleSheet(_fromUtf8(""))
        self.label_never.setObjectName(_fromUtf8("label_never"))
        self.label_harder = QtGui.QLabel(self.frameButtons)
        self.label_harder.setGeometry(QtCore.QRect(100, 130, 41, 16))
        self.label_harder.setStyleSheet(_fromUtf8(""))
        self.label_harder.setObjectName(_fromUtf8("label_harder"))
        self.label_better = QtGui.QLabel(self.frameButtons)
        self.label_better.setGeometry(QtCore.QRect(220, 130, 41, 16))
        self.label_better.setStyleSheet(_fromUtf8(""))
        self.label_better.setObjectName(_fromUtf8("label_better"))
        self.label_faster = QtGui.QLabel(self.frameButtons)
        self.label_faster.setGeometry(QtCore.QRect(330, 130, 41, 16))
        self.label_faster.setStyleSheet(_fromUtf8(""))
        self.label_faster.setObjectName(_fromUtf8("label_faster"))
        self.label_stronger = QtGui.QLabel(self.frameButtons)
        self.label_stronger.setGeometry(QtCore.QRect(430, 130, 51, 16))
        self.label_stronger.setStyleSheet(_fromUtf8(""))
        self.label_stronger.setObjectName(_fromUtf8("label_stronger"))
        self.label_ever = QtGui.QLabel(self.frameButtons)
        self.label_ever.setGeometry(QtCore.QRect(770, 130, 31, 16))
        self.label_ever.setStyleSheet(_fromUtf8(""))
        self.label_ever.setObjectName(_fromUtf8("label_ever"))
        self.label_after = QtGui.QLabel(self.frameButtons)
        self.label_after.setGeometry(QtCore.QRect(880, 130, 31, 16))
        self.label_after.setStyleSheet(_fromUtf8(""))
        self.label_after.setObjectName(_fromUtf8("label_after"))
        self.label_workits = QtGui.QLabel(self.frameButtons)
        self.label_workits.setGeometry(QtCore.QRect(980, 130, 51, 16))
        self.label_workits.setStyleSheet(_fromUtf8(""))
        self.label_workits.setObjectName(_fromUtf8("label_workits"))
        self.label_over = QtGui.QLabel(self.frameButtons)
        self.label_over.setGeometry(QtCore.QRect(1100, 130, 31, 16))
        self.label_over.setStyleSheet(_fromUtf8(""))
        self.label_over.setObjectName(_fromUtf8("label_over"))
        self.label_hight = QtGui.QLabel(self.frameButtons)
        self.label_hight.setGeometry(QtCore.QRect(140, 220, 31, 16))
        self.label_hight.setStyleSheet(_fromUtf8(""))
        self.label_hight.setObjectName(_fromUtf8("label_hight"))
        self.label_veryhight = QtGui.QLabel(self.frameButtons)
        self.label_veryhight.setGeometry(QtCore.QRect(230, 220, 61, 16))
        self.label_veryhight.setStyleSheet(_fromUtf8(""))
        self.label_veryhight.setObjectName(_fromUtf8("label_veryhight"))
        self.label_low = QtGui.QLabel(self.frameButtons)
        self.label_low.setGeometry(QtCore.QRect(690, 220, 21, 16))
        self.label_low.setStyleSheet(_fromUtf8(""))
        self.label_low.setObjectName(_fromUtf8("label_low"))
        self.button_q = QtGui.QPushButton(self.frameButtons)
        self.button_q.setGeometry(QtCore.QRect(50, 30, 91, 71))
        self.button_q.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_q.setStyleSheet(_fromUtf8(""))
        self.button_q.setObjectName(_fromUtf8("button_q"))
        self.label_workit = QtGui.QLabel(self.frameButtons)
        self.label_workit.setGeometry(QtCore.QRect(70, 40, 41, 16))
        self.label_workit.setStyleSheet(_fromUtf8(""))
        self.label_workit.setObjectName(_fromUtf8("label_workit"))
        self.label_verylow = QtGui.QLabel(self.frameButtons)
        self.label_verylow.setGeometry(QtCore.QRect(780, 220, 61, 16))
        self.label_verylow.setStyleSheet(_fromUtf8(""))
        self.label_verylow.setObjectName(_fromUtf8("label_verylow"))
        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(390, 20, 501, 41))
        self.titulo.setObjectName(_fromUtf8("titulo"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1260, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Daft Punk Pythonic by Carmoreno", None))
        self.button_w.setText(_translate("MainWindow", "W", None))
        self.button_o.setText(_translate("MainWindow", "O", None))
        self.button_i.setText(_translate("MainWindow", "I", None))
        self.button_u.setText(_translate("MainWindow", "U", None))
        self.button_y.setText(_translate("MainWindow", "Y", None))
        self.button_t.setText(_translate("MainWindow", "T", None))
        self.button_r.setText(_translate("MainWindow", "R", None))
        self.button_e.setText(_translate("MainWindow", "E", None))
        self.button_p.setText(_translate("MainWindow", "P", None))
        self.button_a.setText(_translate("MainWindow", "A", None))
        self.button_g.setText(_translate("MainWindow", "G", None))
        self.button_f.setText(_translate("MainWindow", "F", None))
        self.button_d.setText(_translate("MainWindow", "D", None))
        self.button_s.setText(_translate("MainWindow", "S", None))
        self.button_z.setText(_translate("MainWindow", "Z", None))
        self.button_punto_coma.setText(_translate("MainWindow", ";", None))
        self.button_l.setText(_translate("MainWindow", "L", None))
        self.button_k.setText(_translate("MainWindow", "K", None))
        self.button_j.setText(_translate("MainWindow", "J", None))
        self.button_h.setText(_translate("MainWindow", "H", None))
        self.button_x.setText(_translate("MainWindow", "X", None))
        self.button_c.setText(_translate("MainWindow", "C", None))
        self.button_v.setText(_translate("MainWindow", "V", None))
        self.button_b.setText(_translate("MainWindow", "B", None))
        self.button_n.setText(_translate("MainWindow", "N", None))
        self.button_m.setText(_translate("MainWindow", "M", None))
        self.button_coma.setText(_translate("MainWindow", ",", None))
        self.button_space.setText(_translate("MainWindow", "Instrumental ♪", None))
        self.label_makeit.setText(_translate("MainWindow", "Make it", None))
        self.label_doit.setText(_translate("MainWindow", "Do it", None))
        self.label_makeus.setText(_translate("MainWindow", "Make us", None))
        self.label_morethan.setText(_translate("MainWindow", "More than", None))
        self.label_hour.setText(_translate("MainWindow", "Hour", None))
        self.label_our.setText(_translate("MainWindow", "Our", None))
        self.label_never.setText(_translate("MainWindow", "Never", None))
        self.label_harder.setText(_translate("MainWindow", "Harder", None))
        self.label_better.setText(_translate("MainWindow", "Better", None))
        self.label_faster.setText(_translate("MainWindow", "Faster", None))
        self.label_stronger.setText(_translate("MainWindow", "Stronger", None))
        self.label_ever.setText(_translate("MainWindow", "Ever", None))
        self.label_after.setText(_translate("MainWindow", "After", None))
        self.label_workits.setText(_translate("MainWindow", "Work its", None))
        self.label_over.setText(_translate("MainWindow", "Over", None))
        self.label_hight.setText(_translate("MainWindow", "Hight", None))
        self.label_veryhight.setText(_translate("MainWindow", "Very hight", None))
        self.label_low.setText(_translate("MainWindow", "Low", None))
        self.button_q.setText(_translate("MainWindow", "Q", None))
        self.label_workit.setText(_translate("MainWindow", "Work it", None))
        self.label_verylow.setText(_translate("MainWindow", "Very Low", None))
        self.titulo.setText(_translate("MainWindow", "Harder, Better, Faster... ♪♫", None))

