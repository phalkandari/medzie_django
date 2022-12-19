"""medzie_django URL Configuration

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
from user.views import UserLoginAPIView, UserCreateAPIView
#  user_register, logout_user, user_login,
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", get_prescriptions, name="home"),

    # path("register/", user_register, name="register"),
    # path("logout/", logout_user, name="logout"),
    # path("login/", user_login, name="login"),

    path("api/signup/", UserCreateAPIView.as_view() , name="signup"),
    path("api/signin/", UserLoginAPIView.as_view() , name="signin"),
]
