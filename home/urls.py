from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name ='home'),
    path('signin', views.signin, name = 'signin'),
    path('explore', views.explore, name = 'explore'),
    path('drug', views.drug, name='drug_list')
    ]
    