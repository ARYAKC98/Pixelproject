from django.urls import path
from logapp import views

urlpatterns=[
    path('log_page/', views.log_page, name='log_page'),
    path('home_page/', views.home_page, name='home_page'),
    path('save_regdb/', views.save_regdb, name='save_regdb'),
    path('userlogin/', views.userlogin, name='userlogin'),

]