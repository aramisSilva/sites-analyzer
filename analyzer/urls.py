from django.urls import path

from .views import (
    SiteListCreateView,
    SiteDetailView,
    AnaliseListCreateView,
    AnaliseDetailView, ColetarAnaliseView
)

urlpatterns = [
    path('sites/', SiteListCreateView.as_view(), name='site-list-create'),
    path('sites/<int:pk>/', SiteDetailView.as_view(), name='site-detail'),
    path('analises/', AnaliseListCreateView.as_view(), name='analise-list-create'),
    path('analises/<int:pk>/', AnaliseDetailView.as_view(), name='analise-detail'),
    path('coletar-analise/', ColetarAnaliseView.as_view(), name='coletar-analise'),
]