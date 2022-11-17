from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.MyNewClass.excelmapping),
    path('doc/', views.MyNewClass.docmapping),
    path('xls/', views.MyNewClass.writeexcel),

]
