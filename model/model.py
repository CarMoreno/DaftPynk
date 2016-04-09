import os
import pygame
import random
from model_music import *
from model_styles import *
from constantes import *
class ModelLaunchpad(object):
	"""Clase que se encarga de gestionar los botones"""	
	def __init__(self):
		self.model_music = ModelMusic()
		self.model_styles = ModelStyle()

	def manager_music(self, button):
		"""Administrador de musica"""
		if str(button.objectName()) == Q:
			self.model_music.play_fragments(WORK_IT)
		elif str(button.objectName()) == W:
			self.model_music.play_fragments(MAKE_IT)
		elif str(button.objectName()) == E:
			self.model_music.play_fragments(DO_IT)
		elif str(button.objectName()) == R:			
			self.model_music.play_fragments(MAKE_US)
		elif str(button.objectName()) == U:
			self.model_music.play_fragments(MORE_THAN)
		elif str(button.objectName()) == I:
			self.model_music.play_fragments(HOUR)
		elif str(button.objectName()) == O:
			self.model_music.play_fragments(OUR)
		elif str(button.objectName()) == P:
			self.model_music.play_fragments(NEVER)	
		elif str(button.objectName()) == A:
			self.model_music.play_fragments(HARDER)
		elif str(button.objectName()) == S:
			self.model_music.play_fragments(BETTER)
		elif str(button.objectName()) == D:
			self.model_music.play_fragments(FASTER)
		elif str(button.objectName()) == F:
			self.model_music.play_fragments(STRONGER)
		elif str(button.objectName()) == J:
			self.model_music.play_fragments(EVER)
		elif str(button.objectName()) == K:
			self.model_music.play_fragments(AFTER)
		elif str(button.objectName()) == L:
			self.model_music.play_fragments(WORK_ITS)
		elif str(button.objectName()) == PUNTO_COMA:
			self.model_music.play_fragments(OVER)						

	def behavior_space(self, array_buttons):
		"""Comportamiento para la tecla espacio"""
		self.model_music.playFull()
		background_color = "#{azar}".format(azar=random.randint(100, 999))
		for button in array_buttons:
			self.model_styles.apply_style_divers(array_buttons, background_color)