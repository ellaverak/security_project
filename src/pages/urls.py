from django.urls import path

from pages.views import Index, Home, Register, Login, Save, Logout

urlpatterns = [
    path('', Index, name='index'),
    path('home/', Home, name='home'),
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('save/', Save, name='save'),
    path('logout/', Logout, name='logout')
]
