from PyQt4 import QtGui
class ModelStyle(object):
	"""Maneja los estilos de la aplicacion"""

	def apply_style_pressed(self, widget):
		"""Aplica los cambios de estilo dependiendo si un boton ha sido presionado"""
		if type(widget) == QtGui.QLabel:
			widget.setStyleSheet("background-color: #263238;\n"
				"border: 1px solid #263238;\n"
				"color: #00c853;\n"
				"font-family: \'Verdana\';\n"
				"font-size: 11px;")
		else: #Es un boton!	
			widget.setStyleSheet("border-radius: 6px;\n"
				"background-color: #263238;\n"
				"border: 5px solid #00c853;\n"
				"color: #00c853;\n"
				"font-family: \'Verdana\';\n"
				"font-size: 25px;\n"
				"")

	def apply_style_released(self, widget):
		""""Aplica los cambios de estilo dependiendo si un boton ha sido liberado"""
		if type(widget) == QtGui.QLabel:
			widget.setStyleSheet("background-color: #263238;\n"
				"border: 1px solid #263238;\n"
				"color: #78909c;\n"
				"font-family: \'Verdana\';\n"
				"font-size: 11px;")
		else:	
			widget.setStyleSheet("border-radius: 6px;\n"
				"background-color: #263238;\n"
				"border: 3px solid #78909c;\n"
				"color: #78909c;\n"
				"font-family: \'Verdana\';\n"
				"font-size: 25px;\n"
				"")	

	def apply_style_divers(self, array_buttons, array_labels):
		"""Recibe un arreglo de botones y un string que hace referencia al background
		que toma el boton, este estilo se aplica a todos los botones cada vez que se presione
		la barra de espacio"""
		for button in array_buttons:
			self.apply_style_pressed(button)			
		for label in array_labels:
			self.apply_style_pressed(label)	