from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    email = models.EmailField(unique=True, help_text="We will contact you at this email regarding your submission.")
    bio = models.TextField(help_text="Please provide a brief summary about the author, awards, publications, and mentions.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
