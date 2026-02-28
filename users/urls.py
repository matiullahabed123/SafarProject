from django.urls import path, include
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()

router.register("signup", CustomUserViewSet, basename="signup")
# app_name = "users"


urlpatterns = [
  path('login/', LoginAPIView.as_view(), name="login"),
  path("", include(router.urls)),


]
