from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token,\
    verify_jwt_token

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('verify-token/', verify_jwt_token),
]
