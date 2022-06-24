from django.urls import path
from recipes.views import home, contato, sobre

urlpatterns = [
    path('', home), # Home, página inicial do site
    path('contato/', contato), # Contato
    path('sobre/', sobre), # Sobre
]
