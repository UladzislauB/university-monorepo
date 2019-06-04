from django.urls import path

from . import views
from .views import SearchView


app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('top_headlines/', views.top_headlines, name='top_headlines'),
    path('search/', SearchView.as_view(), name='search'),
    path('favourites/', views.favourites, name='favourites'),
    path('top_headlines/<int:article_id>/', views.article, name='article')
]
