from rest_framework import routers
from .api import interviewViewSet

router = routers.DefaultRouter()
router.register('api/calificaciones',interviewViewSet,'calificaciones')

urlpatterns = router.urls