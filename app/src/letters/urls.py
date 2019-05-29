from django.urls import path, include, re_path
from .views import letter_view


urlpatterns = [
    path('', letter_view, name='letter_view'),
]
