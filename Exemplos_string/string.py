texto = "aula pycode"
print(texto[0])  # imprime o texto da posição passada
print(texto[2:6])  # imprime o range passado (imprime 1 a menos)
print(texto[3:])  # imprime a partir da posição passada
print(texto[:6])  # imprime até a posição passada
print(len(texto))  # imprime o tamanho do texto
print(texto.count("a"))  # imprime a quantidade de 'a'
print(texto.count("a", 5, 11))  # imprime a quantidade de 'a' dentro do range passado
print(texto.find("aula"))  # imprime a posição onde o trecho começa
print(texto.upper())  # imprime o texto em caixa alta
print(texto.lower())  # imprime o texto em caixa baixa
print(texto.capitalize())  # imprime a primeira letra em caixa alta
print(texto.title())
# imprime a primeira letra de cada palavra do 'texto' em caixa alta
print(texto.split())  # imprime uma lista com todas as palavras (quebra por espaço)

lista_de_palavras = texto.split()
print("-".join(lista_de_palavras))
# as '' no join indicam o separador: espaço, traço, etc

print(texto.strip())  # tira os espaços antes ou depois do texto
print(texto.rstrip())  # tira os espaços da direita
print(texto.lstrip())  # tira os espaços da esquerda
