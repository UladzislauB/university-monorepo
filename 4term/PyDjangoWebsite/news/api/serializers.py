from rest_framework import serializers

from likes import services as likes_services
from ..models import TopHeadline


class TopHeadlineSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = TopHeadline
        fields = (
            'id',
            'title',
            'author',
            'description',
            'url',
            'urlToImage',
            'publishedAt',
            'is_fan',
            'total_likes',
        )

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)
