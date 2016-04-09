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
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_coma.setObjectName(_fromUtf8("button_coma"))
        self.button_v = QtGui.QPushButton(self.frame)
        self.button_v.setGeometry(QtCore.QRect(410, 190, 81, 71))
        self.button_v.setStyleSheet(_fromUtf8("border-radius: 6px;\n"
"background-color: #263238;\n"
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
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
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
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
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
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
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
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
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
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
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
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
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
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
"border: 3px solid #78909c;\n"
"color: #78909c;\n"
"font-family: \'Verdana\';\n"
"font-size: 25px;\n"
""))
        self.button_t.setObjectName(_fromUtf8("button_t"))
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
        self.titulo.setText(_translate("MainWindow", "Harder Better Faster ... ♪♫", None))

