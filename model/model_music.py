import os
import pygame

class ModelMusic(object):
	"""Clase que maneja los sonidos de las teclas"""
	def __init__(self):
		pygame.mixer.init()
			
	def playFull(self):
		"""Reproduce la cancion completamente, por tiempo indefinido o bien, hasta que se de click en otra tecla"""
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/DaftPunk-HBFS.mp3"))
		pygame.mixer.music.play(-1)
	
	def play_fragments(self, name):
		"""Metodo generico para reproducir cualquier fragmento de cancion"""
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/{fragment}.mp3".format(fragment=name)))
		pygame.mixer.music.play()							
	
	