# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:08:30 2023

@author: logonrmlocal
"""
dados = [('Rafael', ('Leite', 'Ovos', 'Pão', 'Arroz', 'Batatas')), ('Gabriel', ('Massa', 'Molho de tomate', 'Batatas', 'Arroz')), ('João', ('Cebola', 'Alho', 'Tomate', 'Cenoura', 'Arroz'))]

print('Analizando dados de compras')
print('Menu:')
print('[1] Clientes que compraram um mesmo item')
choice = str(input(''))
match choice:
    case '1':
        item = str(input('Qual o item a ser analizado: '))
        for e in dados:
            print(f'Nome: {dados[e]}')
            for v in e:
                print(f'Itens comprados: {dados[1][v]}')
        