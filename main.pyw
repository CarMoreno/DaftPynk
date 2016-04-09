 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import sys
from controller.controller import *

"""
Author: Carlos Andrés Moreno
Page: http://carmoreno.github.io/
Version: 1.0
Licence: Creative Commons 4.0
"""
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	myapp = ControllerLaunchpad()
	myapp.show()
	sys.exit(app.exec_())
