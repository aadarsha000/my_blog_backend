from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import PostAPIViewSet, PostCategoryAPIViewSet

router = DefaultRouter()

router.register("posts", PostAPIViewSet)
router.register("post-categories", PostCategoryAPIViewSet)

urlpatterns = [path("", include(router.urls))]
