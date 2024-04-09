# Exercício funções
'''
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def somar_numeros(num1, num2, num3):
    soma_numeros = num1 + num2 + num3
    return(somar_numeros)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print(f"A soma entre os números é: {somar_numeros(num1,num2, num3)}.")
    