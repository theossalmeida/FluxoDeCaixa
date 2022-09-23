from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:lancamento_id>', views.ver_lancamento, name='ver_lancamento'),
    path('busca/', views.busca, name='busca')
]