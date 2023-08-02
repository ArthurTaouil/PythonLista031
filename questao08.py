'''
    Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem.

    O programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o valor do consumo médio do automóvel, em quilômetros por litro
'''

distancia_percorrida = float(input("Qual foi a distância percorrida pelo automóvel na viagem, em quilômetro? "))
consumo_medio = float(input("Qual é o consumo médio de combustível de seu automóvel por quilômetro?" ))

combustivel_necessario = distancia_percorrida / consumo_medio

print("A quantidade necessária de combustível, em litros, é ", combustivel_necessario)