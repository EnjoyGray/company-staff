from django import template
from django.urls import reverse
from urllib.parse import urlencode

register = template.Library()

@register.simple_tag(takes_context=True)
def sort_url(context, field, display):
    request = context['request']
    current_ordering = request.GET.getlist('o')
    new_ordering = []

    if field in current_ordering:
        new_ordering = [f"-{field}" if f == field else f for f in current_ordering]
    else:
        new_ordering = current_ordering + [field]

    query_params = request.GET.copy()
    query_params.setlist('o', new_ordering)
    return f'<a href="?{query_params.urlencode()}">{display}</a>'
