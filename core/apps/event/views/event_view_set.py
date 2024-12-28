from rest_framework.viewsets import ModelViewSet

from core.apps.event.models import Event
from core.apps.event.serializers import EventSerializer


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
