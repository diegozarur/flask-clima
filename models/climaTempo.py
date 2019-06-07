import peewee
from database import mysql_db
import datetime


class Clima_Tempo(peewee.Model):
    country = peewee.CharField(null=True)
    city_id = peewee.IntegerField(null=True)
    max_day = peewee.IntegerField(null=True)
    min_day = peewee.IntegerField(null=True)
    probability = peewee.IntegerField(null=True)
    precipitation = peewee.IntegerField(null=True)
    name = peewee.CharField(null=True)
    state = peewee.CharField(null=True)
    date = peewee.DateField(null=True)
    created_at = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mysql_db
