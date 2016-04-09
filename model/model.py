import os
import pygame
import random
from model_music import *
from model_styles import *
from constantes import *
class ModelLaunchpad(object):
	"""Clase que se encarga de gestionar los botones"""
	
	def __init__(self):
		pygame.mixer.init()
		self.model_music = ModelMusic()
		self.model_styles = ModelStyle()

	def manager_music(self, button):
		"""Administrador de musica"""
		if str(button.objectName()) == Q:
			self.model_music.workIt()
		elif str(button.objectName()) == W:
			self.model_music.makeIt()
		elif str(button.objectName()) == E:
			self.model_music.doIt()
		elif str(button.objectName()) == R:			
			self.model_music.makeUs()
		elif str(button.objectName()) == U:
			self.model_music.moreThan()
		elif str(button.objectName()) == I:
			self.model_music.hour()
		elif str(button.objectName()) == O:
			self.model_music.our()
		elif str(button.objectName()) == P:
			self.model_music.never()	
		elif str(button.objectName()) == A:
			self.model_music.harder()
		elif str(button.objectName()) == S:
			self.model_music.better()
		elif str(button.objectName()) == D:
			self.model_music.faster()
		elif str(button.objectName()) == F:
			self.model_music.stronger()
		elif str(button.objectName()) == J:
			self.model_music.ever()
		elif str(button.objectName()) == K:
			self.model_music.after()
		elif str(button.objectName()) == L:
			self.model_music.workIts()
		elif str(button.objectName()) == PUNTO_COMA:
			self.model_music.over()							

	def behavior_space(self, array_buttons):
		"""Comportamiento para la tecla espacio"""
		self.model_music.playFull()
		background_color = "#{azar}".format(azar=random.randint(100, 999))
		for button in array_buttons:
			self.model_styles.apply_style_divers(array_buttons, background_color)