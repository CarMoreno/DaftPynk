import os
import pygame
import random
from model_music import *
from model_styles import *
from constantes import *
class ModelLaunchpad(object):
	"""Clase que se encarga de gestionar los botones"""	
	def __init__(self):
		self.model_styles = ModelStyle()
		self.model_music = ModelMusic()

	def manager_music(self, label):
		"""Administrador de musica"""
		if str(label.objectName()) == LABEL_WORIT:
			self.model_music.play_fragments(WORK_IT)
		elif str(label.objectName()) == LABEL_MAKEIT:
			self.model_music.play_fragments(MAKE_IT)
		elif str(label.objectName()) == LABEL_DOIT:
			self.model_music.play_fragments(DO_IT)
		elif str(label.objectName()) == LABEL_MAKEUS:			
			self.model_music.play_fragments(MAKE_US)
		elif str(label.objectName()) == LABEL_MORETHAN:
			self.model_music.play_fragments(MORE_THAN)
		elif str(label.objectName()) == LABEL_HOUR:
			self.model_music.play_fragments(HOUR)
		elif str(label.objectName()) == LABEL_OUR:
			self.model_music.play_fragments(OUR)
		elif str(label.objectName()) == LABEL_NEVER:
			self.model_music.play_fragments(NEVER)	
		elif str(label.objectName()) == LABEL_HARDER:
			self.model_music.play_fragments(HARDER)
		elif str(label.objectName()) == LABEL_BETTER:
			self.model_music.play_fragments(BETTER)
		elif str(label.objectName()) == LABEL_FASTER:
			self.model_music.play_fragments(FASTER)
		elif str(label.objectName()) == LABEL_STRONGER:
			self.model_music.play_fragments(STRONGER)
		elif str(label.objectName()) == LABEL_EVER:
			self.model_music.play_fragments(EVER)
		elif str(label.objectName()) == LABEL_AFTER:
			self.model_music.play_fragments(AFTER)
		elif str(label.objectName()) == LABEL_WORKITS:
			self.model_music.play_fragments(WORK_ITS)
		elif str(label.objectName()) == LABEL_OVER:
			self.model_music.play_fragments(OVER)						
		elif str(label.objectName()) == LABEL_HIGHT:
			self.model_music.play_full()
		elif str(label.objectName()) == LABEL_VERYHIGHT:
			self.model_music.play_full()
		elif str(label.objectName()) == LABEL_LOW:
			self.model_music.play_full()
		elif str(label.objectName()) == LABEL_VERYLOW:
			self.model_music.play_full()			

	def behavior_space(self, button_space):
		"""Comportamiento para la tecla espacio"""
		self.model_music.play_full()
