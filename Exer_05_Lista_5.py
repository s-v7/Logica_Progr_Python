################################ IFSC - CAMPUS FLORIANÓPOLIS ##########################
# Algoritmo que Calcula o somatório dos números inferior 
# e superior, dados valores pelo usuário f(x);
#
#       Curso: Tecnologia em Eletrônica Industrial
#       Matéria: Lógica de Programação
#       Prof: Carlos Speranza
#       Aluno/Author: Silas Vasconcelos Cruz 
#
#
##Definindo as variáveis de Entrada
i_inferior = 0 
x_superior = 0 
soma = 0
#
#Entrada de Dados 
i_inferior = int(input("Digite o valor inferior: "))
x_superior = int(input("Digite o valor superior:  "))

#Laço para cálculos
for  i  in range(-i_inferior,x_superior):
    soma += i

    print(f'Na posição {i} a soma é: {soma}')



################################### FIM  #################################