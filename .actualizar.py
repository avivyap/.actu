#!/usr/bin/env python3

import time
import subprocess
import signal
import sys
from termcolor import colored


def def_handler(sig, frame):

	print("\n[+] Saliendo........\n\n")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler) #ctrl + c


def todo_actualizado():
	print(colored("\n[+] Esta todo actualizado\n", 'green'))

def actualizacion():

	print(colored("\n[+] Se han encontrado paquetes sin actualizar\n", 'red'))
	command_actu = subprocess.run("sudo apt upgrade -y", shell = True, capture_output=True)

	comprobacion()

def packets_cant_actu():

	print(colored("\n[+] Hay varios paquetes que no se pueden actualizar, asi que tienes que hacerlo a mano\n", 'yellow'))

	out = subprocess.run("sudo apt list --upgradable", shell=True)

	print(colored("\n[+] Para actualizarlos es --->   sudo apt upgrade x <- x es el nombre del paquete\n", 'yellow'))

trys = 0
def comprobacion():

	command = subprocess.run("sudo apt update| tail -n 1", shell= True, text=True, capture_output=True)

	global trys
	trys += 1

	if trys != 3:

		if "Se pueden actualizar" in command.stdout or "Se puede actualizar" in command.stdout:

			actualizacion()

		elif "Todos los paquetes están actualizados." in command.stdout:

			todo_actualizado()

	else:

		packets_cant_actu()


def todo_actualizado_en():
        print(colored("\n[+] All packages are up to date.\n", 'green'))

def actualizacion_en():

        print(colored("\n[+] Unupdated packages found \n", 'red'))
        command_actu = subprocess.run("sudo apt upgrade -y", shell = True, capture_output=True)

        comprobacion_en()

def packets_cant_actu_en():

        print(colored("\n[+] There are several packages that cannot be updated, so you have to do it manually\n", 'yellow'))

        out = subprocess.run("sudo apt list --upgradable", shell=True)

        print(colored("\n[+] To update them is ---> sudo apt upgrade x <- x is the package name\n", 'yellow'))

trys = 0
def comprobacion_en():

        command = subprocess.run("sudo apt update| tail -n 1", shell= True, text=True, capture_output=True)

        global trys
        trys += 1

        if trys != 3:

                if "packages can be upgraded" in command.stdout or "package can be upgrade" in command.stdout:

                        actualizacion_en()

                elif "All packages are up to date" in command.stdout:

                        todo_actualizado_en()

        else:

                packets_cant_actu_en()
def main():

	idioma = subprocess.run("echo $LANG", shell=True, text=True, capture_output=True)

	if idioma.stdout.strip() == "es_ES.UTF-8":
		comprobacion()

	elif idioma.stdout.strip() == "en_US.UTF-8":
		comprobacion_en()

	else:

		print(colored("\n[+] El idioma que tiene tu sistema operativo no es compatible con este script\n", 'red'))

if __name__ == '__main__':

	main()
