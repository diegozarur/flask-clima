import peewee

mysql_db = peewee.MySQLDatabase('climatempo',
                                user='root',
                                password='123',
                                host='localhost',
                                port=3131)
