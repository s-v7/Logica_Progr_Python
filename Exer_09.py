####****{Silas Vasconcelos Cruz}***####
#Algoritmo  que pergunte o tempo gasto em uma viagem (em horas), a
#velocidade média (em km/h) e a autonomia do automóvel (em km/l); e que
#calcule a distância (em km) e o consumo total de combustível (em l - litros).
#
#       Curso: Tecnologia em Eletrônica Industrial
#       Matéria: Lógica de Programação
#       Prof: Carlos Speranza
#       Aluno/Author: Silas Vasconcelos Cruz 
#
#Definindo as Variáveis de Entrada
from statistics import *
tempo = 0
velocidadeMédia = 0
autonomiaAutomovel = 0 
distancia = 0 
consumoTotal = 0 
#
# Entrada de Dados
tempo = float(input("Digite o tempo que foi gasto na viagem em(horas): "))
velocidadeMédia = int(input("Qual foi a velocidade Média da viagem(em Km / h): "))
autonomiaAutomovel = int(input("Digite o valor da autonomia do automóvel em(km/l): "))
#
#cálculo da distãncia e Consumo total do automóvel
distancia = (velocidadeMédia * tempo)
consumoTotal =  ((autonomiaAutomovel) / distancia)
#
#Saída de Dados
print(f'A distância percorrida foi de {distancia} Km e o seu consumo foi {consumoTotal:.2f} Litros')

