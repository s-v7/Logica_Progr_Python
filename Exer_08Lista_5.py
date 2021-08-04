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
id_usuario = 0
n_Input = 0
positivos = 0 
negativos = 0
#
#
#
id_usuario = str(input("Digite seu Nome por favor: "))
n_Input = int(input("Enter valor f(n) ou Digite 0 para Sair! "))
#
##
###
####
if(n_Input != 0):

    while(n_Input != 0):
        n_Input = int(input("Digite outro valor: "))
        if(n_Input >= 0):
            positivos += 1
            print(f'{id_usuario} Esta é a quantidade de Valores positivos que você Ditou até o instante: {positivos}')
        else:
            negativos += 1
            print(f'{id_usuario} Esta é a quantidade de valores negativos digitados até o instante: {negativos}')
else:
    print(f'Obrigado,Volte Sempre!!! Você digitou -> {n_Input} ')