from peewee import *
from os import path

# creating our first database
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Namusavi.db"))


# creating table inside db
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)

from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Namusavi.db"))


class User:
    name = CharField()
    phonenumber = CharField(unique=True)
    age = CharField(int)
    gender = CharField()
    studentcode = CharField(unique=True)

    class Meta:
        database = db


User.create_table(fail_silently=True)
