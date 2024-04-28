from ..serializer import PostSerializer
from ..models import Post

from rest_framework.viewsets import ModelViewSet


class PostAPIViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "id"
