from django.urls import path

from .views import *

urlpatterns = [
    path('home/', index, name='home'),
    path('cats/<slug:cats>/', categories)
]