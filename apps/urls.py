from django.urls import include, path

urlpatterns = [path("", include("apps.posts.urls"))]
