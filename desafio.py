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

carteira = [
    {
        'numero': 1,
        'ativo': True,
        'bilhete': 10,
    },
    {
        'numero': 2,
        'ativo': False,
        'bilhete': 0,
    },
    {
        'numero': 3,
        'ativo': True,
        'bilhete': 12,
    },
    {
        'numero': 4,
        'ativo': False,
        'bilhete': 0,
    },
    {
        'numero': 5,
        'ativo': True,
        'bilhete': 14,
    },
    {
        'numero': 6,
        'ativo': True,
        'bilhete': 15,
    },
]


def atualiza_socios(lista_socios):
    indexes = []
    for a, b in lista_socios:
        indexes.append(a)

    indexes_db = []
    for t in carteira:
        indexes_db.append(t['numero'])

    for b in carteira:
        for id, bilhete in lista_socios:
            if b['numero'] == id:
                b['bilhete'] = bilhete

            if not b['numero'] in indexes:
                b['ativo'] = False
                b['bilhete'] = 0

    for i, b in lista_socios:
        if not i in indexes_db:
            carteira.append({'numero': i, 'ativo': True, 'bilhete': b})
    return carteira


print(atualiza_socios(lista_socios))

# ----------------------------------------------------------------------------#
