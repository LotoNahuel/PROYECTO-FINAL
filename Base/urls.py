from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="inicio"),
    path("diseños/", diseños, name="diseños"),
    path("otroFilter/", otroFilter, name="otroFilter"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
]