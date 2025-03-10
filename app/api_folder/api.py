from rest_framework import routers

from .views import (
    ZonesProtgesDuSngal_Api_ViewSet,
)

router = routers.DefaultRouter()
router.register(r"ZonesProtégées", ZonesProtgesDuSngal_Api_ViewSet)

urlpatterns = router.urls