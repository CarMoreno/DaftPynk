from view.interface import *
from model.model import *
from model.model_styles import *
from PyQt4.QtCore import pyqtSlot
class ControllerLaunchpad(QtGui.QMainWindow):
	"""Esta clase se encarga de pasar al modelo los mensajes traidos desde la vista"""
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.view = Ui_MainWindow() #view es un objeto de la clase Ui_MainWindow (mi interface)
		self.view.setupUi(self)
		self.the_model = ModelLaunchpad() #Objeto del modelo
		self.the_model_style = ModelStyle() #Objeto model de estilos
		#Almacenamos todos los botones en un arreglo
		self.buttons = [ self.view.button_a, self.view.button_d, self.view.button_e, self.view.button_f,
						self.view.button_i, self.view.button_j, self.view.button_k, self.view.button_l,
						self.view.button_n, self.view.button_o, self.view.button_p, self.view.button_q, 
						self.view.button_r, self.view.button_s, self.view.button_u, self.view.button_w,
						self.view.button_x, self.view.button_z, self.view.button_punto_coma, self.view.button_space]
		
		self.connect_button()
		self.view.button_space.clicked.connect(self.wrapper)

	@pyqtSlot()
	def wrapper(self):
		"""Slot personalizado para la signal clicked de la tecla de espacio"""
		self.the_model.behavior_space(self.buttons)

	@pyqtSlot()
	def is_pressed(self):
		"""Slot para cuando una tecla es presioanda"""
		for button in self.buttons:
			if button.isDown():#SI el boton actual fue presionado, entonces...
				self.the_model_style.apply_style_pressed(button)#Aplicamos estilos al boton
				self.the_model.manager_music(button)#Manejamos la gestion de musica

	@pyqtSlot()
	def is_released(self):
		"Slot para cuando una tecla es liberada"
		for button in self.buttons:
			if not button.isDown():
				self.the_model_style.apply_style_released(button)			
			
	def connect_button(self):
		"""Conecta cada boton a las senales de pressed y released"""
		for button in self.buttons:
			button.pressed.connect(self.is_pressed)			
			button.released.connect(self.is_released)