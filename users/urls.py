from django.urls import path
from .views import (LOGIN, LOGOUT, RegisterUser, EditUser, ChangePassword)
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

app_name = 'users'

urlpatterns = [
    path("", LOGIN, name="LG"),
    path("logout/", LOGOUT, name="LO"),
    # path("users/new/user/add/", RegisterUser, name="RUF"),
    path("users/new/user/add/", RegisterUser.as_view(), name="RUF"),
    path("users/new/user/edit/<pk>/", EditUser.as_view(), name="EUF"),
    path("users/user/edit/password/<pk>/", ChangePassword, name="change_password"),
    # path('change_password/', PasswordChangeView.as_view(), name='password_change')
]