from django.db import models
from django.core.validators import MinLengthValidator
from authors.models import Author

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Submission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('review', 'Under Review'),
        ('accepted', 'Accepted for Publication'),
        ('rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=200)
    synopsis = models.TextField(help_text="Please provide a short synopsis including story description and targeted audience.")
    script_sample = models.TextField(
        validators=[MinLengthValidator(10000)],
        help_text="Please provide a part of the actual book script (min 10000 characters).")
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')

    # Relationships
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='submissions')
    genres = models.ManyToManyField(Genre, related_name='submissions')

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return self.title
