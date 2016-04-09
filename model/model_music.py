import os
import pygame
import time
import threading
class ModelMusic(object):
	"""Clase que maneja los sonidos de las teclas"""
	def __init__(self):
		pygame.mixer.init()
			
	def playFull(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/DaftPunk-HBFS.mp3"))
		pygame.mixer.music.play(-1)
	
	# def play_fragments(self, name):
	# 	pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/{fragment}.mp3".format(fragment=name)))
	# 	pygame.mixer.music.play()							
	# 	pygame.mixer.stop()	
	
	def workIt(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/workit.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()	

	def doIt(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/doit.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()

	def makeIt(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/makeit.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()	

	def doIt(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/doit.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()	

	def makeUs(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/makeus.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()	

	def moreThan(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/morethan.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()

	def hour(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/hour.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()

	def our(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/our.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()

	def never(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/never.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()

	def faster(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/faster.mp3"))
		pygame.mixer.music.play()	
		pygame.mixer.stop()		
	
	def harder(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/harder.mp3"))
		pygame.mixer.music.play()	
		pygame.mixer.stop()
	
	def better(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/better.mp3"))
		pygame.mixer.music.play()	
		pygame.mixer.stop()	
	
	def stronger(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/stronger.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()

	def ever(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/ever.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()

	def after(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/after.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()

	def workIts(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/workits.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()

	def over(self):
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/over.mp3"))
		pygame.mixer.music.play()							
		pygame.mixer.stop()