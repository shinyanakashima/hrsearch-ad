from django.urls import path

from . import views

urlpatterns = [
    # ex: /search/
    path('', views.index, name='index'),
    # ex: /search/results/
    path('<str:site_name>/', views.table, name='table'),
    path('<str:site_name>/save_csv/', views.save_csv, name='save_csv'),
    # ex: /search/results/8
    path('<str:site_name>/<int:article_id>/', views.detail, name='detail'),
]
