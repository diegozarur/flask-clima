from models.socio import Socio

# ----------------------------------------------------------------------------#
# Primeiro Desafio
# ----------------------------------------------------------------------------#
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']
test_str = "geeks geeks"
data = {}
repeat_data = []
for alpha in alphabet:
    for test in test_str:
        if test == alpha:
            data[alpha] = test_str.count(alpha)
    if alpha != ' ':
        repeat_data.append(alpha * test_str.count(alpha))

str_list = list(filter(None, repeat_data))

print(data)
seperator = ''
print(seperator.join(str_list))
# ----------------------------------------------------------------------------#


# ----------------------------------------------------------------------------#
# Segundo Desafio
# ----------------------------------------------------------------------------#
lista_socios = [
    (1, 16),
    (3, 13),
    (5, 15),
    (8, 10),
    (9, 19),
]


def listaDoBanco():
    lista = []
    for p in Socio.select(Socio.id):
        lista.append(p)
    return lista


def atualiza_socios(lista_socios):
    for a, b in lista_socios:
        if Socio.select().where(Socio.id == a):
            Socio.update(bilhete=b).where(Socio.id == a).execute()
            print("Sòcios atualizados: " + str(a))

        if not Socio.select().where(Socio.id == a):
            Socio.insert(id=a, bilhete=b, ativo=1).execute()
            print("Sòcios adicionados: " + str(a))


atualiza_socios(lista_socios)
# ----------------------------------------------------------------------------#
