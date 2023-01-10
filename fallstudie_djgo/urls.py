"""fallstudie_djgo URL Configuration

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

from fideo.views import (
    about_us_view,
    fideo_view,
    home_view,
    impressum_view,
    login_view,
    factory,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # add urls for each page on website
    path("", home_view, name="index"),
    path("fideo/", fideo_view, name="fideo"),
    path("aboutUs/", about_us_view, name="aboutUs"),
    path("impressum/", impressum_view, name="impressum"),
    path("login/", login_view, name="login"),
    path("factory/" , factory)
]