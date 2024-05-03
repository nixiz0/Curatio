from django.urls import include, path

from .views import statistic, statistic_import_csv
from .functions.statistic_functions import *


# statistic/
urlpatterns = [
    path('', statistic, name="statistic"),
    
    path('upload_csv/', statistic_import_csv, name="statistic_upload_csv"),
    path('pca/', pca, name="pca"),
    path('chi_square/', chi_square, name="chi_square"),
    path('shapiro_wilk/', shapiro_wilk, name="shapiro_wilk"),
    path('features_importance/', features_importance, name="features_importance"),
]