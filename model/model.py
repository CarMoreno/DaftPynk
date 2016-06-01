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

	def get_model_music(self):
		return self.model_music	

	def manager_music(self, label):
		"""Administrador de musica"""
		if label == LABEL_WORKIT:
			self.model_music.play_fragments(WORK_IT)
		elif label == LABEL_MAKEIT:
			self.model_music.play_fragments(MAKE_IT)
		elif label == LABEL_DOIT:
			self.model_music.play_fragments(DO_IT)
		elif label == LABEL_MAKEUS:			
			self.model_music.play_fragments(MAKE_US)
		elif label == LABEL_MORETHAN:
			self.model_music.play_fragments(MORE_THAN)
		elif label == LABEL_HOUR:
			self.model_music.play_fragments(HOUR)
		elif label == LABEL_OUR:
			self.model_music.play_fragments(OUR)
		elif label == LABEL_NEVER:
			self.model_music.play_fragments(NEVER)	
		elif label == LABEL_HARDER:
			self.model_music.play_fragments(HARDER)
		elif label == LABEL_BETTER:
			self.model_music.play_fragments(BETTER)
		elif label == LABEL_FASTER:
			self.model_music.play_fragments(FASTER)
		elif label == LABEL_STRONGER:
			self.model_music.play_fragments(STRONGER)
		elif label == LABEL_EVER:
			self.model_music.play_fragments(EVER)
		elif label == LABEL_AFTER:
			self.model_music.play_fragments(AFTER)
		elif label == LABEL_WORKITS:
			self.model_music.play_fragments(WORK_ITS)
		elif label == LABEL_OVER:
			self.model_music.play_fragments(OVER)						
		elif label == LABEL_HIGHT:
			self.model_music.play_full(50250)
		elif label == LABEL_VERYHIGHT:
			self.model_music.play_full(53250)
		elif label == LABEL_LOW:
			self.model_music.play_full(38250)
		elif label == LABEL_VERYLOW:
			self.model_music.play_full(36250)			
		elif label == SPACE:
			self.model_music.play_full()	
