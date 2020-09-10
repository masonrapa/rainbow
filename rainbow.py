from lib import fore
from random import randint
import sys
def rb(lista):
	lista = str(lista).replace("['","").replace("']","").replace("', '"," ").replace("","@@@")
	colores = open("colors.txt","r").read().split("\n")
	digits = lista.split("@@@")
	a = randint(0,len(colores)-1)
	for l in digits:
		if l != "" or l != " ":
			if a == len(colores)-1:a = 0
			a = a + 1
			color = colores[a].split(",")
			fore(int(color[0]),int(color[1]),int(color[2]),l).go
		else:sys.stdout.write("")
try:
	test = sys.argv[1]
	lista = sys.argv
	lista.remove(sys.argv[0])
	rb(lista)
except:
	rb(input(">> "))
