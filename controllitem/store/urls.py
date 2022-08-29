from rest_framework import routers

from .views import ItemViewSet, ListItemViewSet

router = routers.DefaultRouter()
router.register(r'list-itens', ListItemViewSet)
router.register(r'itens', ItemViewSet)

urlpatterns = router.urls
