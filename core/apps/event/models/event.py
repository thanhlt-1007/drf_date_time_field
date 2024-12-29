from django.db.models import CharField, DateTimeField, Model


class Event(Model):
    name = CharField(max_length=255)
    start_at = DateTimeField()
