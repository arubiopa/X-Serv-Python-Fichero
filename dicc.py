#! /usr/bin/env python
# -*- coding: utf-8 -*-

fich = open('/etc/passwd','r')
lista = fich.readlines()
dicc = {}

for linea in lista:
    lista2 = linea.split(':')
    dicc[lista2[0]] = lista2[-1][:-1]

print dicc['root']
print len(lista)

try:
	print dicc["imaginario"]
except KeyError:
	print "El usuario imaginario no existe"