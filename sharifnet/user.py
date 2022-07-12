import os

from peewee import SqliteDatabase, Model, CharField, BooleanField


db = SqliteDatabase(os.path.join(os.path.dirname(__file__), '..', 'sharifnet.db'))


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True, primary_key=True)
    password = CharField()
    is_default = BooleanField(default=False)


db.connect(reuse_if_open=True)
db.create_tables([User], safe=True)
