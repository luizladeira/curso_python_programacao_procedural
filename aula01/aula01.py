"""
FUNÇÕES: def - definir funções próprias - PART 01
"""
def saudacao(msg="Olá", nome="Rodolfo"):
    nome = nome.replace('e', '3')
    print(msg, nome)

saudacao('Mensagem', 'Luiz Ladeira')
saudacao()
saudacao(nome="Zezínho")

def teste2(msg="Olá", nome="Rodolfo"):
    nome = nome.replace('e', '3')
    return f'{msg} {nome}'

variavel = teste2()
print(variavel)

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

dividir = divisao(0,2)
if dividir:
    print(dividir)
else:
    print('Conta inválida')

def dumb():
    return [2, '2', 77, True]
var1 = dumb()
print(var1, type(var1))

def f(var):
    print(var)

def fdumb():
    return f
print(fdumb)
var = fdumb()('E colocar o valor aqui')

# Função retorna tuplas - que são listas que não podem ser alteradas
def tuplas():
    return 'Luiz', 'Ladeira'
print(tuplas())
var = tuplas()
print(var, type(var))