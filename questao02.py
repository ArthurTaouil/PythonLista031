'''
    Elaborar um programa que pergunte quatro (4) valores inteiros e apresente dois (2) resultados

    1. Resultado de suas adições
    2. Resultado de suas multiplicações
'''

num1 = int(input("Insira o primeiro valor inteiro: "))
num2 = int(input("Insira o segundo valor inteiro: "))
num3 = int(input("Insira o terceiro valor inteiro: "))
num4 = int(input("Insira o quarto valor inteiro: "))

adicao = num1 + num2 + num3 + num4
multiplicacao = num1 * num2 * num3 * num4

print("Resultado da adição: ", adicao)
print("Resultado da multiplicação: ", multiplicacao)