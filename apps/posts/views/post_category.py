from ..serializer import PostCategorySerializer
from ..models import PostCategory

from rest_framework.viewsets import ModelViewSet


class PostCategoryAPIViewSet(ModelViewSet):
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all()
    lookup_field = "id"
