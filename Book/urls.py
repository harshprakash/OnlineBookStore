
from django.contrib import admin
from django.urls import path
from . import views
from .views import BookDetailView,SearchResultsView


urlpatterns = [
    path('', views.home,name='home'),
    #path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/',BookDetailView.as_view(),name='detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
]
