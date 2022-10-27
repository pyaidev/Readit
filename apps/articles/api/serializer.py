from rest_framework import serializers
from ..models import Article


class ArticleGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'get_image_url', 'category', 'context', 'tags', 'views', 'created_at']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'image', 'category', 'context', 'tags', 'views', 'created_at']
        extra_kwargs = {
            'views':{'read_only': True}
        }