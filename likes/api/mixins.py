from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .. import services
from .serializers import FanSerializer
from news.api.serializers import TopHeadlineSerializer


class LikedMixin:

    @detail_route(methods=['POST'])
    def like(self, request, pk=None):
        obj = self.get_object()
        if services.is_fan(obj, request.user):
            services.remove_like(obj, request.user)
        else:
            services.add_like(obj, request.user)
        is_fan = services.is_fan(obj, request.user)
        return Response({"is_fan": is_fan, "total_likes": obj.total_likes})

    @detail_route(methods=['POST'])
    def unlike(self, request, pk=None):
        obj = self.get_object()
        services.remove_like(obj, request.user)
        return Response()

    @detail_route(methods=['GET'])
    def fans(self, request, pk=None):
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)

    @detail_route(methods=['GET'])
    def watch(self, request, pk=None):
        obj = self.get_object()
        obj.views = obj.views + 1
        obj.save()
        print(obj.views)
        return Response({"views": obj.views})
