from PyQt4 import QtGui
class ModelStyle(object):
	"""Maneja los estilos de la aplicacion"""

	def apply_style_pressed(self, button, label=None):
		
		"""Aplica los cambios de estilo dependiendo si un boton ha sido presionado"""
		button.setStyleSheet("""border-radius: 6px;
			background-color: #263238;
			border: 5px solid #00c853;
			color: #00c853;
			font-family: \'Verdana\';
			font-size: 25px;
			""")
		if label is not None:
			label.setStyleSheet("""background-color: #263238;
				border: 1px solid #263238;
				color: #00c853;
				font-family: \'Verdana\';
				font-size: 11px;""")

	def apply_style_released(self, button, label):
		""""Aplica los cambios de estilo dependiendo si un boton ha sido liberado"""
		button.setStyleSheet("""border-radius: 6px;
			background-color: #263238;
			border: 3px solid #78909c;
			color: #78909c;
			font-family: \'Verdana\';
			font-size: 25px;
			""")
		label.setStyleSheet("""background-color: #263238;
			border: 1px solid #263238;
			color: #78909c;
			font-family: \'Verdana\';
			font-size: 11px;""")	