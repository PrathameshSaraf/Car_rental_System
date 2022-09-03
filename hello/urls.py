from django.urls import path
from .views import hello
from .views import about
from . import views
urlpatterns = [
    path('',views.hello,name='home'),
    path('about/',about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'), 
]