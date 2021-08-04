################################ IFSC - CAMPUS FLORIANÓPOLIS ##########################
# Algoritmo que recebe como estrada um número inteiro positivo n
# e gere uma lista com números inteiros de (-n,n) dados os valores pelo usuário f(n);
#
#       Curso: Tecnologia em Eletrônica Industrial
#       Matéria: Lógica de Programação
#       Prof: Carlos Speranza
#       Aluno/Author: Silas Vasconcelos Cruz 
#
#
##Definindo as variáveis de Entrada
n_Numero = 0 

n_Numero = int(input("Enter um valor n: "))

for i in range(-n_Numero, n_Numero):
    print(f'Os valores da Lista: {i} na posição: {i}')