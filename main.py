import peewee
from models.climaTempo import Clima_Tempo
from models.socio import Socio

if __name__ == '__main__':
    try:
        Clima_Tempo.create_table()
        print('create Clima Tempo table')
    except peewee.OperationalError:
        print('Table Clima Tempo Already exist!')

    try:
        Socio.create_table()
        print('create Socio table')
    except peewee.OperationalError:
        print('Table Socio Already exist!')
