from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf.urls import url
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/login/$', obtain_auth_token, name='auth_user_login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^auth/register/$', views.CreateUserAPIView.as_view(), name='auth_user_create'),
]
