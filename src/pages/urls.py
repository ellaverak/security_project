from django.urls import path

from pages.views import Index

urlpatterns = [
    path('', Index, name='index')
]
