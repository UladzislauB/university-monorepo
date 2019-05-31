from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('top_headlines/', views.top_headlines, name='top_headlines'),
    path('top_headlines/<int:article_id>/', views.article, name='article')
]
