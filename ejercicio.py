#! /usr/bin/env python
# -*- coding: utf-8 -*-

fich = open('/etc/passwd','r')
lista = fich.readlines()

for linea in lista:
    lista2 = linea.split(':')
    login = lista2[0]
    shell =lista2[-1][:-1]
    print login,shell
print len(lista)
