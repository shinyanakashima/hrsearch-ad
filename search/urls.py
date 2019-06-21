from django.urls import path

from . import views

urlpatterns = [
    # ex: /search/
    path('', views.index, name='index'),
    # ex: /search/results/
    path('results/', views.results, name='results'),
    # ex: /search/results/8
    path('results/<int:article_id>/', views.detail, name='detail'),
    path('results/save_csv/', views.save_csv, name='save_csv'),
]
