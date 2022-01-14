"""
Funções (def):
  *args - argumentos
  **kwargs - chaves de argumentos
"""

# Argumentos simples
def func(a1, a2, a3, a4, a5, nome=None):
    print(a1, a2, a3, a4, a5, nome)
func(1, 2, 3, 4, 5, nome='Ladeira')


lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(*lista, sep='|')


# Numeros de argumentos indefinidos - Faz o mesmo que o empacotamento e desempacotamento
def fun_args(*args):
    print(args)
    print(args[0])
    print(args[1])
    print(args[-1])
    print(len(args))
#var = fun_args(1,2,3,4, 5, 6, 7, 8, 9)

# Obs. Uma lista pode ser alterada uma tupla não
def fun_args_2(*args):
    args = list(args) # mudando de tupla para lista
    args[0] = 20
    print(args[0])
    args[5] = 1
    for v in args:
        print(v)

var = fun_args_2(1,2,3,4, 5, 6, 7, 8, 9)


def fun_args_3(*args):
    for v in args:
        print(args)
lista = [1, 2, 3, 4, 6]
lista2 = [40, 50, 60]
#fun_args_3(lista)   # vou ter uma lista no primeiro indice da minha tupla
#fun_args_3(*lista, 20, 30, 40)  # desempacotando a lista
fun_args_3(*lista, *lista2) #as listas são mescladas no *args