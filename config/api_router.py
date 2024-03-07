from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from langcorrect.posts.api.views import PostViewSet
from langcorrect.users.api.views import UserViewSet

router = (
    DefaultRouter(trailing_slash=False)
    if settings.DEBUG
    else SimpleRouter(trailing_slash=False)
)

router.register("users", UserViewSet)
router.register("posts", PostViewSet)


app_name = "api"
urlpatterns = router.urls
