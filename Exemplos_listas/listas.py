carros = []
print(carros)

carros.append('Marea')
print(carros)

carros.append('Fusca')
print(carros)

carros.append(10) # adiciona itens na última posição da lista 
print(carros)

carros_new = ['Marea', 'Fusca', 'Chevette']
print(carros_new)

print(carros_new[0])

carros_new.insert(1, 'Escort') #insere um novo elemento no index indicado
print(carros_new)

carros_new.pop() #remove o último da lista
print(carros_new)

del carros_new[2] #remove no índice indicado
print(carros_new)

carros.remove('Fusca') #remove o valor passado
print(carros)

print(carros.count(10)) #ele conta a quantidade de vezes que o elemento '10', aparece na lista

carros.reverse() #inverte a posição dos elementos da lista
print(carros)

carros_new.sort() #organiza na ordem alfanumérica
print(carros_new )
