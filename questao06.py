'''
    Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e apresente esta temperatura convertida em graus Celsius.

    A fórmula de conversão é c=(f-32)*5/9, onde c é a temperatura em graus Celsius e f em Fahrenheit
'''

f = float(input("Informe uma temperatura em graus Fahrenheit: "))

c = (f - 32) * 5 / 9
#quando fizer uma conta/formula em python, sempre use espaços entre componentes

print(f, "graus Fahrenheit é igual a", c, "graus Celsius")