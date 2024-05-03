from django.urls import path

from .views import *


# notebooks/
urlpatterns = [
    path('', notebooks, name="notebooks"),
    path('classic_notebooks/', classic_notebooks, name='classic_notebooks'),
]