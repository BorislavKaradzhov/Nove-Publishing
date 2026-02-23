from django.contrib import admin
from .models import Genre, Submission

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ...

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    ...
