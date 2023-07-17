from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views.author import AuthorViewSet
from .views.user import UserViewSet

router = SimpleRouter()
router.register(
    'authors',
    AuthorViewSet
)
router.register(
    'users',
    UserViewSet
)


urlpatterns = [
    path('', include(router.urls))
]
