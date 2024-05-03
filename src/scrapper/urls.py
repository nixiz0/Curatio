from django.urls import include, path

from .views import *
from .functions.scrap_tools import *


# scrapper/
urlpatterns = [
    path('', scrapper, name="scrapper"),
    path('scrap_email/', scrap_email, name="scrap_email"),
    path('scrap_href/', scrap_href, name="scrap_href"),
    path('scrap_text/', scrap_text, name="scrap_text"),
    path('scrap_images/', scrap_images, name="scrap_images"),
    path('scrap_list/', scrap_list, name="scrap_list"),
    path('scrap_numbers/', scrap_numbers, name="scrap_numbers"),
    path('scrap_content/', scrap_content, name="scrap_content"),
]