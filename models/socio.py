import peewee
from database import mysql_db
import datetime


class Socio(peewee.Model):
    ativo = peewee.SmallIntegerField(null=True)
    bilhete = peewee.IntegerField(null=True)
    created_at = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mysql_db