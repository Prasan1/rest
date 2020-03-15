
from .views import SuperheroViewSet, MemberViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'superhero', SuperheroViewSet, basename='superhero')
router.register(r'members', MemberViewset, basename='superhero')
urlpatterns = router.urls


