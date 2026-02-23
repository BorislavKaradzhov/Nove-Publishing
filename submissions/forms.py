from django import forms
from .models import Submission, Genre


# --- Submission Forms ---

class SubmissionBaseForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'author', 'genres', 'synopsis', 'script_sample']
        widgets = {
            'synopsis': forms.Textarea(attrs={'placeholder': 'Enter the story summary...', 'rows': 3}),
            'genres':forms.CheckboxSelectMultiple(),
        }
        labels = {
            'script_sample': 'Book Script Snippet'
        }

class CreateSubmissionForm(SubmissionBaseForm):
    pass

class EditSubmissionForm(SubmissionBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].disabled = True # Author shouldn't change after submission

class DeleteSubmissionForm(SubmissionBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

# Change status form
class ChangeStatusForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'})
        }


# --- Genre Forms ---

class GenreBaseForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter the genre name...'}),
        }
        labels = {
            'name': 'Genre Name'
        }

class GenreCreateForm(GenreBaseForm):
    pass

class GenreEditForm(GenreBaseForm):
    pass

class GenreDeleteForm(GenreBaseForm):
    """Read-only form for delete confirmation"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].disabled = True
