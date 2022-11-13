"""takming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from website import views
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("captcha/", include("captcha.urls")),
    path("", views.index, name='post-list'),
    path("search/", views.search),
    path("login/", views.login),
    path("logout/", views.logout),
    path("accounts/", include("registration.backends.default.urls")),
    # path("profile/", views.profile),
    path("post/<str:slug>/", views.showpost, name="showpost"),
    path("post/<str:slug>/edit/", views.editpost, name="editpost"),
    path("post/<str:slug>/delete/", views.deletepost, name="deletepost"),
    path("create/", views.createpost),
    path("accounts/profile/", views.profile),
    # path("accounts/login", include("django.contrib.auth.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    # path("accounts/password/reset/", views.password_reset_confirm, name="password_reset_confirm"),
]
