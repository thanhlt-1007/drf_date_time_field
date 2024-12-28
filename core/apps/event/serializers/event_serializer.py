from rest_framework.serializers import ModelSerializer

from core.apps.event.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
