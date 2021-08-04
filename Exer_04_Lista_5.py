################################ IFSC - CAMPUS FLORIANÓPOLIS ##########################
# Algoritmo que recebe a idade de 10 pessoas, calcula e mostra pessoas com idade
# maior ou igual a 18 anos dados os valores pelo usuário f(x);
#
#       Curso: Tecnologia em Eletrônica Industrial
#       Matéria: Lógica de Programação
#       Prof: Carlos Speranza
#       Aluno/Author: Silas Vasconcelos Cruz 
#
#
##Definindo as variáveis de Entrada
Idade = 0 
contador = 0 
sum = 0
sum_1 = 0 
quantas_Pessoas = 0
#
#
##quantas_Pessoas = int(input("Digite a quantidade de Pessoas a Investigar: "))
while(contador < 10 ):
        Idade  = int(input("Enter idade: "))
        contador +=1
        if(Idade >= 18):
            sum += 1
            print(f'Quantidade de pessoas com Idade maio de 18 Anos: {sum}')
        else:
            sum_1 += 1
            print(f'Quantidade de pessoas com menos de 18 Anos: {sum}')
    

####################### FIM #############################