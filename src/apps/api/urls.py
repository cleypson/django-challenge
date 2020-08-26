from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token,\
    verify_jwt_token
from apps.api import views

router = routers.DefaultRouter()
router.register(r'signup', views.UserSignupViewSet, basename='signup')
router.register(r'projects', views.ProjectViewSet)
router.register(r'nevers', views.NeverViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('verify-token/', verify_jwt_token),
]
