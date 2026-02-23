from django.urls import path
from .views import (
    AuthorListView, AuthorDetailView, AuthorCreateView,
    AuthorUpdateView, AuthorDeleteView
)

urlpatterns = [
    path('', AuthorListView.as_view(), name='author-list'),
    path('create/', AuthorCreateView.as_view(), name='author-create'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('<int:pk>/edit/', AuthorUpdateView.as_view(), name='author-edit'),
    path('<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
]