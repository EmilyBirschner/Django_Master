def somar(a, b):
    resultado = a + b
    return resultado


valor = somar(25, 30)
print(valor)


def envia_email():
    email = "email@email.com"
    senha = "1234"
    ...  # código que envia o email
    return "Email enviado com sucesso!"


pessoas = ["Fulano", "Ciclano", "Maria"]

for pessoa in pessoas:
    email_enviado = envia_email()
    print(email_enviado)


def send_email(nome, email):
    email_send = "email@email.com"
    senha = "1234"

    nome_destinatario = nome
    email_destinatario = email

    return f"Email enviado para {nome}, dona do email {email}"


pessoas_dest = [
    {"nome": "Felipe", "email": "felipe@gmail.com"},
    {"nome": "João", "email": "joao@gmail.com"},
    {"nome": "Maria", "email": "maria@gmail.com"},
]

for pessoa in pessoas_dest:
    print(pessoa)
    email_enviados = send_email(pessoa["nome"], pessoa["email"])
    print(email_enviados)
