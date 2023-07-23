from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from . import services


class LikedMixin(GenericViewSet):

    @action(detail=True,
            methods=['POST'],
            permission_classes=[IsAuthenticated]
            )
    def like(self, request, pk=None, news_id=None):
        services.add_like(obj=self.get_object(), user=request.user)
        return Response({'status': 'ok'})

    @action(detail=True,
            methods=['POST'],
            permission_classes=[IsAuthenticated]
            )
    def unlike(self, request, pk=None, news_id=None):
        services.remove_like(obj=self.get_object(), user=request.user)
        return Response({'status': 'ok'})
