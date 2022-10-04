from django.urls import path
from .views import (LOGIN, LOGOUT, RegisterUser, EditUser)

app_name = 'users'

urlpatterns = [
    path("", LOGIN, name="LG"),
    path("logout/", LOGOUT, name="LO"),
    # path("users/new/user/add/", RegisterUser, name="RUF"),
    path("users/new/user/add/", RegisterUser.as_view(), name="RUF"),
    path("users/new/user/edit/<pk>/", EditUser.as_view(), name="EUF"),
]