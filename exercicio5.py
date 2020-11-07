'''
Solicite 5 números ao usuário e armazene-os em uma tupla.
'''

tupla = ()
for a in range(5):
    n = int(input("Informe um número: "))
    tupla = tupla + (n,)

print(tupla)
