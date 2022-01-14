"""
1º Desafio - Crie uma função que exiba uma saudação ocm os parâmetros saudação e nome
"""

def desafio1(nome="Afonso", saudacao="Olá!"):
    return (f'{saudacao}, {nome}')

print(f'Desafio 1 - Resultado: ', desafio1(nome="Luiz", saudacao="Bem vindo"))

"""
2º Desafio - Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles.
"""
def desafio2(numero_1, numero_2, numero_3):
    soma = numero_1 + numero_2 + numero_3
    return soma
print(f'Desafio 2 - A Soma é igual à:', desafio2(2,5,7))

"""
3º Desafio - Crie uma função que receba 2 números. 
    O primeiro é um valor e  segundo um percentual (ex. 10%). Retorne o valor do primeiro número somado do aumento do percentual do mesmo.
"""
def desafio3(num1, num2):
    return num1 + num2 / 100
print(f'Desafio 3 - A soma deles é:', desafio3(9,5))

"""
4º Desafio - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorn Fizz.
   Se o parâmetro da função for divísivel por 5, retorn Buzz.
   Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
"""

def desafio4(parametro_1):
    divisivel_2 = int(parametro_1) % 2
    divisivel_3 = int(parametro_1) % 3
    divisivel_5 = int(parametro_1) % 5

    if divisivel_2 == 0:
        return 'Fizz'
    if divisivel_5 == 0:
        return 'Buzz'
    if divisivel_3 == 0 and divisivel_5 == 0:
        return 'FizzBuzz'
    else:
        return parametro_1
print(f'Desafio 4 - O resultado é: ', desafio4(105))