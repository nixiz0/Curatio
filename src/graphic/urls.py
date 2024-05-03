from django.urls import include, path

from .views import graphic, graphic_import_csv
from .functions.graphic_functions import *


# graphic/
urlpatterns = [
    path('', graphic, name="graphic"),
    
    path('upload_csv/', graphic_import_csv, name="graphic_upload_csv"),
    
    path('histogram/', histogram, name="histogram"),
    path('boxplot/', boxplot, name="boxplot"),
    path('scatter/', scatter, name="scatter"),
    path('pie/', pie, name="pie"),
    path('heatmap/', heatmap, name="heatmap"),
    path('violin/', violin, name="violin"),
    path('butterfly/', butterfly, name="butterfly"),
    path('stem/', stem, name="stem"),
    path('bar_chart/', bar_chart, name="bar_chart"),
]