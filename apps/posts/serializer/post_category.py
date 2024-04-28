from ..models import PostCategory

from rest_framework import serializers


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = "__all__"
