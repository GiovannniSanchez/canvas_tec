from django.urls import path
from . import views
from .views import home, register


urlpatterns = [
    path('', home, name='Usuario'),
    path('registration/register', register, name='register'),
]