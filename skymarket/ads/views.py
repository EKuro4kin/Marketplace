from rest_framework import pagination, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Ad, Comment
from .filters import AdFilter
from .serializers import AdSerializer, CommentSerializer
from rest_framework.decorators import action


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AdViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,) # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filterset_class = AdFilter # Выбираем наш фильтр
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    permission_classes = []

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'me']:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    # def get_serializer_class(self):
    #     if self.action == "retrieve":
    #         return AdDetailSerializer
    #     return AdSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



    @action(detail=False, methods=["get"])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)






