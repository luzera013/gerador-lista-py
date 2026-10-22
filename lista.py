#OUTRO CODE.

import random

# 1. Lista com 100 nomes
nomes = [
    f"Pessoa_{i:03d}" for i in range(1, 101)
]

# 2. Lista com 100 idades
idades = [
    random.randint(18, 80) for _ in range(100)
]

# 3. Lista com 100 cidades fictícias
cidades = [
    f"Cidade_{i:03d}" for i in range(1, 101)
]

# 4. Lista com 100 CPFs fictícios (não válidos para uso real)
cpfs = [
    f"000.000.{i:03d}-00" for i in range(100)
]

# 5. Lista com 100 salários
salarios = [
    round(random.uniform(1500, 15000), 2)
    for _ in range(100)
]

# 6. Lista com 100 produtos
produtos = [
    f"Produto_{i:03d}" for i in range(1, 101)
]

# 7. Lista com 100 preços
precos = [
    round(random.uniform(5, 2000), 2)
    for _ in range(100)
]

# 8. Lista com 100 notas escolares
notas = [
    round(random.uniform(0, 10), 1)
    for _ in range(100)
]

# 9. Lista com 100 profissões
profissoes_disponiveis = [
    "Programador", "Professor", "Médico", "Advogado",
    "Engenheiro", "Designer", "Contador", "Enfermeiro",
    "Arquiteto", "Analista", "Vendedor", "Cozinheiro",
    "Motorista", "Eletricista", "Jornalista"
]

profissoes = [
    random.choice(profissoes_disponiveis)
    for _ in range(100)
]

# 10. Lista com 100 números de telefone fictícios
telefones = [
    f"(00) 00000-{i:04d}" for i in range(100)
]

# 11. Lista com 100 e-mails fictícios
emails = [
    f"usuario{i:03d}@exemplo.com"
    for i in range(1, 101)
]

# 12. Lista com 100 alturas em metros
alturas = [
    round(random.uniform(1.40, 2.10), 2)
    for _ in range(100)
]

# 13. Lista com 100 pesos em kg
pesos = [
    round(random.uniform(40, 150), 1)
    for _ in range(100)
]

# 14. Lista com 100 quantidades em estoque
estoques = [
    random.randint(0, 500)
    for _ in range(100)
]

# 15. Lista com 100 datas fictícias
datas = [
    f"{random.randint(1, 28):02d}/"
    f"{random.randint(1, 12):02d}/"
    f"{random.randint(2000, 2026)}"
    for _ in range(100)
]

# 16. Lista com 100 notas de satisfação
satisfacoes = [
    random.randint(1, 5)
    for _ in range(100)
]

# 17. Lista com 100 estados fictícios
estados = [
    f"Estado_{i:03d}" for i in range(1, 101)
]

# 18. Lista com 100 códigos de identificação
codigos = [
    f"ID-{i:05d}" for i in range(1, 101)
]

# 19. Lista com 100 temperaturas
temperaturas = [
    round(random.uniform(-5, 45), 1)
    for _ in range(100)
]

# 20. Lista com 100 percentuais de desconto
descontos = [
    random.randint(0, 70)
    for _ in range(100)
]

# Organizando todas as listas em um dicionário
dados = {
    "nomes": nomes,
    "idades": idades,
    "cidades": cidades,
    "cpfs_ficticios": cpfs,
    "salarios": salarios,
    "produtos": produtos,
    "precos": precos,
    "notas": notas,
    "profissoes": profissoes,
    "telefones_ficticios": telefones,
    "emails_ficticios": emails,
    "alturas": alturas,
    "pesos": pesos,
    "estoques": estoques,
    "datas": datas,
    "satisfacoes": satisfacoes,
    "estados_ficticios": estados,
    "codigos": codigos,
    "temperaturas": temperaturas,
    "descontos": descontos
}

# Exibindo os dados
for nome_lista, lista in dados.items():
    print(f"\n--- {nome_lista.upper()} ---")
    print(f"Quantidade de informações: {len(lista)}")
    print(lista)

# Conferindo se todas as listas possuem 100 itens
for nome_lista, lista in dados.items():
    assert len(lista) == 100, f"Erro na lista: {nome_lista}"

print("\nTodas as 20 listas possuem 100 informações!")
print("Total de elementos:", sum(len(lista) for lista in dados.values()))
