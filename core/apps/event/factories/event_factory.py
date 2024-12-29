from factory.django import DjangoModelFactory
from factory.faker import Faker


class EventFactory(DjangoModelFactory):
    class Meta:
        model = "event.Event"

    name = Faker(provider="name")
    start_at = Faker(provider="date_time")
