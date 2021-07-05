from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include, re_path
from rest_framework import routers
from api.views import UserViewSet
from django.conf.urls import url
from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/login/$', obtain_auth_token, name='auth_user_login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
