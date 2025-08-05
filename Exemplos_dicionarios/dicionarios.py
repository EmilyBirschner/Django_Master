# chave-valor
# meu_dicionario = {'chave':'valor'}
meu_dicionario = {"nome": "Felipe", "idade": 25, "profissao": "Dev"}

print(meu_dicionario)
print(meu_dicionario["nome"])
print(meu_dicionario.get("idade"))
print(meu_dicionario.pop("profissao"))  # remove dados
print(meu_dicionario.keys())  # lista as chaves
print(meu_dicionario.values())  # lista os valores
print(meu_dicionario.clear())  # limpa tudo do dicionario

pessoa = {
    "nome": "Emily",
    "idade": "36",
    "profissao": "dev",
    "interesses": ["Python", "Programação", "Notebooks"],
    "pet": {"nome": "Redd", "idade": 5, "peso": "47kg"},
}

print(pessoa.get("interesses")[2])
print(pessoa["interesses"][2])

print(pessoa.get("pet").get("nome"))
print(pessoa["pet"]["nome"])

pessoa["ano_nascimento"] = 1989
print(pessoa)
