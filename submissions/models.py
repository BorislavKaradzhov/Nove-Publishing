from django.db import models
from django.core.validators import MinLengthValidator
from authors.models import Author

class Genre(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50
    )

    # Automatically capitalizes the first letter of every word before saving to ensure unique genres.
    def clean(self):
        if self.name:
            self.name = self.name.title()

    def __str__(self):
        return self.name

class Submission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('review', 'Under Review'),
        ('accepted', 'Accepted for Publication'),
        ('rejected', 'Rejected'),
    ]

    title = models.CharField(
        max_length=200,
        help_text="Please enter the title of the submission.",
    )
    synopsis = models.TextField(help_text="Please provide a short synopsis of the story.")
    script_sample = models.TextField(
        validators=[MinLengthValidator(1000)],
        help_text="Please provide a part of the actual book script (min 1000 characters).")
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')

    # Relationships
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='submissions',
        help_text="Please select an author or add a new author by visiting Main/Top Menu -> Authors."
    )
    genres = models.ManyToManyField(
        Genre,
        related_name='submissions',
        help_text="Please select applicable genres or add a new genre by visiting Main/Top Menu -> Genres."
    )

    objects = models.Manager()

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return self.title
