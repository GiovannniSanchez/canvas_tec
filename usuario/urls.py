from django.urls import path
from . import views
from .views import home, products, register


urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('registration/register', register, name='register'),
]