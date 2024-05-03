"""
URL configuration for Curatio project.

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
from django.urls import include, path

from .views import home, credits, documentation


urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel/', include("panel.urls")),
    path('graphic/', include("graphic.urls")),
    path('statistic/', include("statistic.urls")),
    path('converter/', include("converter.urls")),
    path('scrapper/', include("scrapper.urls")),
    path('auto_explo/', include("auto_explo.urls")),
    path('notebooks/', include("notebooks.urls")),
    
    path('', home, name="home"),
    path('credits/', credits, name="credits"),
    path('documentation/', documentation, name="documentation"),
]
