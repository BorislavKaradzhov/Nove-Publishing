from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author
from .forms import AuthorCreateForm, AuthorEditForm, AuthorDeleteForm

class AuthorListView(ListView):
    model = Author
    template_name = 'authors/list.html'
    context_object_name = 'authors'
    paginate_by = 6

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/detail.html'
    context_object_name = 'author'

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create.html'
    success_url = reverse_lazy('author-list')

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit.html'
    success_url = reverse_lazy('author-list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/delete.html'
    success_url = reverse_lazy('author-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorDeleteForm(instance=self.object)
        return context
