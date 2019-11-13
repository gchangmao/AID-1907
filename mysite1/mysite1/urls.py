"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #127.0.0.1:8000/page1;交由views.page_view方法处理
    url(r'^page1$',views.page_view),
    # 127.0.0.1:8000/page2;交由views.page_view方法处理
    url(r'^page2$', views.page1_view),
    # 127.0.0.1:8000/page3;交由views.page_view方法处理
    url(r'^page3$', views.page2_view),
    #page4  --page 100 1到100页
    url(r'^page(\d+)',views.pagen_view)
]
