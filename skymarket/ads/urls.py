from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers


# TODO настройка роутов для модели

from .views import AdViewSet, AdDetailView, CommentViewSet
ads_router = routers.SimpleRouter()
ads_router.register('ads', AdViewSet, basename='ads')


# urlpatterns = [
#     # path('ads/', views.AdViewSet.as_view({'get': 'list', 'post':'create'})),
#     # path('ads/<int:pk>/', views.AdViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
#     #
#     # path('ads/<int:pk>/comments/', views.CommentViewSet.as_view({'get': 'retrieve', 'post': 'create'})),
#     # # path('ads/<int:pk>/comments/<int:pk>', views.AdViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
#     #
#     # path('ads/me/', views.AdViewSet.as_view({'me': 'list'})),

# ]

urlpatterns = [
    path("", include(ads_router.urls)),
]

