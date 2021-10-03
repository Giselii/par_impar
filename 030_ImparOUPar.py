#Crie um programa que leia um número inteiro e mostre na tela se ele é PAr ou ÌMPAR.

num = int(input('Digite um número inteiro: '))
if (num % 2) == 0:
    print('{} é um número PAR'.format(num))
else:
    print('{} é um número ÍMPAR'.format(num))
