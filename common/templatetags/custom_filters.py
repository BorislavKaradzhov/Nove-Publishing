from django import template

register = template.Library()

@register.filter
def status_class(status):
    colors = {
        'pending': 'text-warning',
        'review': 'text-info',
        'accepted': 'text-success',
        'rejected': 'text-danger',
    }
    return colors.get(status, 'text-secondary')
