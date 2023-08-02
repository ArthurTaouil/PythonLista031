'''
    Fazer um algoritmo que pergunte um (1) número e apresente

    1. O próprio número
    2. O quadrado deste número
    3. A raiz quadrada deste número
'''

num = float(input("Insira um número: "))

quadrado = num ** 2
raiz_quadrada = num ** 1/2

print("O número que você inseriu: ", num)
print("O quadrado do número que você inseriu: ", quadrado)
print("A raiz quadrada do número que você inseriu: ", raiz_quadrada)