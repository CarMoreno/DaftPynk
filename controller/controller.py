from view.interface import *
from model.model import *
from PyQt4.QtCore import pyqtSlot
import PyQt4

class ControllerLaunchpad(QtGui.QMainWindow):
	"""Esta clase se encarga de pasar al modelo los mensajes traidos desde la vista"""
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.view = Ui_MainWindow() #view es un objeto de la clase Ui_MainWindow (mi interface)
		self.view.setupUi(self)
		self.the_model = ModelLaunchpad() #Objeto del modelo
		# self.button es un arreglo de tuplas (button, label)
		self.buttons = [
			(self.view.button_a, self.view.label_harder),(self.view.button_d, self.view.label_faster),
			(self.view.button_e, self.view.label_doit),(self.view.button_f, self.view.label_stronger),
			(self.view.button_i, self.view.label_hour),(self.view.button_j, self.view.label_ever),
			(self.view.button_k, self.view.label_after),(self.view.button_l, self.view.label_workits),
			(self.view.button_n, self.view.label_low),(self.view.button_o, self.view.label_our),
			(self.view.button_p, self.view.label_never),(self.view.button_q, self.view.label_workit), 
			(self.view.button_r, self.view.label_makeus),(self.view.button_s, self.view.label_better),
			(self.view.button_u, self.view.label_morethan),(self.view.button_w, self.view.label_makeit),
			(self.view.button_x, self.view.label_veryhight),(self.view.button_z, self.view.label_hight), 
			(self.view.button_punto_coma, self.view.label_over)
		]
		self.connect_button()
		self.view.button_space.clicked.connect(self.wrapper)

	@pyqtSlot()
	def wrapper(self):
		"""Slot personalizado para la signal clicked de la tecla de espacio"""
		self.the_model.behavior_space(self.view.button_space)

	@pyqtSlot()
	def is_pressed(self):
		"""Slot para cuando una tecla es presioanda"""
		for button, label in self.buttons:
			if button.isDown():#SI el boton actual fue presionado, entonces...
				self.the_model.manager_music(label)#Manejamos la gestion de musica		

	def connect_button(self):
		"""Conecta cada boton a las senales de pressed y released"""
		for button, label in self.buttons:
			button.pressed.connect(self.is_pressed)			
			#button.released.connect(self.is_released)