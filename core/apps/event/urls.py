from rest_framework import routers

from core.apps.event.views import EventViewSet

router = routers.SimpleRouter()
router.register(r"events", EventViewSet)
urlpatterns = router.urls
