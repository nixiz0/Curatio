from django.urls import include, path

from .views import *


# converter/
urlpatterns = [
    path('', converter, name="converter"),
    
    path('string_converter/', string_converter, name="string_converter"),
    path('object_converter/', object_converter, name="object_converter"),
    path('int_converter/', int_converter, name="int_converter"),
    path('float_converter/', float_converter, name="float_converter"),
    path('bool_converter/', bool_converter, name="bool_converter"),
    path('date_converter/', date_converter, name="date_converter"),
]