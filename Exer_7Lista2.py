### {Silas Vasconcelos Cruz} ###
## Algoritmo onde usuário digita os valores dos coeficientes a, b e c de uma 
##Equação do segundo Grau
#
#       Curso: Tecnologia em Eletrônica Industrial
#       Matéria: Lógica de Programação
#       Prof: Carlos Speranza
#       Aluno/Author: Silas Vasconcelos Cruz 
#
#Importando a biblioteca matemática
from math import *
#Definindo as variáveis de Entrada
a = 0 
b = 0 
c = 0
delta = 0 
raiz_x = 0
raix_y = 0
#
#
##Entrada de Dados
a = int(input(f'Digite o valor de a: '))
b = int(input(f'Digite o valor de b: '))
c = int(input(f'Digite o valor de c: '))
##
##Cálculo do delta para saber se existe raiz
delta = sqrt((b**2) - 4 * a * c)
#
#Testando as condições
if(delta >= 0):
    raiz_x = ((-(b) + delta) / 2 * a)
    raix_y = ((-(b) - delta) / 2 * a)
    print(f'Existe Raízes\nRaízes:{raiz_x}\n,{raix_y}')
elif(delta < 0):
    print(f'Não Existe Raízes!')

############ Fim #####################