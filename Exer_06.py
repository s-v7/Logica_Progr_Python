################################ IFSC - CAMPUS FLORIANÓPOLIS ##########################
### {Silas Vasconcelos Cruz} ####
###Algoritmo para calcular o volume de uma Esfera
#
#       Curso: Tecnologia em Eletrônica Industrial
#       Matéria: Lógica de Programação
#       Prof: Carlos Speranza
#       Aluno/Author: Silas Vasconcelos Cruz 
#
#Defindo Variáveis
Volume = 0 
Raio = 0 
#
#Solicitando o valor do Raio
Raio = float(input("Digite o valor do Raio: "))
#
#
#Equação para o cálculo do Volume de uma Esfera
Volume = (((4)/3) * 3.1415 * Raio**3)
#
#Saída de Dados!
print(f'O Volume da Esfera é {Volume:.2f}m³ para o raio de {Raio:.2f}mm')
