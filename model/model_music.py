#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pygame import mixer

class ModelMusic(object):
	"""Clase que maneja los sonidos de las teclas"""
		
	def play_full(self, frequency=22050):
		"""Reproduce la cancion completamente, por tiempo indefinido o bien, hasta que se de click en otra tecla"""
		mixer.pre_init(frequency=frequency)
		mixer.init()
		mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/DaftPunk-HBFS.mp3"))
		mixer.music.play()	
	
	def play_fragments(self, name):
		"""Metodo generico para reproducir cualquier fragmento de cancion"""
		mixer.init()
		mixer.music.load(os.path.join(os.path.dirname(__file__), "../music/{fragment}.mp3".format(fragment=name)))
		mixer.music.play()							
	
	