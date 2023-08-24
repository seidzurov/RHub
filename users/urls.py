from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path("profile/", profiles_list, name="profiles_list"),
    path("profile/<int:pk>", profile, name="profile"),
]
