'''
    Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso

    Utilizando a formula: prestação = valor + (valor * (taxa / 100) * tempo em dias)
'''

valor = float(input("Insira o valor normal da prestação: "))
taxa = float(input("Insira o valor da taxa: "))
tempo = float(input("Insira os dias de atraso: "))

prestacao = valor + (valor * (taxa / 100) * tempo

print("O valor da prestação com atraso é de R$", prestacao)
