# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:37:43 2023

@author: logonrmlocal
"""
#------------------------------------------------------------------------------
'''Adicionando e removendo elementos em um conjunto'''

conjunto = set()
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
conjunto.add(4)
conjunto.discard(5)
print(conjunto)
#------------------------------------------------------------------------------
'''Concatenando dois conjuntos'''

conjunto1 = {'banana', 'maçã', 'apple'}
conjunto2 = {'google', 'microsoft', 'apple'}

print(conjunto1.union(conjunto2))
#------------------------------------------------------------------------------
'''Intersecção de dois conjuntos'''

conjunto1 = {'banana', 'maçã', 'apple'}
conjunto2 = {'google', 'microsoft', 'apple'}

print(conjunto1.intersection(conjunto2))
#------------------------------------------------------------------------------
'''Unindo dois conjuntos'''

conjunto1 = {'banana', 'maçã', 'apple'}
conjunto2 = {'google', 'microsoft', 'apple'}

print(conjunto1.union(conjunto2))
#------------------------------------------------------------------------------
'''Verificando se um conjunto está contido em outro'''

conjunto1 = {'banana', 'maçã', 'apple'}
conjunto2 = {'maçã', 'apple', 'banana'}

print(conjunto1.issubset(conjunto2))
#------------------------------------------------------------------------------
'''
Dada uma lista com elementos duplicados, crie um conjunto com os elementos 
únicos
'''

lista = ['banana', 'laranja', 'apple', 'apple']
elementos_unicos = set(lista)
print(elementos_unicos)
#------------------------------------------------------------------------------
'''
Verificação de igualdade de conjuntos:
Crie dois conjuntos A e B e verifique se eles são iguais
'''

conjunto1 = {'banana', 'maçã', 'apple'}
conjunto2 = {'google', 'microsoft', 'apple'}

if conjunto1 == conjunto2:
    print('Os conjuntos são iguais')
else:
    print('Os conjuntos não são iguais')
#------------------------------------------------------------------------------
'''
Conjunto de potências:
Crie um conjunto de potências de um conjunto A dado
''' 

conjunto_a = {1, 2, 3, 4}
conjunto_b = set()
for e in conjunto_a:
    conjunto_b.add(e**e)
print(conjunto_b)
#------------------------------------------------------------------------------