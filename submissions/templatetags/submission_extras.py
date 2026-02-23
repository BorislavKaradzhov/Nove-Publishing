from django import template

register = template.Library()

@register.filter
def status_percentage(status):
    """Maps status string to a percentage value for a progress bar."""
    mapping = {
        'pending': 25,
        'review': 50,
        'accepted': 100,
        'rejected': 100,
    }
    return mapping.get(status, 0)

@register.filter
def status_color(status):
    """Maps status string to a Bootstrap contextual colors for a progress bar."""
    colors = {
        'pending': 'bg-warning',
        'review': 'bg-info',
        'accepted': 'bg-success',
        'rejected': 'bg-danger',
    }
    return colors.get(status, 'bg-secondary')
