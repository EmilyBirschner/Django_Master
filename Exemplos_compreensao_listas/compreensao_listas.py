#problema proposto, multiplicar todos os elementos de uma lista por 2

numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []

#sem compreensão
for numero in numeros:
    numeros_dobrados.append(numero * 2)
    
print(numeros_dobrados)

#com compreensão
numeros_dobrados_comp = [numero * 2 for numero in numeros]

print(numeros_dobrados_comp)

#outro exemplo
def dobro(numero):
    return numero * 2

numeros_dobrados_comp_2 = [dobro(numero) for numero in numeros]
print(numeros_dobrados_comp_2)

#mais um exemplo
nomes = ['Ana', 'Felipe', 'João', 'Arlindo', 'Carlos']

nomes_uppercase = [nome.upper() for nome in nomes]
print(nomes_uppercase)

#compressão de listas com condicional
nomes_uppercase_a = [nome.upper() for nome in nomes if nome[0] == 'A']
print(nomes_uppercase_a)