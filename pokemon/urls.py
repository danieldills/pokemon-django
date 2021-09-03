from django.urls import path
from .views import PokemonListView, PokemonDetailView, PokemonCreateView, PokemonUpdateView, PokemonDeleteView

urlpatterns = [
    path('', PokemonListView.as_view(), name='pokemon_list'),
    path('<int:pk>/', PokemonDetailView.as_view(), name='pokemon_detail'),
    path('create/', PokemonCreateView.as_view(), name='pokemon_create'),
    path('<int:pk>/update/', PokemonUpdateView.as_view(), name='pokemon_update'),
    path('<int:pk>/delete/', PokemonDeleteView.as_view(), name='pokemon_delete'),
]
