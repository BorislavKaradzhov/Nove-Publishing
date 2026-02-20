from django import forms
from .models import Submission

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
