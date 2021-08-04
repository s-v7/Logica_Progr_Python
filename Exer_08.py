### {Silas Vasconcelos Cruz} ####
###Algoritmo  dados “x” segundos fornecidos pelo usuário,
# sejam fornecidas as quantidades de horas, minutos e segundos.
# 
# 
#       Curso: Tecnologia em Eletrônica Industrial
#       Matéria: Lógica de Programação
#       Prof: Carlos Speranza
#       Aluno/Author: Silas Vasconcelos Cruz 
#  
#Defindo Variáveis
Xsegundos = 0
horas = 0 
minutos = 0 
segundos = 0 
#
#Entrada de valores 
Xsegundos = int(input("Enter com a quantidade de segundos: "))
#
#Processamento
horas = ((Xsegundos) / 3600)
minutos = ((horas * 60) / 60)
segundos = (Xsegundos % 60)
#
#Saída de dados!
print(f'São {horas:.2f} horas e {minutos:.2f} minutos e {segundos:.2f} segundos')