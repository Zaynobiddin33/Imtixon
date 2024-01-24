from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('services', service, name='service')

]