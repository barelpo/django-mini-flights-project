"""
URL configuration for mini_flights project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from mini_flights_app.auth.views import UserViewSet, me
from mini_flights_app.flights.views import FlightViewSet

router_user = routers.DefaultRouter()
router_user.register(r'api/auth/users', UserViewSet)

router_flight = routers.DefaultRouter()
router_flight.register(r'api/flights', FlightViewSet)

urlpatterns = [
    path('api/auth/login', TokenObtainPairView.as_view()),
    path('api/auth/refresh', TokenRefreshView.as_view()),
    path('api/auth/me', me)
]

urlpatterns.extend(router_user.urls)
urlpatterns.extend(router_flight.urls)

