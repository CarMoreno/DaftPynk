class ModelStyle(object):
	"""Maneja los estilos de la aplicacion"""

	def apply_style_pressed(self, button):
		"""Aplica los cambios de estilo dependiendo si un boton ha sido presionado"""
		button.setStyleSheet("border-radius: 6px;\n"
			"background-color: #263238;\n"
			"border: 5px solid #00c853;\n"
			"color: #00c853;\n"
			"font-family: \'Verdana\';\n"
			"font-size: 25px;\n"
			"")

	def apply_style_released(self, button):
		""""Aplica los cambios de estilo dependiendo si un boton ha sido liberado"""
		button.setStyleSheet("border-radius: 6px;\n"
			"background-color: #263238;\n"
			"border: 3px solid #78909c;\n"
			"color: #78909c;\n"
			"font-family: \'Verdana\';\n"
			"font-size: 25px;\n"
			"")	

	def apply_style_divers(self, array_buttons, color_background):
		"""Recibe un arreglo de botones y un string que hace referencia al background
		que toma el boton, este estilo se aplica a todos los botones cada vez que se presione
		la barra de espacio"""
		style = """border-radius: 6px;
			background-color: {color};
			border: 3px solid #78909c;
			color: #78909c;
			font-family: \'Verdana\';
			font-size: 25px;
			""".format(color=color_background)
		for button in array_buttons:
			button.setStyleSheet(style)			
				