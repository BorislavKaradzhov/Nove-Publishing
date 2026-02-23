from django import forms
from .models import Author

class AuthorBaseForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email', 'bio']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'bio': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tell us about yourself'}),
        }
        labels = {
            'bio': 'Biography & Awards'
        }

class AuthorCreateForm(AuthorBaseForm):
    pass

class AuthorEditForm(AuthorBaseForm):
    pass

class AuthorDeleteForm(AuthorBaseForm):
    """
    Form that displays the data but prevents editing,
    used for the Delete confirmation page.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
