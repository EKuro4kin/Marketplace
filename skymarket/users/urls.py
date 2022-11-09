from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

user_router = SimpleRouter()
user_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(user_router.urls)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
