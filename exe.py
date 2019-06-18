 #!/usr/bin/python
 # -*- coding: utf-8 -*- 
import sys
import os
from cx_Freeze import setup, Executable

 #Si la plataforma es Windows, seteas base a "Win32GUI", pues los archivos ejecutables con cx_Freeze se construyen
 #por default para aplicaciones de consola, por lo que base SIEMPRE estará seteada en 'Console',
 #A menos de que tengamos esta condición.


if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {
	"include_files" : ["images/", "music/"],#Si tu aplicación necesita imágenes, sonidos o fonts, acá lo incluyes
	"excludes": ["tkinter", "numpy", "scipy"]
}  

ejecutables = [Executable( 
	"main.pyw", #Este es mi archivo principal, el que arranca con la ejecucion de mi app 
	base = base, #Si no te funciona, prueba con base = "Win32GUI"
	targetName = "DaftPynk.exe", #El nombre que quieres que tenga tu ejecutable
	)]

setup(
	name = "DaftPynk",#El nombre de tu aplicación
	version = "1.0",
	options = {"build_exe": build_exe_options},
	executables	= ejecutables
)