from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

def validate_letters_and_dashes(value):
    # Temporarily remove dashes to check if the remaining characters are letters.
    check_value = value.replace('-', '')

    if not check_value.isalpha():
        raise ValidationError("Allowed characters: letters and dashes only.")


class Author(models.Model):
    first_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), validate_letters_and_dashes],
        help_text="First name (letters and dashes only)."
    )
    last_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), validate_letters_and_dashes],
        help_text="Last name (letters and dashes only)."
    )
    email = models.EmailField(
        unique=True,
        help_text="We will contact you at this email regarding your submission."
    )
    bio = models.TextField(
        help_text="Please provide a brief summary about yourself, including any awards, publications, and mentions."
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']
