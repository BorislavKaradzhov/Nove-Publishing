from django.urls import path
from .views import (
    SubmissionListView, SubmissionDetailView, SubmissionCreateView,
    SubmissionUpdateView, SubmissionDeleteView,
    GenreListView, GenreCreateView, GenreUpdateView, GenreDeleteView, SubmissionChangeStatusView
)

urlpatterns = [
    # --- Submission Paths ---
    path('', SubmissionListView.as_view(), name='submission-list'),
    path('create/', SubmissionCreateView.as_view(), name='submission-create'),
    path('<int:pk>/', SubmissionDetailView.as_view(), name='submission-detail'),
    path('<int:pk>/edit/', SubmissionUpdateView.as_view(), name='submission-edit'),
    path('<int:pk>/delete/', SubmissionDeleteView.as_view(), name='submission-delete'),
    path('<int:pk>/change-status/', SubmissionChangeStatusView.as_view(), name='change-status'),

    # --- Genre Paths ---
    path('genres/', GenreListView.as_view(), name='genre-list'),
    path('genres/create/', GenreCreateView.as_view(), name='genre-create'),
    path('genres/<int:pk>/edit/', GenreUpdateView.as_view(), name='genre-edit'),
    path('genres/<int:pk>/delete/', GenreDeleteView.as_view(), name='genre-delete'),
]