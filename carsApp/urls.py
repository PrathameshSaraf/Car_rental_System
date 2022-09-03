from django.urls import path
from carsApp import views 
urlpatterns = [
    path('',views.cars,name='car'),
    path('<int:id>/',views.car_detail,name='car_detail'),
    path('/search', views.search, name='search'),
]