def envia_email(cliente):
    print(f"Email enviado para o cliente {cliente}!")


clientes = ["Ana", "João", "Felipe", "Maria", "Renato"]

for cliente in clientes:
    envia_email(cliente)


for i, cliente in enumerate(clientes):
    print(i, cliente)

for i in range(2):
    print(i)

for i, cliente in enumerate(clientes):
    if i == 2:
        break  # continue
    envia_email(cliente)

numero = 0
while numero < 5:
    print(numero)
    numero += 1

numero_2 = 0
while numero_2 < 5:
    if numero_2 == 2:
        break
    print(numero_2)
    numero_2 += 1
