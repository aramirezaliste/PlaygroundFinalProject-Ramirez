from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("register/", views.register, name="register"),
    path("logout/", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("profile_edit/", views.profile_edit, name="profile_edit"),
]