"""day3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from controller import InfoController
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InfoController.yiqing),
    path('sendMsg/', InfoController.sendMsg,name='sendMsg'),
    path('sendJson/',InfoController.sendJson),
    path('selectConfirmedCountTopSeven/',InfoController.selectConfirmedCountTopSeven),
    path('selectMap/',InfoController.selectMap),
    path('selectTotal/',InfoController.selectTotal),
    # 查询治愈前七的省份
    path('selectCuredCountTopSeven/',InfoController.selectCuredCountTopSeven),
]
