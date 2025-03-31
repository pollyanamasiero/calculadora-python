# Criar um programa que recebe nome e idade e retorna uma mensagem formatada.

nome = input('Olá! Qual é o seu nome? ')
anoNascimento = int(input('Em que ano você nasceu? ')) #Converte string em inteiro
ano = 2025
idade = ano - anoNascimento

print(f'Olá, {nome}! Você nasceu em {anoNascimento}!')
print(f'Esse ano você fez/faz {idade}!')