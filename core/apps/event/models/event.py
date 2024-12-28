from django.db.models import CharField, Model


class Event(Model):
    name = CharField(max_length=255)
