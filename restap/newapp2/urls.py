from django.urls import path
from .import views

urlpatterns=[

    path('home',views.home,name="home"),
    path('app',views.app,name="app"),
    path('search',views.search,name="search"),

    path('company',views.Company_Profile.as_view(),name="company"),
    path('company/<int:pk>',views.Company_Profile.as_view(),name="company"),



]