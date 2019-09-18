from rest_framework import routers
from .api import SensorViewSet

router = routers.DefaultRouter()
router.register('api/core', SensorViewSet, 'core')

urlpatterns = router.urls
