### {Silas Vasconcelos Cruz} ####
###Algoritmo para calcular a quantidade de piso para uma sala a ser construída, bem como a quantidade 
# de tinta a ser usada nas paredes. Precisa também saber qual o volume da sala 
# em metros quadrados para estimar a potência necessária para o ar condicionado.
#
#       Curso: Tecnologia em Eletrônica Industrial
#       Matéria: Lógica de Programação
#       Prof: Carlos Speranza
#       Aluno/Author: Silas Vasconcelos Cruz 
#
#Defindo Variáveis      
altura = 0
comprimento = 0 
largura = 0 
#
#
altura = float(input("Digite o valor da altura do ambiente: "))
comprimento = float(input("O valor do comprimento do ambiente: "))
largura = float(input("Agora a largura do ambiente: "))
#
#
print(f'A área do piso da sala: {largura * altura}m²')
print(f'O volume da sala: {altura * comprimento * largura}m³')
print(f'A área das paredes da sala: {(2 * altura * largura) + (2 * altura * comprimento)}m²')