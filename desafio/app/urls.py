from rest_framework import routers
from app.views import PostoAtendimentoViewSet
from app.views import ClienteViewSet



router = routers.DefaultRouter()
router.register('', PostoAtendimentoViewSet)
router.register('', ClienteViewSet)


urlpatterns = router.urls