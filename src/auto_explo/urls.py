from django.urls import include, path

from .views import *


# auto_explo/
urlpatterns = [
    path('', auto_explo, name="auto_explo"),
    path('ydata_explo/', ydata_explo, name="ydata_explo"),
    path('sweetviz_explo/', sweetviz_explo, name="sweetviz_explo"),
]