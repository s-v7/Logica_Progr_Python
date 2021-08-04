### {Silas Vasconcelos Cruz} ####
### Algoritmo onde dado o diametro de uma bola e os 
### valores de uma caixa mostra se a bola cabe ou não dentro da caixa!!
#
#       Curso: Tecnologia em Eletrônica Industrial
#       Matéria: Lógica de Programação
#       Prof: Carlos Speranza
#       Aluno/Author: Silas Vasconcelos Cruz 
#
#Definindo as Variéveis
diametroBola = 0
altura = 0 
largura = 0 
profundidade = 0
VolumeCaixa = 0 
#
#Entrada de Dados
diametroBola = int(input(f'Digite o valor do Diametro: '))
altura = int(input(f'Digite a altura da caixa: '))
largura = int(input(f'Digite a largura da caixa: '))
profundidade = int(input(f'Digite a profundidade da casa: '))
#
#Diamentro = (diametro_Valor) / 3.141592;
#
### diametro_Valor = (diametro * 3.141592)
#
### VolumeCaixa = (altura * largura * profundidade)
#
# Testando as condições
if(altura >= diametroBola and largura >= diametroBola and profundidade >= diametroBola):
    print(f'Sim, a bola cabe dentro da Caixa!')
else:
    print(f'A bola não cabe dentro da caixa!')


#### Fim ######