 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from controller.controller import *
import ctypes
import sys
"""
Author: Carlos Andrés Moreno
Page: http://carmoreno.github.io/
Github: http://www.github.com/CarMoreno
Version: 1.0
Licence: Creative Commons 4.0

Launchpy es una aplicación construida sobre Python 2.7 he inspirada en el famoso proyecto "DaftPunkConsole" disponible
en http://codepen.io/kowlor/pen/MYOKRd, usando la librería gráfica PyQt junto con Pygame para el manejo de sonidos.
La arquitectura de esta pequeña aplicación sigue un patrón MVC, espero se útil y divertida :-).
Pull Request son bien recibidos :-)
"""
if __name__ == '__main__':
	myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	app = QtGui.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('image/icon.png'))
	myapp = ControllerLaunchpad()
	myapp.show()
	sys.exit(app.exec_())