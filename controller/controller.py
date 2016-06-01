from view.interface import *
from model.model import *
from model.constantes import *
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
			(self.view.button_a, LABEL_HARDER),(self.view.button_d, LABEL_FASTER),
			(self.view.button_e, LABEL_DOIT),(self.view.button_f, LABEL_STRONGER),
			(self.view.button_i, LABEL_HOUR),(self.view.button_j, LABEL_EVER),
			(self.view.button_k, LABEL_AFTER),(self.view.button_l, LABEL_WORKITS),
			(self.view.button_n, LABEL_LOW),(self.view.button_o, LABEL_OUR),
			(self.view.button_p, LABEL_NEVER),(self.view.button_q, LABEL_WORKIT), 
			(self.view.button_r, LABEL_MAKEUS),(self.view.button_s, LABEL_BETTER),
			(self.view.button_u, LABEL_MORETHAN),(self.view.button_w, LABEL_MAKEIT),
			(self.view.button_x, LABEL_VERYHIGHT), (self.view.button_m, LABEL_VERYLOW),
			(self.view.button_z, LABEL_HIGHT),(self.view.button_punto_coma, LABEL_OVER)
		]
		self.view.button_space.pressed.connect(self.wrapper)
		self.connect_button()

	@pyqtSlot()
	def wrapper(self):
		"""Slot personalizado para la signal clicked de la tecla de espacio"""
		self.the_model.manager_music(SPACE)

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