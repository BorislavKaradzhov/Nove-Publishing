from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Submission, Genre
from authors.models import Author
from .forms import CreateSubmissionForm, EditSubmissionForm, DeleteSubmissionForm, ChangeStatusForm
from .forms import GenreCreateForm, GenreEditForm, GenreDeleteForm


# --- Submission Views ---

class SubmissionListView(ListView):
    model = Submission
    template_name = 'submissions/list.html'
    context_object_name = 'submissions'
    paginate_by = 3

    def get_queryset(self):
        # Base query with optimized relationships
        queryset = Submission.objects.select_related('author').prefetch_related('genres').all()

        # Capture GET parameters
        sort_by = self.request.GET.get('sort_by')
        order = self.request.GET.get('order', 'asc')

        # Apply sorting
        # Map the HTML dropdown values to the actual database field names
        sort_mapping = {
            'title': 'title',
            'first_name': 'author__first_name',
            'last_name': 'author__last_name',
            'email': 'author__email',
            'status': 'status',
        }

        if sort_by in sort_mapping:
            sort_field = sort_mapping[sort_by]
            # If descending, add a minus sign to the field name
            if order == 'desc':
                sort_field = f'-{sort_field}'
            queryset = queryset.order_by(sort_field)
        else:
            # Default sorting if nothing is selected
            queryset = queryset.order_by('-submitted_at')

        return queryset

    def context_data(self, **kwargs):
        # Pass the authors and status choices to the template for the dropdowns
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all().order_by('last_name')
        context['statuses'] = Submission.STATUS_CHOICES
        return context

class SubmissionDetailView(DetailView):
    model = Submission
    template_name = 'submissions/detail.html'

class SubmissionCreateView(CreateView):
    model = Submission
    form_class = CreateSubmissionForm
    template_name = 'submissions/create.html'
    success_url = reverse_lazy('submission-list')

class SubmissionUpdateView(UpdateView):
    model = Submission
    form_class = EditSubmissionForm
    template_name = 'submissions/edit.html'
    success_url = reverse_lazy('submission-list')

class SubmissionDeleteView(DeleteView):
    model = Submission
    template_name = 'submissions/delete.html'
    success_url = reverse_lazy('submission-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .forms import DeleteSubmissionForm
        context['form'] = DeleteSubmissionForm(instance=self.object)
        return context

class SubmissionChangeStatusView(UpdateView):
    model = Submission
    form_class = ChangeStatusForm
    template_name = 'submissions/change_status.html'

    def get_success_url(self):
        # Redirect back to the detail page to see the updated status
        return reverse_lazy('submission-detail', kwargs={'pk': self.object.pk})


# --- Genre Views ---

class GenreListView(ListView):
    model = Genre
    template_name = 'submissions/genre_list.html'
    context_object_name = 'genres'
    paginate_by = 6
    ordering = ['name']

class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreCreateForm
    template_name = 'submissions/genre_create.html'
    success_url = reverse_lazy('genre-list')

class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreEditForm
    template_name = 'submissions/genre_edit.html'
    success_url = reverse_lazy('genre-list')

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'submissions/genre_delete.html'
    success_url = reverse_lazy('genre-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GenreDeleteForm(instance=self.object)
        return context
